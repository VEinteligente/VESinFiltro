---
layout: post
title:  "Informe Preliminar: Phishing del gobierno de Maduro contra plataforma Héroes de la Salud"
small:  ""
excerpt: "Personal medico que busca registrarse para recibir ayuda es engañado por gobierno de Maduro. Mientras la página clonada y censurada"
permalink: /noticias/2020-04-26-phishing_heroes_salud"
date:   2020-04-27 6:23:00 -0400
categories: [bloqueos, reporte]
image: /res/post_img/2020-04-26_es.png
lang: es
---

El domingo 26 de Marzo VE sin filtro identificó una nueva campaña de phishing del gobierno de Nicolás Maduro en contra de una plataforma de registro de médicos vinculada con su oposición política.

La plataforma **Héroes de la Salud fue creada por la gestión de Juan Guaidó para proveer una asistencia económica mensual al personal de salud en Venezuela en el marco de la pandemia de Covid-19**, ante las difíciles condiciones de trabajo y bajos sueldos en el sector público.

![comparación](/res/post_img/2020-04-26/comp.png)

Los usuarios del proveedor CANTV llegaron al sitio malicioso gracias a la manipulación de los servidores DNS de esta empresa del estado, que es el principal proveedor de internet en Venezuela. Es posible que este sitio malicioso también haya recibido visitas de usuarios engañados al hacer click en links engañosos

Phishing es un ataque informático en el que se engaña a los usuarios para que revelen información sensible, entre otros métodos, haciéndoles creer que están en una página genuina cuando realmente están en una página falsa que aparenta ser la original.

## Impulsado por CANTV

CANTV participa en esta campaña de phishing facilitando la resolución maliciosa de la dirección IP para *heroesdesaludve.info*. Un servidor DNS traduce nombres de dominio como "dominio.com" en una dirección IP que es lo que la computadora realmente usa para encontrar servidores en internet.

A más tardar a las [7:26 del 2020-04-26 ](https://explorer.ooni.org/measurement/20200426T232636Z_AS8048_HIAA1QxJZaxc2Ux2wPoDzaU7yRrBy8XGDRv7cStOYqAQB19zyb?input=https%3A%2F%2Fheroesdesaludve.info%2F)(preliminar, Hora de Venezuela) el servidor DNS de CANTV comenzó a responder con esta información falsa. El servidor indicado por el DNS de CANTV redirige el navegador al dominio *heroesdesaludve.co*, controlado por los atacantes, con una página casi idéntica a la original.A más tardar a las [7:26 del 2020-04-26 ](https://)(preliminar, Hora de Venezuela) el servidor DNS de CANTV comenzó a responder con esta información falsa. El servidor indicado por el DNS de CANTV redirige el navegador al dominio *heroesdesaludve.co*, controlado por los atacantes, con una página casi idéntica a la original.

Esta estrategia implica que casi todos los usuarios de CANTV y empresas filiales que intentan visitar *heroesdesaludve.info* van a terminar en un sitio malicioso. En el caso de haber hecho click o escrito el URL con HTTPS (*https://heroesdesaludve.info*) entonces el usuario hubiese visto una advertencia del navegador, sin embargo, los usuarios Venezolanos están acostumbrados a ignorar estas advertencias.

![SSL certificate warning](/res/post_img/2020-04-26/warning_chrome.png)

## El sitio malicioso

El sitio malicioso está diseñado para imitar la apariencia y comportamiento del genuino, basándose en la estructura HTML del original. *heroesdesaludve.co* es servido por HTTPS usando un certificado SSL, lo que hace que la ventana del navegador tenga un ícono de candado, dando una falsa sensación de seguridad, cuando en realidad solo confirma que la conexión se está estableciendo de forma cifrada, mas no da garantías de que sea con el sitio legítimo.

Hay pequeñas diferencias en el comportamiento del formulario de registro malicioso respecto al original para maximizar la obtención de datos: Luego de "registrarse" en el sitio, la víctima es recibida con el mismo mensaje de confirmación en la página web que en el sitio genuino.

El formulario de registro información altamente sensible, incluye el número de cédula de identidad, dirección de residencia, e-mail, dirección de trabajo y cargo, así como imágenes de documentos oficiales.

![formulario](/res/post_img/2020-04-26/form.png)

Al menos uno de los involucrados en el sitio falso dejó un mensaje en la estructura de la página, hasta el momento VE sin Filtro decide no darle visibilidad a los seudónimos de estos actores.



## Bloqueos en paralelo

Mientras esta campaña ha estado activa, hemos documentado múltiples bloqueos a esta misma plataforma y a otros dominios relacionados en los proveedores de internet públicos y privados.

Incluyendo:
- coronavirusvenezuela.info
- apoyosaludve.com
- heroesdesaludve.org
- heroesdesaludve.info

![Table con multiples dominios bloqueados por ISP](/res/post_img/2020-04-26/blocks_table.png)

## Repitiendo las jugadas

Esta campaña tiene muchas simulitudes con una campaña del [Gobierno de Maduro contra Voluntarios por Venezuela](https://vesinfiltro.com/noticias/Phishing_impulsado_por_gobierno_de_Venezuela/), donde también se abusó del sistema DNS para engañar a usuarios, en este caso activistas, a registrarse en un clon malicioso del sitio genuino voluntariosxvenezuela.com.

En ese caso se pudo probar la participación de CONATEL y CANTV. Y los datos obtenidos, así como la confusión por el atque mismo, fueron utilizados para generar dudas y noticias falsas, además de exponer los datos sensibles de los que se registraron en el sitio web.

## Recomendaciones para los usuarios

Para usuarios que desen visitar este sitio o cualquier otro con informacion sensible recomendamos tomar en cuenta estas medidas básicas de seguridad.

1. Solo obtener el enlace o dirección usando fuentes de confianza.
 En este caso: Directamente del bot oficial de Whatsapp o Facebook
1. Usar un VPN de confianza si hay razones para creer que el trafico podría ser interferido. Aplica para este caso
1. Asegurarse que el link abierto empiece por HTTPS
1. Desconfiar y desistir de usar un sitio web si el navegador te da una advertencia de seguridad
1. Si la dirección de un sitio web no coincide exactamente con el dominio que conoces considera el sitio como falso y evita cualquier tipo de interacción.
misitioweb.com, missitiosweb.com y  missitioweb.net pueden ser controlados por personas completamente distintas


## Siguientes pasos

Un reporte con más detalles técnicos está en desarrollo


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEzNjE5NDMxNl19
-->
