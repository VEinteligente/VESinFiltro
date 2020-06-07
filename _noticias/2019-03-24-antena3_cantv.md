---
layout: post
title:  Venezuela bloquea en internet a Antena 3 Internacional.
excerpt: "El sitio de Antena 3 Internacional ha sido bloqueado, impidiendo que se vea su transmisión por internet. Ya había sido censurado en servicios de TV por suscripción."
permalink: /noticias/antena3_2019-03/
date:   2019-03-24 16:30:00 -0400
categories: bloqueos
image: /res/post_img/2019-03-24-post.png
author: "Andrés Azpúrua"
lang: es
---

El sitio de **[Antena 3 Internacional](antena3internacional.com) ha sido bloqueado en Venezuela por CANTV**, proveedor de internet mas importante del país y una empresa estatal. Este bloqueo existe al menos desde 2019-03-24, fecha en la que empezamos a registrar el estado de antena3internacional.com.

**Este bloqueo impide disfrutar de la transmisión por internet del canal que fue habilitado para su audiencia en Venezuela**. Antena 3 Internacional [había habilitado un streaming en vivo para usuarios en Venezuela](https://twitter.com/antena3int/status/1107630484505403393) *www.antena3internacional.com/venezuela/*, en respuesta a a la censura del canal en servicios de TV por cable y satélite desde 2019-02-23 por ordenes del regulador de las telecomunicaciones, CONATEL.

![antena3int tweet](/res/post_img/2019-03-24/antena3int_tweet.png)

El bloqueo se basa en los protocolos HTTP y HTTPS y deja casi sin opciones a usuarios de CANTV. El cambio de servidores DNS no tiene efecto sobre este bloqueo y el uso de la mayoría de los VPNs sería registrado por el servidor de streaming de Antena 3 como una conexión fuera de Venezuela.

![Cover image](/res/post_img/2019-03-24-post.png)


## Métodos y detalles técnicos
Esta alerta se sustenta múltiples mediciones de red de distintos tipos, incluyendo pruebas manuales y realizadas mediante OONI en dispositivos de voluntarios de VE sin Filtro y una red de medición de VE sin Filtro.

Esperamos publicar las mediciones de OONI cuando estén publicadas en los repositorios en línea. Las pruebas de OONI sustentan el bloqueo HTTP/HTTPS desde numerosos puntos.

Pruebas con el navegador Mozilla Firefox con ESNI (SNI encriptado) habilitado parecen mostrar que el servidor de Antena 3 Internacional no lo soporta, limitando la posibilidad de evadir este bloqueo.

Pruebas detalladas, desde varios puntos pero un número mucho menor, evidencian que el bloqueo HTTPS utiliza Filtrado por SNI. El bloqueo HTTPS y HTTP es aplicado para cualquier solicitud a ** \*antena3internacional.com ** (cualquier cosa que termine en *antena3internacional.com*)

Ejemplos de muchos experimentos manuales:
```
$ nc -vtzw 15 www.antena3internacional.com 443
www.antena3internacional.com [104.71.253.206] 443 (https) open
MacBook-Pro-4:~ nano$ nc -vtzw 15 www.antena3internacional.com 80
www.antena3internacional.com [104.71.253.206] 80 (http) open


$ curl -v --connect-to ::www.wikipedia.org: https://www.antena3internacional.com
* Rebuilt URL to: https://www.antena3internacional.com/
* Connecting to hostname: www.wikipedia.org
*   Trying 208.80.154.224...
* TCP_NODELAY set
* Connected to www.wikipedia.org (208.80.154.224) port 443 (#0)
    (...)
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.antena3internacional.com:443
* stopped the pause stream!
* Closing connection 0
curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.antena3internacional.com:443


$ curl -v --connect-to ::www.wikipedia.org: https://cualquiercosaantena3internacional.com
* Rebuilt URL to: https://cualquiercosaantena3internacional.com/
* Connecting to hostname: www.wikipedia.org
*   Trying 208.80.154.224...
* TCP_NODELAY set
* Connected to www.wikipedia.org (208.80.154.224) port 443 (#0)
    (...)
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* Operation timed out after 300153 milliseconds with 0 out of 0 bytes received
* stopped the pause stream!
* Closing connection 0
curl: (28) Operation timed out after 300153 milliseconds with 0 out of 0 bytes received


$ curl -v --connect-to ::www.antena3internacional.com: https://www.wikipedia.org
* Rebuilt URL to: https://www.wikipedia.org/
* Connecting to hostname: www.antena3internacional.com
*   Trying 104.71.253.206...
* TCP_NODELAY set
* Connected to www.antena3internacional.com (104.71.253.206) port 443 (#0)
    (...)
* SSL: no alternative certificate subject name matches target host name 'www.wikipedia.org'
* stopped the pause stream!
* Closing connection 0
* TLSv1.2 (OUT), TLS alert, Client hello (1):
curl: (51) SSL: no alternative certificate subject name matches target host name 'www.wikipedia.org'
```
