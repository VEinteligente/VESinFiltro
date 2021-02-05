---
layout: post
title: "Ataque de phishing dirigido a usuarios de Instagram "
small:   "Ataque de phishing dirigido a usuarios de Instagram "
excerpt: "Una red de dominios maliciosos se dirige a los usuarios de Instagram en una campaña de phishing"
permalink: /noticias/2021-02-04/
date:   2021-02-03 23:10:00 -0400
categories: phishing
image:
---

Después de proveerle asistencia a una de las víctimas, en VESinFiltro hemos identificado una red de dominios usada para el robo de credenciales de Instagram.

La persona o grupo llevando a cabo esta campaña no parecen tener intereses políticos y sólo buscan conseguir ganancias gracias a las cuentas vulneradas.

# Modus Operandi

1.  Los atacantes envían mensajes directos a través de Instagram a cuentas que consideran valiosas, haciéndose pasar por el soporte oficial de la red social.
    
2. Ofrecen la posibilidad de verificar la cuenta (marca de verificación azul) después de completar un formulario online.

3. Para comenzar el formulario solicita un usuario de Instagram y su contraseña, junto con un número telefónico y demás detalles. Éste se encuentra alojado online bajo un dominio diseñado para parecer oficial, imitando el branding y apariencia de la marca.
    
4.  Los atacantes toman control de la cuenta al cambiar la contraseña, el email de recuperación y, en algunos casos, el nombre de la cuenta.
    
5.  Los atacantes contactan a la víctima a través de los datos suministrados y exigen un pago para regresar la cuenta.

Otra posibilidad implica que, dependiendo del criterio de los atacantes, algunas cuentas se vendan en lugar de exigir un rescate. Nuestra evaluación descubrió que también engañan a otros usuarios con mensajes falsos relacionados a demandas por derechos de autor.

# Dominios e IPs usados
La URL recibida fue alojada en la IP **35.225.60.105** junto con muchos otros domains de phishing, y luego se movió a la IP **34.76.11.139**. Los dominios de phishing se pueden clasificar en dos categorías: reclamos falsos sobre derechos de autor y verificación de Instagram falsa (marca de verificación azul). Los otros dominios que se alojaron en el servidor están inactivos, no muestran ninguna información o aparentemente son irrelevantes para los sitios web de phishing.

Lista de dominios alojados en IP 35.225.60.105:

| Dominio                      |               Estatus           |
|-----------------------------------------|--------------------------|
| lnstagramhelpbusinessverified.com       | Activo                   |
| pandesmidestek.com                      | Activo en parking de dominios |
| lnstagramverify-tick.com                | Activo                   |
| pandemimdestek.com                      | Activo en parking de dominios |
| sosyalyardimm.com                       | Inactivo                 |
| copyrightaccounthelp.com                | Inactivo                 |
| copyrightaccounthelp.com                | Inactivo                 |
| lnstagram-copyrights-helpcenter.com     | Inactivo                 |
| ig-copyrightbusiness.com                | Inactivo                 |
| lnstagram-verifiedaccount.com           | Inactivo                 |
| helpbluetick.net                        | Inactivo                 |
| helpaccountcopyright.com                | Inactivo                 |
| servicecopyrighthelp.com                | Inactivo                 |
| destekpandemis.com                      | Inactivo                 |
| 105.60.225.35.bc.googleusercontent.com  | Inactivo                 |
| lnstagram-helpscopyright-team.com       | Inactivo                 |
| lnstagram-copyright-helpscenter.com     | Inactivo                 |
| lnstagram-accountverify.com             | Inactivo                 |
| cranky-perlman.35-225-60-105.plesk.page | Inactivo                 |
| lnstagram-verify-tick.com               | Inactivo                 |
| lnstagramverify-support.com             | Inactivo                 |
| lnstagram-accountverification.com       | Inactivo                 |
| lnstagramverifysupport.com              | Inactivo                 |
| lnstagram-verifyform.com                | Inactivo                 |
| ig-verifiedbadgesform.gq                | Inactivo                 |
| lnstagramserviceverify.com              | Inactivo                 |
| lnstagramverifyservice.com              | Inactivo                 |
| lnstagramverifybusiness.com             | Inactivo                 |
| ig-bluetick.com                         | Inactivo                 |
| lnstagramcontactverified.com            | Inactivo                 |
| ig-verifiedform.gq                      | Inactivo                 |

Los dos dominios activos relacionados a un esquema engañoso de verificación de cuentas de Instagram son lnstagramverify-tick.com e lnstagramhelpbusinessverified.com. Estos dos sitios web son idénticos y su código HTML es el mismo. **Tenga en cuenta el uso de una L en lugar de una i en los nombres de dominio, ya que se ve como una i mayúscula**.

Aunque hay muchos otros dominios cuyos nombres indican intenciones maliciosas, todos ellos ya eran inaccesibles cuando se inició esta investigación. También hay dos dominios, pandesmidestek.com y pandemimdestek.com, a los que se puede acceder pero no se observa ningún contenido en sus sitios web. Es importante tener en cuenta que estos dominios también están relacionados con el idioma turco, ya que las palabras *"pandemi destek"* se pueden traducir como "apoyo pandémico".

