---
layout: post
title:  Wikipedia bloqueada en CANTV desde el 12 de Enero.
excerpt: El sitio web de todas las ediciones de Wikipedia fue bloqueado por CANTV, el proveedor de internet del estado Venezolano, del 12 al 14 de Enero de 2019
permalink: /noticias/wikipedia_2019-01/
date:   2019-01-15 6:30:00 -0400
categories: bloqueos
image: /res/post_img/2019-01-18-wikipedia.png
author: "Andrés Azpúrua"
lang: es
---


Desde la mañana del sábado 12 de Enero de 2018, los usuarios de CANTV han tenido problemas para acceder a Wikipedia, la enciclopedia libre, en todas sus ediciones por un bloqueo intencional con aparentes motivos políticos. El ha podido ser medido intermitentemente desde entonces.

Actualización 2019-01-19: El bloqueo culminó el viernes 18 de Enero.

El bloqueo ocurrió luego de ediciones a varios artículos de wikipedia haciendo referencia a Juan Guaidó y la presidencia de la República Bolivariana de Venezuela. El artículo de Juan Guaidó, Presidente de la Asamblea Nacional (parlamento) llegó a nombrarlo Presidente de la República, entre otros cambios controversiales. Imágenes de su artículo se volvieron virales en Venezuela y la guerra de ediciones fue [cubierta por la prensa nacional]().

Análisis técnicos de VEsinFiltro, con colaboración de OONI, y análisis de NetBlocks también evidenciaron la existencia del bloqueo independientemente.

Nuestro análisis coloca a este bloqueo en la categoría de bloqueo HTTP; específicamente funciona bloqueando los paquetes del _TLS handshake_, necesario para  establecer una conexión segura con el servidor. El bloqueo se realiza filtrando los paquetes cuyo SNI (Server Name Indicación) termina en wikipedia.org. Al impedir que se establezca la conexión segura con el servidor, se impide la navegación a cualquier pagina de Wikipedia.

Similar a otros bloqueos en 2018, el bloqueo no fue uniformemente efectivo, con una tasa de conexiones bloqueadas que varió durante la vida del mismo. El bloqueo sólo fue detectable en CANTV, el proveedor de internet estatal que además maneja la gran mayoría de las conexiones residenciales a internet.

## Detalles del análisis técnico

