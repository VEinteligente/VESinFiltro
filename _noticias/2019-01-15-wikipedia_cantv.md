---
layout: post
title:  Wikipedia bloqueada en CANTV desde el 12 de Enero.
small: El sitio web de todas las ediciones de Wikipedia fue bloqueado por CANTV, el proveedor de internet del estado Venezolano, del 12 al 14 de Enero de 2019
permalink: /noticias/wikipedia_2019-01/
date:   2019-01-15 6:30:00 -0400
categories: bloqueos
image: /res/post_img/2019-01-15-wikipedia.png
author: "Andrés Azpúrua (Venezuela Inteligente / VEsinFiltro)"
---


Desde la mañana del sábado 12 de Enero de 2018, los usuarios de CANTV han tendio para acceder Wikipedia, la enciclopedia libre, en todas sus ediciones por un bloqueo intencional con aparentes motivos políticos. El ha podido ser medido intermitentemente desde entonces.

El bloqueo ocurrió luego de ediciones a varios artículos de wikipedia haciendo referencia a Juan Guaidó y la presidencia de la República Bolivariana de Venezuela. El artículo de Juan Guaidó, Presidente de la Asamblea Nacional (parlamento) llegó a nombrarlo Presidente de la República, entre otros cambios controversiales. Imágenes de su artículo se volvieron virales en Venezuela y la guerra de ediciones fue [cubierta por la prensa nacional]().

Análisis técnicos de VEsinFiltro, con colaboración de OONI, y análisis independientementes de NetBlocks han comprobaron la existencia del bloqueo.

Nuestro análisis coloca a este bloqueo en la categoría de bloqueo HTTP; específicamente funciona bloqueando los paquetes del _TLS handshake_, neceisario para  establecer una conexión segura con el servidor. El bloqueo se realiza filtrando los paquetes cuyo SNI (Server Name Indication) termina en wikipedia.org. Al impedir que se establezca la conexión segura con el servidor, se impide la navegación a cualquier pagina de Wikipedia. 

Similar a otros bloqueos en 2018, el bloqueo no fue uniformemente efectivo, con una tasa de conexiones bloqueadas que varió durante la vida del mismo. El bloqueo sólo fue detectable en CANTV, el proveedor de internet estatal que además maneja la gan mayoría de las conexiones residenciales a internet.

## Detalles del análisis técnico

Pruebas de [publicadas en Ooni Explorer](https://explorer.ooni.torproject.org/measurement/20190113T203747Z_AS8048_zmgCmhj2SnRKM6utWKbrj2GHz9UFtYq5db0nYWIbSJzDsHOXWE?input=http://wikipedia.org) muestran que no se puede cargar la página de Wikipedia desde CANTV (ASN 8048) a pesar de haber resuelto DNS correctamente y de establecer conexión TCP con el servidor exitosamente. 

Intentos de conexión a wikipedia suelen fallar en el _handshake_ TLS, pero cuando la sesión TLS se establece exitosamente, por la razón que fuese, se puede navegar la página durante esa sesión del navegador. 

Ejemplo
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

Como se pudo observar que no hubo respuesta al primer mensaje del _TLS handshake_, _Client Hello_. Pero sí se pudo establercer una connexión TCP con el servidor, el bloqueo parecía ser en la capa de aplicación impidiendo la sesión TLS. Esto coincide con la expeiencia de usuarios en sus navegadores web, si la sesión TLS se establece por cualquier vía el usuario puede navegar en Wikipedia.

Para probar que el bloqueo funciona únicamente filtrado se hacía según el SNI (Server Name Indication), realizamos conexiones a servidores no relacionados con Wikipedia que no estuvieran bloqueados pero haciendo la solicitud pididendo la URL de wikipedia; de esta forma se conexta a un servidor destinto pero el SNI dice "www.wikipedia.org" o similar. Si no hya bloqueo por TLS se recibiría la respuesta del servidor y completarse el handshake aunque el servidor no hospede ese url.

Ejemplo:
```shell
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

Adicionalmente se realizaron pruebas conectandose a Wikipedia mediante SNI encriptado (ESNI), que transmite el nombre del servidor solicitado de forma encryptada, y terceros como el ISP no pueden leer.

Pudimos verificar con la técnica de internar un handshake TLS a terceros servidores que el filtrado SNI ocurre para cualquier * wikipedia.org, abarcando todas las ediciones de wikipedia pero tambien dominios que no se están usando como foo.wikipedia.org y cualquiercosawikipedia.org. Técnicamente el bloqueo estaría afectando cualquier otro sitio, si exitistiera, con un dominio que termine en wikipedia.org.


![Cover image](/res/post_img/2019-01-15-wikipedia.png)
