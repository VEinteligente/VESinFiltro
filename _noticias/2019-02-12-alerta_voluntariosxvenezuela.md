---
layout: post
title:  "ALERTA: CANTV impulsa phishing contra plataforma de voluntariado, poniendo en riesgo a disidentes y opositores."
small:  "VALERTA: CANTV impulsa phishing contra plataforma de voluntarios"
excerpt: Hemos identificado y seguimos analizando un grave caso de phishing impulsado, al menos en parte, por el ISP estatal de Venezuela CANTV
permalink: /noticias/alerta-phishing_voluntariado/
date:   2019-02-12 17:20:00 -0400
categories: bloqueos
image: /res/post_img/2019-02-12-alerta.png
author: "Andrés Azpúrua"
---

Hemos identificado y seguimos analizando un grave caso de phishing impulsado, al menos en parte, por el ISP estatal de Venezuela CANTV. **Todo el tráfico a [https://voluntariosxvenezuela.com](http://web.archive.org/web/20190211200329/https://www.voluntariosxvenezuela.com/), un portal asociado a la oposición venezolana para el registro de voluntarios en la distribución de ayuda humanitaria, es redirigido a otro servidor completamente distinto.**

Esta campaña de phishing utiliza un sitio web virtualmente idéntico al original para captar los datos de voluntarios y es impulsada por técnicas sofisticadas de interceptación y _spoofing_ DNS en la red de CANTV/Movilnet.

En CANTV **todo el tráfico DNS está siendo inspeccionado y cualquier solicitud por el IP de voluntariosxvenezuela.com es interceptada y el equipo recibe una respuesta forjada (159.65.65.194, la dirección IP del servidor que hospeda el sitio malicioso)**, esto incluye tráfico a servidores DNS externos a CANTV, como 8.8.8.8 de google y 1.1.1.1 de Cloudflare, así como a servidores DNS inexistentes.

El servidor en 159.65.65.194 está hospedado en Digital Ocean y responde al dominio [voluntariovenezuela.com](http://web.archive.org/web/*/voluntariovenezuela.com) (sin la s y sin x) además de voluntariosxvenezuela.com. Tiene un certificado SSL para el dominio falso con el que intentan confundir.

Cuando el usuario de CANTV intenta navegar al dominio real en na conexión insegura (HTTP) el servidor malicioso redirije a www.voluntariovenezuela.com y no hay otro indicio de que haya ocurrido algo malo. Si accede mediante una conexión HTTPS el navegador mostrará una alerta indicado la inconsistencia entre el dominio navegado y el del certificado.

Este caso es sumamente grave por la historia de persecución a activistas, manifestantes y opositores en Venezuela; particularmente el uso de listas de ciudadanos usadas para discriminar en contra de opositores al gobierno.

Desde tempranas horas de la tarde [hemos estado alertando](https://twitter.com/andresAzp/status/1095420751979708417) a los usuarios para que tengan cuidado y no otorguen su información privada en el sitio falso colocado para engañarlos.

VE sin Filtro publicará mañana un informe más completo de estos hallazgos.

## Actualización 2019-02-13

En horas de la mañana la DNS injection de #CANTV fue levantado y el sitio malicioso fuera de línea, pero podría ser temporal.


## Recomendaciones

Es sumamente importante reconocer el URL (dirección) del sitio que uno esta visitando y asegurarse que haya una conexión segura (HTTPS://) sin errores o alertas de parte del navegador. Si el navegador dice que no es segura, desconfía inmediatamente del sitio.

Los administradores de sitios similares deben asegurarse de colocar certificados SSL, redigirir el traffico http a https y sólo compartir URLS https de sus sitios en comunicaciones oficiales, y usar DNSsec; para minimizar las probabilidades de éxito phishing (engaños dirigidos) a sus usuarios.

Para acceder sitios bloqueados o inaccesibles en Venezuela tenemos [estas recomendaciones generales](https://twitter.com/vesinfiltro/status/1088156683317231621)


![Cover image](/res/post_img/2019-02-12-alerta_share.png)

![SSL error](/res/post_img/2019-02-12-alerta-capture.png)
