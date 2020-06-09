---
layout: post
title: "Por un día entero bloquearon YouTube en CANTV"
small: "Por un día entero bloquearon YouTube"
excerpt: "CANTV, el principal proveedor de internet de Venezuela, bloqueó por todo un día el acceso a youtube.com. Este bloqueo aplicó Filtrado SNI, por lo que no afectó a otros servicios de google. Bloqueos previos a YouTube habían sido más cortos."
permalink: /noticias/bloqueo_youtube_un_dia/
date:   2019-03-07 15:00:00 -0400
categories: alerta
image: /res/post_img/2019-03-07-post.png
lang: es
---


VE sin Filtro **ha podido documentar que YouTube estuvo bloqueado por
todo un día en CANTV**, el principal proveedor de internet de Venezuela
y una empresa estatal. Este bloqueo fue inicialmente [reportado por
VEsinFiltro ayer 6 de
marzo](https://twitter.com/vesinfiltro/status/1103424906342080512)
y el bloqueo duró hasta inicios de la tarde del 7 de marzo, cumpliendose
aproximadamente 24 horas del bloqueo de la plataforma de videos más
importante en internet y el sitio más visitado por los venezolanos luego
de google.com.

Desde el [6 de marzo de
2019](https://explorer.ooni.io/measurement/20190306T193453Z_AS8048_jmYnrsmmhaJP8SKiMDvhORIe99M74ucNTn5zmUxCdv31pVd1W0?input=https:%2F%2Fwww.youtube.com%2F)
entre las 10am y 4pm (hora de Venezuela) se pudo evidenciar este bloqueo
a YouTube en CANTV utilizando Filtrado por SNI. **\"Este bloqueo de YouTube
es distinto a los bloqueos cortos que hemos visto desde febrero, los
censores parecen apuntar a bloqueos más extensos de plataformas claves\"**
expresó Andrés Azpúrua, Director de VE sin Filtro y la organización VE
inteligente. \"Los venezolanos tenemos que prepararnos para una censura
cada vez más fuerte en internet\" --agregó.

Este bloqueo coincicidó con la presencia de Juan Gauidó a una misa de
miércoles de ceniza en la iglesia San Pedro de Caracas. Este evento esta
siendo cubierto por medios de streaming por internet.

Desde el 22 de febrero VE sin Filtro, ha documentado y recabado
evidencias técnicas de los múltiples bloqueos más cortos de YouTube,
generalmente durante declaraciones públicas del Presidente Encargado
Juan Guaidó (disputado), ruedas de prensa del Grupo de Lima y eventos
como el concierto [Venezuela Aid
Live](http://venezuelaaidlive.com). Los bloqueos frecuentes
y breves de YouTube también han sido identificados de forma
independiente por la organización Netblocks. VE sin Filtro también ha
documentado y reportado bloqueos indefinidos [a medios de noticias por
streaming como VivoPlay,
VPItv](https://twitter.com/vesinfiltro/status/1099073994496622593),
entre otros.

Este bloqueo es distinto:
-------------------------

Los anteriores bloqueos a YouTube habían sido altamente tácticos,
durando sólo hasta el fin del evento, \"antes parecían balancear el
deseo de limitar el acceso a noticias por streaming con el impacto de
bloquear todo YouTube y otros servicios de Google, ahora están
dispuestos a dejar YouTube bloqueado\" afirmó Andrés Azpúrua. Esto ocurre en un
contexto donde el sitio de muchos medios de comunicación nacionales e
internacionales que ofrecen streaming están bloqueados y la TV abierta y
por suscripción altamente censurada.

**Este bloqueo es distinto porque duró un día entero y al usar una técnica
distinta no afectó de forma colateral otros servicios de Google**, bajando
el impacto no intencional del bloqueo y cambiando la ecuación
costo-beneficio de un bloqueo más prolongado de Google. Esto pudo ser
una prueba para próximos bloqueos de Youtube aún más prolongados o
indefinidos.

La mayoría de los bloqueos de YouTube en Febrero fueron mediante
bloqueos TCP a una lista de direcciones IP, que al bloquearlas impedían
el acceso a YouTube.com pero también a otros servicios de Google como
Google Drive, Calendar, Meet y Chat, creando un costo adicional en el
bloqueo y presión para no mantenerlo innecesariamente.

El nuevo bloqueo implementa **Filtrado por SNI**, una técnica que impide
el establecimiento de la conexión segura con el servidor. Esta técnica
es utilizada en el bloqueos activos como el caso de
[Vivoplay](https://twitter.com/vesinfiltro/status/1100757785992708097)
de
[SoundCloud](https://twitter.com/vesinfiltro/status/1100757785992708097)
reportado el 27 de Febrero, y fue utilizada previamente [contra
Wikipedia](http://vesinfiltro.com/noticias/wikipedia_2019-01/)
en enero de 2019.

![Cover image](/res/post_img/2019-03-07-post.png)


### Detalles técnicos

Se recopilaron [numerosas pruebas
automatizadas](https://api.ooni.io/api/v1/measurements?probe_cc=VE&input=youtube.com&since=2019-03-06&until=2019-03-08&limit=100),
pruebas realizadas por voluntarios a través de la aplicación
[OONI](http://ooni.torproject.org) y pruebas manuales
específicas para determinar el tipo de bloqueo.

Permanece desde hace días días un aparente bloqueo TCP a la ip
172.217.8.78, la cual es accesible por UDP. Esta dirección IP es una de
las múltiples IPs a las que resuelve
[www.youtube.com](http://www.youtube.com), por lo cual hay
una probabilidad menor a 10% de que un usuario experimente bloqueo de
youtube en cualquier momento dado. Esto puede podría ser la primera
prueba de un bloqueo más extenso, un error: dejando bloqueada una
dirección IP al remover un bloqueo más breve de youtube o un bloqueo mal
configurado.

VEsinFiltro recopiló captura de paquetes de múltiples pruebas para
comprobar el funcionamiento del bloqueo por Filtrado SNI. Ejemplo de la
evidencia del comportamiento de Filtrado por SNI:

```
$ curl -v --connect-to ::www.wikipedia.org: https://www.youtube.com
* Rebuilt URL to: https://www.youtube.com/
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
* LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.youtube.com:443
* stopped the pause stream!
* Closing connection 0
curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.youtube.com:443
```
```
$ curl -v --connect-to ::www.youtube.com: https://www.kernel.org
* Rebuilt URL to: https://www.kernel.org/
* Connecting to hostname: www.youtube.com
*   Trying 172.217.8.78...
* TCP_NODELAY set
* Connection failed
* connect to 172.217.8.78 port 443 failed: Operation timed out
*   Trying 172.217.2.206...
* TCP_NODELAY set
* Connected to www.youtube.com (172.217.2.206) port 443 (#0)
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
* SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
* ALPN, server accepted to use h2
* Server certificate:
*  subject: C=US; ST=California; L=Mountain View; O=Google LLC; CN=*.google.com
*  start date: Mar  1 09:45:25 2019 GMT
*  expire date: May 24 09:25:00 2019 GMT
*  subjectAltName does not match www.kernel.org
* SSL: no alternative certificate subject name matches target host name 'www.kernel.org'
* stopped the pause stream!
* Closing connection 0
* TLSv1.2 (OUT), TLS alert, Client hello (1):
curl: (51) SSL: no alternative certificate subject name matches target host name 'www.kernel.org'
```

Recomendaciones:
----------------

Recomendamos el uso de herramientas confiables de circunvención de
bloqueos en internet. Recomendamos tener instaladas varias de las
siguientes herramientas ante la posibilidad de que alguna sea bloqueada.

-   Psiphon [https://psiphon.ca](https://psiphon.ca)

-   Lantern
    > [https://getlantern.org](https://getlantern.org)

-   Tor Browser
    > [https://torproject.org](https://torproject.org)