Pruebas de [publicadas en Ooni Explorer](https://explorer.ooni.torproject.org/measurement/20190113T203747Z_AS8048_zmgCmhj2SnRKM6utWKbrj2GHz9UFtYq5db0nYWIbSJzDsHOXWE?input=http://wikipedia.org) muestran que no se puede cargar la página de Wikipedia desde CANTV (ASN 8048) a pesar de haber resuelto DNS correctamente y de establecer conexión TCP con el servidor exitosamente.

Intentos de conexión a wikipedia suelen fallar en el _handshake_ TLS, pero cuando la sesión TLS se establece exitosamente, por la razón que fuese, se puede navegar la página durante esa sesión del navegador.

Ejemplo de múltiples pruebas:
```shell
$ curl -v https://es.wikipedia.org
* Rebuilt URL to: https://es.wikipedia.org/
*   Trying 208.80.154.224...
* TCP_NODELAY set
* Connected to es.wikipedia.org (208.80.154.224) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to es.wikipedia.org:443
* stopped the pause stream!
* Closing connection 0
curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to es.wikipedia.org:443
```

Como se pudo observar que no hubo respuesta al primer mensaje del _TLS handshake_, _Client Hello_. Pero sí se pudo establecer una conexión TCP con el servidor, el bloqueo parecía ser en la capa de aplicación impidiendo la sesión TLS. Esto coincide con la experiencia de usuarios en sus navegadores web, si la sesión TLS se establece por cualquier vía el usuario puede navegar en Wikipedia.

Para probar que el bloqueo funciona únicamente filtrado según el SNI (Server Name Indication), realizamos varios experimentos que se repitieron múltiples veces y posteriormente se usaron para monitorear la continuidad del bloqueo.

Realizamos conexiones a servidores no relacionados con Wikipedia que no estuvieran bloqueados, pero haciendo la solicitud pidiendo la URL de wikipedia; de esta forma se conecta a un servidor distinto pero el SNI dice "www.wikipedia.org" "es.wikipedia.org" o similar.

Si no hay bloqueo por TLS se recibiría la respuesta del servidor no bloqueado, se completaría el handshake TLS pero diría que ese servidor no tiene un certificado para "www.wikipedia.org" o el dominio del SNI que se uso en la prueba. En cambio, se esperaría que falle el handshake si hay un bloqueo que solo toma en cuenta el SNI.

Los resultados obtenidos probando conectarse a servidores no relacionados usando un SLI de wikipedia muestran lo mismo que las conexiones a Wikipedia.com y todas sus ediciones, falla por no recibir respuesta a _Client Hello_ del handshake TLS.

Ejemplo de múltiples pruebas:
```shell
$ curl -v --connect-to ::www.kernel.org: https://www.wikipedia.org
* Rebuilt URL to: https://www.wikipedia.org/
* Connecting to hostname: www.kernel.org
*   Trying 147.75.58.133...
* TCP_NODELAY set
* Connected to www.kernel.org (147.75.58.133) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.wikipedia.org:443
* stopped the pause stream!
* Closing connection 0
curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.wikipedia.org:443
```
Para confirmar el bloqueo TLS y descartar otros posibles bloqueos sobre wikipedia, se realizaron pruebas opuestas a la anterior: solicitar un sitio cualquiera, distinto de Wikipedia, a lo servidores de wikipedia. El resultado es consistente con el anterior: el servidor de wikipedia sí responde al _Client Hello_ del handshake TLS, cuando el NSI no es de wikipedia. Adicionalmente no se evidencia ningún otro tipo de bloqueo aplicado a Wikipedia.

Ejemplo de múltiples pruebas:
```shell
curl -v --connect-to ::www.wikipedia.org: https://www.kernel.org
* Rebuilt URL to: https://www.kernel.org/
* Connecting to hostname: www.wikipedia.org
*   Trying 208.80.154.224...
* TCP_NODELAY set
* Connected to www.wikipedia.org (208.80.154.224) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Client hello (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-ECDSA-CHACHA20-POLY1305
* ALPN, server accepted to use h2
* Server certificate:
*  subject: C=US; ST=California; L=San Francisco; O=Wikimedia Foundation, Inc.; CN=*.wikipedia.org
*  start date: Nov  8 21:21:04 2018 GMT
*  expire date: Nov 22 07:59:59 2019 GMT
*  subjectAltName does not match www.kernel.org
* SSL: no alternative certificate subject name matches target host name 'www.kernel.org'
* stopped the pause stream!
* Closing connection 0
* TLSv1.2 (OUT), TLS alert, Client hello (1):
curl: (51) SSL: no alternative certificate subject name matches target host name 'www.kernel.org'
```

Adicionalmente se realizaron pruebas conectándose a Wikipedia mediante SNI encriptado (ESNI), que transmite el nombre del servidor solicitado de forma encriptada, y terceros como el ISP no pueden leer. Se pudo cargar sin experimentar el bloqueo el sitio de Wikipedia usando ESNI en Firefox Nightly.

Todo esto confirma que el bloqueo es un filtrado por SNI, impidiendo el establecimiento de una conexión segura con el servidor y sugiere que no hay otro tipo de bloqueo implementado, varios tipos de bloqueos fueron directamente descartados por el resultado de estas pruebas. Pudimos observar que la tasa bloqueo era alta, pero menor a 100%; por lo que algunos usuarios insistentes pudieran establecer conexiones con el servidor.

Pudimos verificar con la técnica de internar un handshake TLS a terceros servidores que el filtrado SNI ocurre para cualquier * wikipedia.org, abarcando todas las ediciones de wikipedia pero también dominios que no se están usando como foo.wikipedia.org y cualquiercosawikipedia.org. Técnicamente el bloqueo estaría afectando cualquier otro sitio, si existiera, con un dominio que termine en wikipedia.org.

![Cover image](/res/post_img/2019-01-18-wikipedia.png)


### Agradecimientos
Agradecemos a Ooni por su plataforma y software, que hemos usado de diversas maneras en múltiples estudios por años y Simonne Basso por recomendaciones técnicas claves mejorar el análisis.