Algunos dominios, pero no todos, ya habían sido identificados como páginas de phishing, lo que llevó a los atacantes a migrar algunos dominios que aún están activos a la IP **34.76.11.139**. Ambas direcciones IP mencionadas pertenecen a los servicios en la nube de Google.

 Lista de dominios alojados en IP 34.76.11.139:

| Dominio      | Estatus   |
|----------------------------------------------------------|----------|
| lnstagramhelpbusinessverified.com                        | Activo   |
| copyrightaccountbusinesshelp.com                         | Activo   |
| lnstagramverify-tick.com                                 | Activo   |
| servicehelpcopyright.com                                 | Activo   |
| cranky-murdock.34-76-11-139.plesk.page                   | Activo   |
| freska-api-elasticsearch02.freska-staging.aivencloud.com | Activo   |
| 34-76-11-139.plesk.page                                  | Inactivo |
| 39.11.76.34.bc.googleusercontent.com                     | Inactivo |

<img src="/res/post_img/2021-02-03/img_0.png" width="250" height="460"/> <img src="/res/post_img/2021-02-03/img_1.png" width="250" height="460"/>

WaybackMachine snapshots:
[/web/20210121175308/https://lnstagramhelpbusinessverified.com/](https://web.archive.org/web/20210121175308/https://lnstagramhelpbusinessverified.com/)

[web/20210121180220/https://lnstagramhelpbusinessverified.com/form/](https://web.archive.org/web/20210121180220/https://lnstagramhelpbusinessverified.com/form/)

**Las URL de las páginas de phishing no son la raíz de sus dominios, sino que se encuentran en el subdominio /form**, como lnstagramverify-tick.com **/form** y lnstagramhelpbusinessverified.com **/form** . El sitio muestra un formulario en el que se le pide a la víctima que introduzca su usuario de Instagram y su contraseña. Si la persona objeto de la campaña de phishing completa esta información y la envía, los atacantes la recibirán y luego intentarán robar la cuenta.

El otro modelo de phishing se ejecuta engañando a la víctima haciéndole creer que recibió una advertencia por violación de derechos de autor en su cuenta de Instagram. El sitio web relacionado con esto es servicehelpcopyright.com y al igual que el caso anterior también tiene un formulario en el que se supone que la víctima debe completar su información privada.

<img src="/res/post_img/2021-02-03/img_2.png" width="250" height="460"/> <img src="/res/post_img/2021-02-03/img_3.png" width="250" height="460"/> <img src="/res/post_img/2021-02-03/img_4.png" width="250" height="460"/>

WaybackMachine snapshots:
[http://web.archive.org/web/20210202035043/https://servicehelpcopyright.com/](http://web.archive.org/web/20210202035043/https://servicehelpcopyright.com/)

[http://web.archive.org/web/20210130233853/https://servicehelpcopyright.com/form/](http://web.archive.org/web/20210130233853/https://servicehelpcopyright.com/form/)

No solamente se solicita el usuario y la contraseña de Instagram, sino también un correo electrónico y su contraseña. Vale la pena mencionar que los que realizan el ataque piden que *"no se active la autenticación de dos factores en los dos días después de la confirmación de la cuenta"* en un intento de disuadir a la víctima de usar 2FA.

Como se puede ver en las capturas de pantalla, las páginas web comparten la misma estructura y algunas características. El URL base parece el que se usaría para propósitos de prueba y contiene texto escrito en turco. Por ejemplo, al lado de la palabra "*deneme*" en el centro de la pantalla está un botón que lleva a una dirección de correo llamada denemedene@gmail.com, lo cual puede ser traducido como "prueba" o "experimento".

Mientras investigamos sobre este caso encontramos la posible fuente de este código en un foro de hackers turcos. La descripción de los documentos PHP y los comentarios de los usuarios coinciden con las páginas de phishing encontradas, así como un usuario en dicho foro también coincide un comentario de atribución encontrado en el código HTML.

# Recomendaciones
Para los usuarios que quieren visitar cualquier página con información sensible, recomendamos tomar estas medidas de seguridad básicas:

1.  Obtén la dirección de la página web usando fuentes confiables. En este caso: directamente desde la app de Instagram o su página web oficial.
    
2.  Usa un VPN de confianza si hay alguna razón para creer que el tráfico puede ser monitoreado o manipulado.
    
3.  Asegúrate que la dirección empiece con HTTPS.
    
4.  Si tu buscador te da una advertencia de seguridad, sospecha y desiste de acceder a la página.
    
5.  Si una dirección no encaja exactamente con el dominio que tú conoces, considera que el sitio es falso y evita cualquier otra interacción: mipaginaweb.com, mippaginaweb.com y mipaginaweb.net pueden estar controladas por personal completamente distintas.

