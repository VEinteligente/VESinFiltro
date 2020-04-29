---
layout: post
title:  "Preliminar report: State sponsored phishing against healthcare workers amid COVID-19 pandemic in Venezuela"
small:  "State sponsored phishing against healthcare in Venezuela"
excerpt: "Healthcare workers who wanted to register to recieve finanal aid are targeted by state-sponsored phishing by Venezuela's Maduro Government"
permalink: /noticias/2020-04-26-phishing_healthcare_heroes
date:   2020-04-27 6:23:00 -0400
categories: bloqueos
image: /res/post_img/2020-04-26_es.png
---

*This preliminary report was [originally published on 2020-04-27 in spanish](http://vesinfiltro.com/noticias/2020-04-26-phishing_heroes_salud)*
Updated: 2020-04-28

On Sunday, March 26 2020, VE Sin Filtro identified a new phishing campaign against the users of a registration platform for healthcre workers linked to his political opposition.

**The “Héroes de la Salud” platform was created by Juan Guaido’s disputed interim administration to provide monthly financial assistance to healthcare workers in Venezuela, who are facing difficult working conditions and low wages in the public sector.**

![comparison](/res/post_img/2020-04-26/comp.png)

CANTV, Venezuela's largest ISP and a state-owned company under the control of Nicolas Maduro, was **tricking their users with malicious DNS responses for heroesdesaludve.info,*[update]* and the alternative domain saludvzla.com**, sending most of the users who wanted to visit the site to a fake one to capture their data. It's possible that this malicious site also received visits from deceived users after clicking on malicious links.

Phishing is an attack in which users are fooled into revealing personal or sensitive information, making them believe they are visiting the genuine site when they really are in a malicious site that looks like the original.

## Powered by CANTV

CANTV participates in this phishing campaign by facilitating the malicious resolution of the IP address for heroesdesaludve.info. A DNS server translates domain names as "domain.com" in an IP direction; that is what the computer uses to find internet servers.

By 19:26 2020-04-26 (VET), at the latest, [CANTV's DNS server began to reply with this false information](). The server redirects the web browser to the domain heroesdesaludve.co, controlled by attackers, with a page almost identical to the original.

[update]* The alternative domain saludvzla.com** was ponting to the same server shortly after being introduced, in the morning of 2020-04-28

This strategy implies that almost every user of CANTV and subsidiary companies attempting to visit heroesdesaludve.info will end up on a malicious site. If the user typed or clicked the URL starting with HTTPS (https://heroesdesaludve.info), they could have seen a warning; however, many Venezuelans users are used to ignore these warnings.

![SSL certificate warning](/res/post_img/2020-04-26/warning_chrome.png)


## The malicious site

The malicious site is designed to mimic the appearance and behavior of the genuine one, based on the original HTML structure. heroesdesaludve.co is served by HTTPS using an SSL certificate, which makes that a lock icon appears at the browser window, giving a false sense of security when it only confirms that the established connection is encrypted. Still, it doesn't give any guarantee that the site is legitimate.

There are small differences between the behavior of the malicious registration form and the original to maximize data collection. After registering on the site, the victim is received with the same confirmation message on both sites.

The registration form requests for highly sensitive information that includes ID number, residence address, e-mail, work address, and position, as well as images of official documents.

![formulario](/res/post_img/2020-04-26/form.png)


At least one of the participants in the malicious site left a comment in the structure of the page. VE sin filtro has decided not to give visibility to the pseudonyms of these actors.

PARALLEL BLOCKS

While this campaign has been active, we have documented multiple blocks to this platform and other related domains in public and private internet providers.

This includes:
* coronavirusvenezuela.info
* apoyosaludve.com
* heroesdesaludve.org
* heroesdesaludve.

![Table con multiples dominios bloqueados por ISP](/res/post_img/2020-04-26/blocks_table.png)



## Repeating the play

This phishing campaign has many similarities with Maduro's government [2019 phishing campaign against "Voluntarios por Venezuela" (Volunteers for Venezuela)](https://vesinfiltro.com/noticias/Phishing_impulsado_por_gobierno_de_Venezuela/), in which they also abused the DNS system to deceive users, in this case activists, to register at a malicious clone of the official site voluntariosxvenezuela.com.

In that case, it was possible to prove the participation of CONATEL and CANTV, and the data collected, as well as the confusion of the attack itself, were used to generate doubts using fake news and exposed the sensitive data of the people registered at the website.


## Recomendations for users

For the users who want to visit this site or any other with sensitive information, we recommend taking these basic security measures:
1. Get the link or address using trusted sources. In this case: directly from the official Whatsapp or Facebook bots.
2. Use a trusted VPN if there are any reasons to believe that the traffic could be monitored or manipulated, this applies to this case.
3. Make sure that the link begins with HTTPS.
4. Be suspicious and desist from using a website if the browser gives you a security warning.
5. If the website address doesn't match exactly with the domain that you know, consider the site as a false one and avoid any other type of interaction. misitioweb.co, missitiosweb.com y missitioweb.net can be controlled by completely different people.

NEXT STEPS

A more detailed technical report is on development.


El domingo 26 de Marzo VE sin filtro identificó una nueva campaña de phishing del gobierno de Nicolás Maduro en contra de una plataforma de registro de médicos vinculada con su oposición política.

La plataforma **Héroes de la Salud fue creada por la gestión de Juan Guaidó para proveer una asistencia económica mensual al personal de salud en Venezuela en el marco de la pandemia de Covid-19**, ante las difíciles condiciones de trabajo y bajos sueldos en el sector público.

![comparación](/res/post_img/2020-04-26/comp.png)

Los usuarios del proveedor CANTV llegaron al sitio malicioso gracias a la manipulación de los servidores DNS de esta empresa del estado, que es el principal proveedor de internet en Venezuela. Es posible que este sitio malicioso también haya recibido visitas de usuarios engañados al hacer click en links engañosos

Phishing es un ataque informático en el que se engaña a los usuarios para que revelen información sensible, entre otros métodos, haciéndoles creer que están en una página genuina cuando realmente están en una página falsa que aparenta ser la original.

## Impulsado por CANTV

CANTV participa en esta campaña de phishing facilitando la resolución maliciosa de la dirección IP para *heroesdesaludve.info*. Un servidor DNS traduce nombres de dominio como "dominio.com" en una dirección IP que es lo que la computadora realmente usa para encontrar servidores en internet.

A más tardar a las [7:26 del 2020-04-26 ](preliminar, Hora de Venezuela) el servidor DNS de CANTV comenzó a responder con esta información falsa. El servidor indicado por el DNS de CANTV redirige el navegador al dominio *heroesdesaludve.co*, controlado por los atacantes, con una página casi idéntica a la original.

Esta estrategia implica que casi todos los usuarios de CANTV y empresas filiales que intentan visitar *heroesdesaludve.info* van a terminar en un sitio malicioso. En el caso de haber hecho click o escrito el URL con HTTPS (*https://heroesdesaludve.info*) entonces el usuario hubiese visto una advertencia del navegador, sin embargo, ~~los~~muchos usuarios Venezolanos están acostumbrados a ignorar estas advertencias.

![SSL certificate warning](/res/post_img/2020-04-26/warning_chrome.png)

## El sitio malicioso

El sitio malicioso está diseñado para imitar la apariencia y comportamiento del genuino, basándose en la estructura HTML del original. *heroesdesaludve.co* es servido por HTTPS usando un certificado SSL, lo que hace que la ventana del navegador tenga un ícono de candado, dando una falsa sensación de seguridad, cuando en realidad solo confirma que la conexión se está estableciendo de forma cifrada, mas no da garantías de que sea con el sitio legítimo.

Hay pequeñas diferencias en el comportamiento del formulario de registro malicioso respecto al original para maximizar la obtención de datos: Luego de "registrarse" en el sitio, la víctima es recibida con el mismo mensaje de confirmación en la página web que en el sitio genuino.

El formulario de registro solicita información altamente sensible, incluye el número de cédula de identidad, dirección de residencia, e-mail, dirección de trabajo y cargo, así como imágenes de documentos oficiales.

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

En ese caso se pudo probar la participación de CONATEL y CANTV. Y los datos obtenidos, así como la confusión por el ataque mismo, fueron utilizados para generar dudas y noticias falsas, además de exponer los datos sensibles de los que se registraron en el sitio web.

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
