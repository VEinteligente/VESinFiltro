---
layout: post
title:  Twitter, Youtube e Instagram bloqueados por CANTV en la mañana del 21 de enero
small:  CANTV bloquea Twitter, Youtube e Instagram el 21 de Enero
excerpt: Documentamos cómo Twitter, Youtube e Instagram fueron bloqueados por el ISP del estado Venezolano, CANTV. El bloqueo comenzó en la madrugada del 21 de Enero y duró hasta las 9:50am (GMT-4)
permalink: /noticias/twitter_youtube_instagram_2019-01/
date:   2019-01-21 14:30:00 -0400
categories: alerta
image: /res/post_img/2019-01-21-RRSS.png
author: "Andrés Azpúrua"
lang: es
---

El lunes 21 de enero fue documentado cómo Twitter, Youtube e Instagram fueron bloqueados por el ISP del estado Venezolano, CANTV. El bloqueo comenzó en la madrugada y duró hasta las 9:50am (GMT-4). Fue documentado con numerosas mediciones ad-hoc y mediciones  realizadas con [OONI Probe](http://ooni.torproject.org) sistemáticamente en sondas dedicadas para este propósito y corriendo en dispositivos móviles gracias a la colaboración de usuarios de internet que participaron en la recolección de datos.


El bloqueo parece estar motivado por la circulación enredes sociales de videos de un grupo de miembros de la Guardia Nacional Bolivariana donde [declaran su oposición al Gobierno de Venezuela](http://elestimulo.com/blog/detienen-a-grupo-insurgente-de-gnb-en-comandancia-de-cotiza/) liderado por Nicolás Maduro en la madrugada del 21 de Enero de 2019. “Estamos en contra de este régimen. Pueblo de Venezuela estamos con ustedes” dijo uno de los integrantes en el video.

El bloqueo funciona mediante filtrado de _Server Name Indication_ (SNI), impidiendo el handshake TLS; sin embargo el bloqueo no parecía cubrir el 100% del tráfico de CANTV, ocasionalmente el handshake TLS sí lograba efectuarse. Este comportamiento es similar al bloqueo de [Wikipedia del 12 al 18 de Enero](http://vesinfiltro.com/noticias/wikipedia_2019-01/) por CANTV y al bloqueo de algunos medios de comunicación como El Nacional en 2018. También comparte el patrón de funcionamiento inconsistente con el [bloqueo de Tor en 2018](https://vesinfiltro.com/noticias/CANTV_bloquea_Tor_2017-06-26/) analizado por VEsinFiltro junto a OONI en un [reporte publicado el mismo año](https://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/). VEsinFiltro posee evidencias técnicas de distintos tipos que soportan el caso de bloqueo, además de las [incontables testimonios en Redes Sociales](https://twitter.com/search?q=bloqueado%20cantv&src=typd).

CANTV es por un muy amplio margen el principal proveedor de internet residencial del país. Cualquier bloqueo por CANTV puede ser  una gravísima limitación al ejercicio de los derechos de los venezolanos y las venezolanas.

Ante el agravamiento de la crisis política venezolana, podemos esperar mayor cantidad de bloqueos esta sem

Detalles del funcionamiento y diagnóstico de este caso son iguales a los del bloqueo de [Wikipedia del 12 al 18 de Enero](http://vesinfiltro.com/noticias/wikipedia_2019-01/). *Este artículo será actualizado con cualquier nueva información relacionada*

![Cover image](/res/post_img/2019-01-21-RRSS.png)
