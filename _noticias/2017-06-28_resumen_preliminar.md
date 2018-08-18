---
layout: post
title: Resumen preliminar del incidente de bloqueo del 28 de junio de 2017
small: Resumen preliminar de bloqueos del 28 de junio de 2017
excerpt: En horas de la noche del 28 de junio de 2017, aproximadamente a las 23h, detectamos nuevos bloqueos a las principales sociales, el extraño incidente solo duró una hora y se desconocen los motivos, seguimos investigando
permalink: /noticias/resumen_preliminar_2017-06-28/
date:   2017-06-28 01:22:00 -0400
categories: bloqueos
image: no

---

29 de junio de 2017, 1:22 am

En horas de la noche del 28 de junio de 2017, aproximadamente a las 23h, detectamos nuevos bloqueos a redes sociales en Venezuela. Los servidores DNS de *CANTV*, el proveedor de servicio de internet del estado, no responden las solicitudes  DNS sobre *Facebook, Twitter, YouTube, Instagram* y *Periscope*, impidiendo el acceso a los usuarios. Alrededor de una hora después, dichos bloqueos fueron liberados y el acceso a esos sitios volvió a ser libre. Innumerables reportes de usuarios en las redes se suman a mediciones específicas de los servidores DNS del ISP.

No pudimos observar dificultades para resolver otros dominios en este período de tiempo, los servidores DNS de CANTV respondían de forma válida y no emitieron timeouts mientras no devolvían la resolución correcta para los dominios de estas plataformas sociales. Las respuestas "vacías" fueron recibidas en tiempos nominales. Este comportamiento refleja filtrado de DNS de los dominios. 

Como en situaciones anteriores, instrucciones de cómo evadir la censura se esparcieron con velocidad por whatsapp y redes sociales. Para la 1am los trending topics para Venezuela incluyen: "ABA CANTV" (nombre del servicio DSL de CANTV), "Facebook y Youtube" con 7,840 Tweets y "DNS de Google".

Se desconoce el motivo del incidente pero es importante monitorear la situación ante la posibilidad de futuros bloqueos futuros en un contexto político cada vez más álgido. Recientemente Venezuela Inteligente verificó que el 7 de Abril entre las 6 y 10am se comenzaron a bloquear los sitios de tres medios de TV y noticias por streaming: vivoplay.net, elcapitolio.tv y vpitv.com sumándose a una larga lista de dominios bloqueados en Venezuela.

En el pasado se ha observado el patrón de que luego de que CANTV bloquee un sitio web, siguen los demás proveedores. Volvimos a observar este patrón con el proveedor Movistar que comenzó a bloquear Twitter brevemente. Pedimos a la comunidad que estén atentos a futuras restricciones en internet y estén preparados con medidas para evadirlos o mitigarlos.

Seguimos analizando datos de los principales proveedores de internet y en varias regiones del país, la ventana de tiempo para documentar el extraño incidente fue corta. 

Actualizamos todo lo que confirmamos sobre la problemas en la red en Venezuela lo compartimos casi en tiempo real a través de [@VeSinFiltro](http://twitter.com/vesinfiltro)


## Cómo evitar este bloqueo y otros similares

Afortunadamente los bloquos típicos en Venezuela se pueden evadir de varias formas, la manera más sencilla es *cambiando a qué servidor DNS* tu computadora preguntará la dirección IP (el que funciona similar al teléfono de información), cambiándolo por uno de confianza que no te esté bloqueando tu proveedor de internet podrás evadir este tipo de bloqueo.
Puedes utilizar [esta guía](http://vesinfiltro.com/bloqueos/dns/) para saber cómo realizar el cambio:
[vesinfiltro.com/bloqueos/dns/](http://vesinfiltro.com/bloqueos/dns/)

Otras formas de evadir bloqueo son el uso de *VPN*, que es como un túnel especial en internet por el cual pasa todo tu tráfico y sale en otro lugar, a partir del cual viajará normalmente. Bien usados, pueden aumentar tu privacidad también, pero si usas un VPN malicioso podrán vigilar casi todo lo que hagas en internet.

En VE Inteligente recomiendamos:
- [Psiphon](https://psiphon.ca)
- [Lantern](https://getlantern.org)
- [Tunnel Bear](https://www.tunnelbear.com)

