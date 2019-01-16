---
layout: post
title:  Wikipedia bloqueada en CANTV del 12 al 14 de Enero.
small: El sitio web de todas las ediciones de Wikipedia fue bloqueado por CANTV, el proveedor de internet del estado Venezolano, del 12 al 14 de Enero de 2019
permalink: /noticias/wikipedia_2019-01/
date:   2019-01-15 6:30:00 -0400
categories: bloqueos
image: /res/post_img/2019-01-15-wikipedia.png
author: "Andrés Azpúrua (Venezuela Inteligente / VEsinFiltro)"
---


Desde la mañana del sábado 12 de Enero de 2018 hasta la mañana del lunes 14 de Enero los usuarios de CANTV tuvieron dificultades para acceder Wikipedia, la enciclopedia libre, en todas sus ediciones por un bloqueo intencional con aparentes motivos políticos.

El bloqueo ocurrió luego de ediciones a varios artículos de wikipedia haciendo referencia a Juan Guaidó y la presidencia de la República Bolivariana de Venezuela. El artículo de Juan Guaidó, Presidente de la Asamblea Nacional (parlamento) llegó a nombrarlo Presidente de la República, entre otros cambios controversiales. Imágenes de su artículo se volvieron virales en Venezuela y la guerra de ediciones fue cubierta por la prensa nacional.

Análisis técnicos de VEsinFiltro, con colaboración de OONI e independientemente de NetBlocks comprobaron la existencia del bloqueo.

Nuestro análisis coloca a este bloqueo en la categoría de bloqueo HTTP y específicamente funcionó bloqueando el tráfico para establecer una conexión segura (TLS), filtrando según el SNI (Server Name Indication). Al impedir con alta frecuencia que se establezca la conexión segura con el servidor, se impedía la navegación a Wikipedia. 

Similar a otros bloqueos en 2018, el bloqueo no fue uniformemente efectivo, con una tasa de conexiones bloqueadas que varió durante la vida del mismo. El bloqueo sólo fue detectable en CANTV, el proveedor de internet estatal que además maneja la gan mayoría de las conexiones residenciales a internet.

![Cover image](/res/post_img/2019-01-15-wikipedia.png)
