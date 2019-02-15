---
layout: post
title: Phishing impulsado por el gobierno de Venezuela pone en riesgo a activistas y usuarios de internet.
small: Phishing impulsado por el gobierno de Venezuela pone en riesgo a activistas
excerpt: El sitio web voluntariosxvenezuela.com, asociado a la oposición venezolana para el registro de voluntarios en la distribución de ayuda humanitaria ha sufrido una campaña de phishing impulsada por el gobierno con DNS injection.
permalink: /noticias/Phishing_impulsado_por_gobierno_de_Venezuela/
date:   2019-02-15 12:00:00 -0400
categories: bloqueos
image: /res/post_img/2019-02-15-report.png
author: "Andrés Azpúrua, Carlos Guerra, Jose Luis Rivas"
---

![Cover image](/res/post_img/2019-02-15-report.png)

### Resumen Ejecutivo


El sitio web voluntariosxvenezuela.com, un portal asociado a la
oposición venezolana para el registro de voluntarios en la distribución
de ayuda humanitaria ha sufrido una campaña de phishing impulsada por el
gobierno. El 12 de febrero de 2019 se detectó que el proveedor de
servicio de internet con el mayor número de usuarios, CANTV, controlado por el gobierno de Nicolás
Maduro, hacía una redirección de las visitas a otro servidor con un
sitio web visualmente idéntico, que no es controlado por los
administradores del sitio legítimo voluntariosxvenezuela.com

El 12 de febrero también se realizó una marcha masiva y un comunicado
del presidente encargado, acompañado de una campaña para promover que
las personas se registraran como voluntarios. Se estima que al menos
decenas de miles de personas pudieron haber entregando sus datos a la
página fraudulenta dada la magnitud de la movilización, el alcance de la
campaña y el porcentaje del tráfico de internet que pasa a través de las
redes de CANTV.

A través de pruebas técnicas se pudo verificar que la redirección
sucedía incluso al usar otros servidores DNS distintos a los de CANTV:
activamente se monitoreaba el tráfico y se falsificaban respuestas ante
las solicitudes de los usuarios. La investigación también vinculó
directamente a CONATEL (Instituto regulador de las comunicaciones en
Venezuela) con el registro del dominio falso. También se consiguieron
múltiples dominios adicionales muy similares a dominios de redes
sociales y sitios web populares, que podrían haberse usado o usarse en
un futuro para campañas de phishing para -por ejemplo- capturar
credenciales de cuentas.

Todo estos nuevos desarrollos son muy preocupantes porque apuntan a un
aumento de la sofisticación de los ataques, y además los vinculan
directamente al gobierno disputado de Nicolás Maduro. Aumenta
drásticamente la necesidad de tomar medidas para evitar caer en esta o
campañas similares de phishing, tanto desde el punto de vista de los
usuarios como de los administradores de sitios web.

### Índice


* [Contexto](#contexto)

* [Bloqueo y phishing a
VoluntariosXVenezuela.com](#bloqueo-y-phishing-a-voluntariosxvenezuela.com)

    - [Spoofing DNS e inyección
DNS](#spoofing-envenenamiento-e-inyección-dns)

    - [El sitio malicioso en
159.65.65.194](#el-sitio-malicioso)

    - [Comportamiento visible a
usuarios](#comportamiento-visible-a-usuarios)

    - [Afectación y estatus
actual](#afectación-y-estatus-actual)

* [Otras campañas de Phishing](#otras-campañas-de-phishing)

    - [Propietarios del
servidor](#propietarios-del-servidor-y-dominios)

* [Conclusiones](#conclusiones)

* [Recomendaciones](#recomendaciones)



Contexto
========

Venezuela ha vivido una crisis humanitaria compleja en los últimos años
que ha llevado a millones a emigrar, incluso a pie. [La
ONU] [estima que más de 3 millones han salido del
país](https://www.unhcr.org/news/press/2018/11/5be4192b4/number-refugees-migrants-venezuela-reaches-3-million.html).
A esta situación se le suma en enero de 2019 una [grave crisis de
legitimidad](http://es.wikipedia.org/wiki/Crisis_presidencial_de_Venezuela_de_2019),
al estar en entredicho la legitimidad de Nicolás Maduro como Presidente
luego de proclamarse el Presidente de la Asamblea Nacional, Juan Guaidó,
como Presidente interino de Venezuela.

La crisis de legitimidad ha sido el detonante de una ola de bloqueos en
internet mucho más tácticos usando herramientas como filtrado por SNI.
Esta nueva ola de bloqueos comenzó con el [bloqueo de
Wikipedia](http://vesinfiltro.com/noticias/wikipedia_2019-01/)
cuando reflejó a Juan Guaidó como Presidente de Venezuela, y se ha
enfocado en silenciar los discursos públicos que son transmitidos vía
streaming. [El bloqueo de las plataformas con
streaming](http://vesinfiltro.com/noticias/report-jan-2019/#blocking-of-instagram-twitter-and-youtube)
es de particular importancia en el contexto venezolano, donde se tiene
una [hermética censura en los medios
tradicionales](https://rsf.org/en/venezuela). Hemos
reportado múltiples casos de bloqueos incluyendo el [bloqueo de Tor en
2018](http://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/),
y organismos como Freedom House catalogan el [internet de Venezuela
como no
libre](http://freedomhouse.org/report/freedom-net/2018/venezuela).

Como respuesta a la crisis humanitaria, y en muestra de apoyo al gobierno interino, 
se han organizado centros de acopio para recibir ayuda
humanitaria y prepararla para su envío a Venezuela, con el apoyo de
países como Colombia, Brasil, Chile, Argentina, Costa Rica, Estados
Unidos y los Países Bajos entre otros. La gran mayoría no ha podido
entrar por impedimento del Gobierno de Venezuela. La oposición
venezolana ha organizado un movimiento de voluntarios para ayudar en la
logística y distribución de la ayuda humanitaria, a través del sitio web
[voluntariosxvenezuela.com](https://voluntariosxvenezuela.com/)

Bloqueo y phishing a VoluntariosXVenezuela.com
==============================================

Hemos identificado y analizado una campaña sofisticada de phishing
contra venezolanos que deseen registrarse como voluntarios para la
distribución de ayuda humanitaria, iniciativa asociada directamente a la
oposición venezolana y promovida por Juan Guaidó.

**Este grave caso de phishing fue impulsado, al menos en parte, por el
proveedor de servicio de internet (ISP) estatal de Venezuela, CANTV, y
su filial móvil Movilnet**. Los usuarios de internet en CANTV y Movilnet
que intentaban visitar el portal para el registro de voluntarios
[voluntariosxvenezuela.com](https://voluntariosxvenezuela.com)
fueron dirigidos a un servidor malicioso que responde a
voluntariovenezuela.com.

Esta campaña de phishing utiliza un sitio web virtualmente idéntico al
original para captar los datos de voluntarios que creían estar registrándose
en el sitio genuino, y **pudo obtener grandes cantidades de tráfico por
técnicas sofisticadas de intercepción y spoofing de DNS en la red de
CANTV/Movilnet.**

Es difícil conocer con exactitud el inicio de la campaña de phishing, puesto que es
posible que el sitio malicioso haya sido puesto en uso antes de el
spoofing DNS. Desde tempranas horas de la tarde del 12 de febrero hemos
estado [alertando a los usuarios del
phishing](https://twitter.com/andresAzp/status/1095420751979708417)
para que tengan cuidado y no otorguen su información privada en el sitio
falso colocado para engañarlos, así como proveyendo apoyo a distintos
actores en relación a este incidente.

Existen menciones en Twitter del dominio falso [desde la tarde del 11
de
febrero](https://twitter.com/search?f=tweets&vertical=default&q=voluntariovenezuela.com%20since%3A2019-02-11%20until%3A2019-02-12&src=typd&lang=en)
(hora de Venezuela, GMT-4), con usuarios promoviendo el URL del sitio
malicioso. Destaca [este
tweet](https://twitter.com/Wil_Ardilax1/status/1095071269538721793)
([archivado](https://web.archive.org/web/20190214143056/https:/twitter.com/Wil_Ardilax1/status/1095071269538721793),
[2](https://archive.fo/AGjvI)) del usuario @Wil\_Ardilax1
a las 5:25pm que contiene el URL al sitio malicioso
[https://www.voluntariovenezuela.com/index.html\#como-puedo-ayudar](https://www.voluntariovenezuela.com/index.html#como-puedo-ayudar),
que debió ser copiado y pegado del sitio malicioso. Igualmente, un
[tweet](https://twitter.com/alerodriguez150/status/1095073021939847170)
([archivado](https://web.archive.org/web/20190214143240/https:/twitter.com/alerodriguez150/status/1095073021939847170),
[2](https://archive.fo/E1cPd)) del 11 de Febrero a las
5:32 que pide escribir con cuidado el URL y enlaza al dominio falso, en
respuesta a la cuenta oficial @voluntariosxve.

A partir de las 10:30am (GMT-4) se registra [en
Twitter](https://twitter.com/ZombVE/status/1095329455529091074)
([archivado](https://web.archive.org/web/20190214145414/https:/twitter.com/ZombVE/status/1095329455529091074),
[2](https://archive.fo/YKtC6)) una de las primeras quejas
consistentes en el spoofing DNS del sitio
[voluntariosxvenezuela.com](https://voluntariosxvenezuela.com), y
otras claras
[referencias](https://twitter.com/josraf/status/1095385577946599424)
([archivado](https://web.archive.org/web/20190214145250/https:/twitter.com/josraf/status/1095385577946599424),
[2](https://archive.fo/hfqek)) al incidente aparecen
posteriormente.

Se puede estimar que la campaña de phishing comenzó el 11 de febrero a
las 5:25 pm (GMT-4), y probablemente comenzó a efectuarse spoofing DNS
el 12 de febrero a las 10:30 am. Mediciones realizadas apuntan a que la
campaña de phishing fue levantada entre las 2:30am y 7:30am del 13 de
febrero.

También existe una cuenta en Twitter
[@voluntariosvene](https://web.archive.org/web/20190214175249/https:/twitter.com/voluntariosvene),
similar a la cuenta verificada
[@voluntariosxve](https://twitter.com/voluntariosxve),
que promueve links al sitio de registro con conexiones http no seguras,
que facilitan la caída en esta campaña de phishing sin que ocurran mensajes
de error que induzcan a la sospecha.

El 14 de febrero de 2018 la campaña de phishing fue reactivada
brevemente de 5:00pm a 5:55 aproximadamente, con DNS injection para
llevar el tráfico al sitio web malicioso, en otra dirección IP.

Spoofing, envenenamiento e inyección DNS
----------------------------------------

Los navegadores de internet utilizan servidores DNS (sistema de nombres
de dominio) para traducir el nombre de un sitio web, como dominio.com, a
una dirección IP que se usará para conectarse con el servidor deseado.
El spoofing DNS es una familia de técnicas en las que se entrega al
equipo del usuario una respuesta DNS no genuina, y de esta forma el
equipo no puede contactar al destino deseado o contacta otro distinto.

El 12 de febrero todo el tráfico saliente DNS fue inspeccionado y
cualquier solicitud por el IP asociado a voluntariosxvenezuela.com es
respondida indicando la dirección IP 159.65.65.194, la dirección IP del
servidor que hospeda el sitio malicioso y que claramente no coincide con
el [rango de
IPs](https://securitytrails.com/domain/voluntariosxvenezuela.com/history/a)
de voluntariosxvenezuela.com hospedado en AWS. Adicionalmente, la
respuesta es la misma para las respuestas de los servidores DNS de
CANTV. Se desconoce si este ip fue configurado en los servidores de
CANTV o si su caché (memoria temporal) fue \"envenenado\" el consultar
el servidor autoritativo y ser afectado también el DNS injection.

Hay equipos sofisticados que fueron configurados para inspeccionar la
totalidad o casi totalidad del tráfico y detectar cualquier solicitud
DNS sobre voluntariosxvenezuela.com y hacerse pasar por ese servidor
para dar una respuesta forjada.

La intercepción de las solicitudes DNS para enviar una respuesta forjada
se llama *DNS injection.* El ***DNS injection* puede hacerse a cualquier 
solicitud DNS a cualquier servidor en internet, inclusive a servidores de
confianza.** Pudimos observar esto en servidores externos a CANTV, como
8.8.8.8 de Google y 1.1.1.1 de Cloudflare que deberían dar la respuesta
verdadera, y al hacer solicitudes DNS a servidores DNS inexistentes que
no deberían generar respuesta, en todos los casos se obtuvo la misma
respuesta.

Se corrieron numerosas pruebas para obtener el IP de
voluntariosxvenezuela.com y voluntariovenezuela.com con DNS de CANTV:
200.44.32.12, en todos los casos la respuesta es 159.65.65.194

```

$ dig voluntariosxvenezuela.com @200.44.32.12

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @200.44.32.12
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47904
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 2427 IN A 159.65.65.194
;; Query time: 32 msec
;; SERVER: 200.44.32.12\#53(200.44.32.12)
;; WHEN: Tue Feb 12 17:56:41 -04 2019
;; MSG SIZE rcvd: 70

$ dig voluntariovenezuela.com @200.44.32.12

; <<>> DiG 9.10.6 <<>> voluntariovenezuela.com @200.44.32.12
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33913
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:

;voluntariovenezuela.com. IN A
;; ANSWER SECTION:

voluntariovenezuela.com. 126 IN A 159.65.65.194
;; Query time: 139 msec
;; SERVER: 200.44.32.12\#53(200.44.32.12)
;; WHEN: Tue Feb 12 17:56:53 -04 2019
;; MSG SIZE rcvd: 68

```

Adicionalmente se probó repetidamente cómo la respuesta seguía siendo
inconsistente con el rango de [IPs genuino de
voluntariosxvenezuela.com](https://securitytrails.com/domain/voluntariosxvenezuela.com/history/a)
al hacer solicitudes DNS a servidores distintos a los de CANTV, como
8.8.8.8 de Google, 1.1.1.1 de Cloudfare e IPs donde no hay servidores
DNS. Ejemplo de repetidas pruebas:

```

$ dig voluntariosxvenezuela.com @8.8.8.8

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27141
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 159.65.65.194
;; Query time: 31 msec
;; SERVER: 8.8.8.8\#53(8.8.8.8)
;; WHEN: Tue Feb 12 18:09:33 -04 2019
;; MSG SIZE rcvd: 84

$ dig voluntariosxvenezuela.com @1.1.1.1

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65246
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 159.65.65.194
;; Query time: 96 msec
;; SERVER: 1.1.1.1\#53(1.1.1.1)
;; WHEN: Tue Feb 12 18:09:40 -04 2019
;; MSG SIZE rcvd: 84

```

Lo mismo sucede con IPs donde no hay servidores DNS, como 185.199.108.153. Ejemplo:\
```

$ dig voluntariosxvenezuela.com @185.199.108.153

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com
@185.199.108.153
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65246
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 159.65.65.194\
```

Durante la breve ventana de tiempo en que el Spoofing DNS, incluyendo
inyección DNS, estuvo activo el 14 de febrero, se obtuvieron los mismos
resultados, pero con respuesta 134.209.13.64.

```

dig voluntariosxvenezuela.com @1.1.1.1

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26833
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 134.209.13.64
;; Query time: 178 msec
;; SERVER: 1.1.1.1\#53(1.1.1.1)
;; WHEN: Thu Feb 14 17:11:30 -04 2019
;; MSG SIZE rcvd: 84

$ dig voluntariosxvenezuela.com @8.8.8.8

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 55983
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 134.209.13.64
;; Query time: 32 msec
;; SERVER: 8.8.8.8\#53(8.8.8.8)
;; WHEN: Thu Feb 14 17:11:36 -04 2019
;; MSG SIZE rcvd: 84

$ dig voluntariosxvenezuela.com @200.44.32.12

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com @200.44.32.12
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 55331
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 1009 IN A 134.209.13.64
;; Query time: 57 msec
;; SERVER: 200.44.32.12\#53(200.44.32.12)
;; WHEN: Thu Feb 14 17:11:40 -04 2019
;; MSG SIZE rcvd: 70

$ dig voluntariosxvenezuela.com @185.199.111.153

; <<>> DiG 9.10.6 <<>> voluntariosxvenezuela.com
@185.199.111.153
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57551
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:

;voluntariosxvenezuela.com. IN A
;; ANSWER SECTION:

voluntariosxvenezuela.com. 327680 IN A 134.209.13.64
;; Query time: 34 msec
;; SERVER: 185.199.111.153\#53(185.199.111.153)
;; WHEN: Thu Feb 14 17:12:24 -04 2019
;; MSG SIZE rcvd: 84

```

El sitio malicioso
------------------

El servidor con IP 159.65.65.194 está hospedado en [Digital
Ocean](https://www.shodan.io/host/159.65.65.194), según lo
observado en la configuración [DNS del
dominio](https://securitytrails.com/domain/voluntariovenezuela.com/dns)
([archived](https://web.archive.org/web/20190215022940/https://securitytrails.com/domain/voluntariovenezuela.com/dns))
y responde al dominio voluntariovenezuela.com (sin la s y sin x) además
de voluntariosxvenezuela.com. Tiene un certificado SSL para el dominio
falso voluntariovenezuela.com y no muestra certificados para el dominio
genuino.

El servidor hospeda un clon visualmente idéntico al sitio oficial
VoluntariosXVenezuela.com, clonado a base del código fuente y recursos
como imágenes.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/1.png)

El análisis del código HTML que compone a cada sitio muestra las escasas
diferencias en el código. Pudimos observar que se utilizó
[HTtrack](https://www.httrack.com) para descargar el sitio
web original a través del siguiente comentario en el código:

```

<!\-- Mirrored from www.voluntariosxvenezuela.com/ by HTTrack Website
Copier/3.x \[XR&CO\'2014\], Mon, 11 Feb 2019 13:41:27 GMT \-->

```

Comentario en www.voluntariovenezuela.com

```

<!\-- Mirrored from www.voluntariosxvenezuela.com/descargar-kit/ by
HTTrack Website Copier/3.x \[XR&CO\'2014\], Mon, 11 Feb 2019 13:41:34
GMT \-->

```

Comentario en www.voluntariovenezuela.com/descargar-kit/

Sugiriendo que el sitio fue descargado el lunes 11 de febrero de 2019,
un día antes del hallazgo del sitio falso.

El uso de esta herramienta sugiere que el sitio real no fue
comprometido, sino más bien tuvo que ser clonado desde las vistas de
usuario para poder ser configurado en otro servidor. El sitio original
no posee esta línea en su código.

Las diferencias de código son menores, especialmente en el código [HTML
inicial](https://www.diffchecker.com/7jJKq1oH) (sin cambios
dinámicos en el DOM, como el formulario que se carga luego). Las
diferencias apreciables son espacio en blanco, los comentarios del
sistema HTTrack, cambios de algunas URLs para que el sitio malicioso
funcione y muestre el contenido correctamente, remoción de código de
tracking de Facebook y el funcionamiento del formulario de registro que
se carga dinámicamente.

Los formularios de registro de ambos sitios son tratados de forma
diferente, enviando su información a un lugar distinto. En el sitio
malicioso se envía la información a un script en el mismo servidor
llamado guardar.php

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/2.png)

Dirección de envío para el sitio real
(//system.voluntariosxvenezuela.com/venezuela/PublicForm?source=1&jquery=0&geo=4&publicFormGroupClass=col-md-6)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/3.png)

Dirección de envío para el sitio falso (guardar.php)

Al compararlo con el servidor del sitio genuino, se observan mensajes de
error distintos al ejecutar software de servidor web distinto. Esto se
pudo apreciar buscando urls inexistentes en ambos sitios. Se recibieron
respuestas con formatos diferentes, denotando que ambos sitios estaban
siendo ejecutados en servidores diferentes.

El servidor contaba con un certificado SSL expedido por Let\'s Encrypt
para
[www.voluntariovenezuela.com](http://www.voluntariovenezuela.com)
elaborado en Feb 11 17:38:42 2019 GMT

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/4.png)

Error 404 correspondiente al sitio voluntariosxvenezuela.com (real)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/5.png)

Error 404 correspondiente al sitio voluntariovenezuela.com (falso)

El servidor del sitio falso
[www.voluntariovenezuela.com](http://www.voluntariovenezuela.com)
tuvo la dirección IP 159.65.65.194. Durante la breve reaparición de la
campaña de phishing el mismo servidor, u otro con el mismo propósito, tuvo
la dirección IP 134.209.13.64.

Luego del levantamiento de la campaña, momentáneamente en la
tarde del 13 de febrero el servidor respondía a ese dominio [solamente
con](http://web.archive.org/web/20190213223700/http://voluntariovenezuela.com/)
`{\"status\":\"ok\"}`.

Comportamiento visible a usuarios
---------------------------------

Cuando el usuario de CANTV intentaba navegar al dominio real
voluntariosxvenezuela.com en una conexión insegura (HTTP) el navegador
terminaba en el servidor malicioso, que redirige al URL
www.voluntariovenezuela.com y no hay otro indicio de que haya ocurrido
algo incorrecto más allá del cambio de URL.

Si un ciudadano accedía mediante una conexión HTTPS el navegador web
mostraba una alerta indicando la inconsistencia entre el dominio
navegado voluntariosxvenezuela.com y el del certificado SSL del servidor
que correspondía al dominio falso.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/6.png)

Afectación y estatus actual
---------------------------

El ataque fue observado desde el 12 de febrero de 2019 y se reportó
hasta la mañana del día 13 de febrero, coincidiendo el inicio del ataque
con la marcha convocada por el presidente encargado Juan Guaidó en el
marco del Día de la Juventud.

Se estima que la campaña activa con spoofing DNS duró desde las 10:30 am
del 12 de febrero hasta las 4 am del día siguiente. Considerando que
muchos usuarios habrían de conectarse el 12 de febrero luego de escuchar
a Juan Guaidó en la marcha de ese día, que algunas importantes cuentas
de Twitter de la oposición compartieron el link https y no https ese
día, la predominancia de CANTV en el tráfico de internet y una idea de
el número de registros en ese día, se puede estimar de forma
conservadora que el número de afectados en las decenas de miles de
víctimas del phishing, es posible que sean más.

Es práctica en Venezuela la [discriminación
política](https://www.derechos.org.ve/opinion/discriminacion-politica-en-venezuela)
en los [trabajos del sector
público](http://elestimulo.com/blog/cidh-asegura-que-despidos-por-la-lista-tascon-violan-los-derechos-humanos/) y la [obtención de beneficios
sociales](https://www.derechos.org.ve/investigacion/los-clap-7-indicios-de-discriminacion-politica).
Esto ha generado un razonable temor entre los que no están seguros si
fueron víctimas del phishing o nol. Esto ha producido comparaciones con
una lista de opositores conocida como la [\"lista
Tascón\"](https://www.observatoriodeconflictos.org.ve/derechos-humanos/corte-idh-condena-uso-de-lista-tascon-para-violar-derechos-politicos),
derivada de la participación en un proceso político y que se ha usado
para aplicar discriminación política, y cuya utilización por parte del gobierno fue
[condenada](https://www.observatoriodeconflictos.org.ve/derechos-humanos/corte-idh-condena-uso-de-lista-tascon-para-violar-derechos-politicos)
por la Corte Interamericana de Derechos Humanos.

La campaña terminó temprano el 13 de febrero y volvió brevemente en la
tarde del 14. Las razones detrás de la suspensión de la campaña se
desconocen, pero posiblemente están relacionadas con el impacto de las
denuncias sustentadas técnicamente. El cese en el spoofing DNS no
necesariamente tendría que coincidir con la inaccesibilidad del sitio,
pero en el incidente han venido de la mano.

La inaccesibilidad del sitio malicioso pudo ser producida por los
administradores desactivando el sitio, ataques de denegación de servicio
(DoS) exitosos de usuarios indignados como reportaron en redes sociales
el 13 de febrero, o por la bajada exitosa por parte de los proveedores de
alojamiento.

Para el momento de publicación de este informe ninguno de los dominios
de phishing descubiertos resuelve a alguna dirección IP.

Otras campañas de phishing
==========================

### Propietarios del servidor y dominios

Se observó que el servidor analizado no tenía ninguna información que
diera pistas de quién sería el propietario del sitio, además de que este
estaba alojado en la empresa Digital Ocean.

Al analizar el dominio voluntariovenezuela.com se observó que tenía
habilitada protección Whois, por lo que no se pudo obtener información
sobre la persona y/o empresa que registró el dominio. Sin embargo, al
indagar sobre otros dominios asociados a la dirección IP correspondiente
surgieron varios otros presuntamente usados para alojar sitios falsos de
redes sociales y otros servicios conocidos. Todos estos dominios
adicionales terminan en .ve, los cuales son arrendados y autorizados por
el órgano regulador de telecomunicaciones de Venezuela CONATEL.

Los nuevos dominios encontrados tienen datos de registro Whois
disponibles, exponiendo los siguientes datos de propietario:

Nombre: Frank Lopez

Correo electrónico:
[franklopezsystem@gmail.com](mailto:franklopezsystem@gmail.com)

Empresa: micompraventa

Dirección: Caracas, 1 VE

Teléfono: 0212-0212-5554545 (Se asume 0212-5554545)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/7.jpg)

Respuesta de whois para gmail.web.ve, uno de los nuevos dominios
encontrados.

Archive con data truncada del whois de google.web.ve:
[https://archive.fo/BBnZf](https://archive.fo/BBnZf)\
\
Previo a la denuncia al sitio voluntariovenezuela.com, la información
Whois de todos los dominios coincidían tanto en email como en número
telefónico del propietario, luego, posteriormente a la publicación en Twitter
de estos dominios se cambió el número telefónico a 0212-5554545. Sin
embargo, previamente todos tenían el número que coincide con el que está
aún registrado en google.web.ve al tiempo de la publicación: 0212-9090597.

Los dominios encontrados en servicios de búsqueda inversa de DNS e
historia de DNS para el servidor de interés fueron:

-   m.facebook.co.ve

-   www.facebook.co.ve

-   static.facebook.co.ve

-   facebook.co.ve

-   ssl.gmail.web.ve

-   gmail.web.ve

-   www.gmail.web.ve

-   accounts.gmail.web.ve

-   linkedin.co.ve

-   www.linkedin.co.ve

-   account.live.web.ve

-   outlook.live.web.ve

-   live.web.ve

-   www.live.web.ve

-   login.live.web.ve

-   mobile.twitter.info.ve

-   api.twitter.info.ve

-   [abs.twitter.info.ve](https://securitytrails.com/domain/abs.twitter.info.ve/history/a)

-   twitter.info.ve

-   www.voluntariovenezuela.com

-   voluntariovenezuela.com

Resultado disponible en
[https://securitytrails.com/list/ip/159.65.65.194](https://securitytrails.com/list/ip/159.65.65.194)
para el 12 de febrero, antes de publicaciones en redes sociales sobre la
relación entre los mismos. Esta información sigue disponible en la en la
historia de cada uno de esos dominios en
[securitytrails](https://securitytrails.com/list/ip/159.65.65.194).

Al hacer una búsqueda con la herramienta ReverseWhois para el correo
electrónico franklopezsystem@gmail.com se consiguió que habían diversos
dominios bajo el root .ve que parecían apuntar a similares de redes
sociales. (Archive del Reverse Whois:
[archivo](https://archive.fo/eZkhr)). Haciendo comparación
con los whois de los dominios de interés, todos tenían la misma
información en correo electrónico y número telefónico:
[franklopezsystem@gmail.com](mailto:franklopezsystem@gmail.com)
y 0212 909 0597.\
\
Las entradas DNS para estos dominios apuntaban, el 13 de febrero de
2018, al servidor

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/8.jpg)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/9.png)

(Capturas de pantalla de las respuestas de dig:
[https://twitter.com/joseluisrivas/status/1095691955693150214](https://twitter.com/joseluisrivas/status/1095691955693150214)
y
[https://twitter.com/joseluisrivas/status/1095715963138387970](https://twitter.com/joseluisrivas/status/1095715963138387970))

Al revisar el host 159.65.65.194 contra shodan.io, se pudo conseguir que
había hecho un scan de puertos el 8 de febrero de 2018 y en el puerto 80
tenía una redirección a twitter.web.ve en una clara campaña de phishing
(Captura de pantalla en
[https://twitter.com/joseluisrivas/status/1095702783880245248](https://twitter.com/joseluisrivas/status/1095702783880245248)).

Los dominios encontrados en su mayoría se corresponden con servicios de
alto tráfico, y parecen dominios legítimos que pudieron ser usados
potencialmente para alojar otros sitios falsos en ataques diferentes de
phishing. Esto es sugerido en
[checkphish.ai](https://checkphish.ai/insights/url/1534412032063/33aabce69dc4ba807c062a746bf80289d82884907d3302d9620238421f85eb1d)
en donde se puede observar como resultado histórico que en el dominio
accounts.gmail.web.ve se alojó un sitio que imitaba al formulario de
inicio de sesión de Google.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/10.png)

Resultado en checkphish.ai para accounts.gmail.web.ve. Muestra una
captura web idéntica a un login de Gmail genuino.

Con esta evidencia, se establece un enlace claro entre los operadores de
la campaña de phishing contra voluntariosxvenezuela.com y los operadores
de las campañas de phishing con los otros dominios.

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/11.png)
![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/12.png)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/13.png)

### Atribución de las campañas de phishing

Con ayuda de varios investigadores de seguridad, pudimos conocer que al
intentar recuperar la contraseña de la cuenta
[franklopezsystem@gmail.com](mailto:franklopezsystem@gmail.com),
el número telefónico asociado con la cuenta para pasar al siguiente paso
coincide con el teléfono 0212 9090597.

Al llamar a este teléfono a las 11am del 13 de Febrero de 2018,
respondió una persona que se dijo llamar Gabriel y al preguntarle si
respondía de una empresa lo negó, al preguntar si era una casa de
familia respondió \"Esto es CNTI\".

Sin embargo, una investigación posterior ha conseguido que el número de
teléfono no corresponde con los rangos que suelen usar desde el CNTI
sino con los que suelen usar en CONATEL. En el footer de la página web
de CONATEL pueden verse los dos números principales que son 0212 909
0599 y 0212 909 0419 (el registrado en los dominios es 0212 909 0597 y
el registrado para recuperación del email también) (archive del
frontpage de conatel:
[https://archive.fo/lCYho](https://archive.fo/lCYho))\
\
Al buscar en archive.org, nos conseguimos con más información apuntando
al rango de teléfonos usados por CONATEL: 0212-909.03.11,
0212-909.03.47, 0212-909.04.18
[https://web.archive.org/web/20141024115047/https://www.conatel.gob.ve/index.php/principal/contactos](https://web.archive.org/web/20141024115047/https://www.conatel.gob.ve/index.php/principal/contactos)

Al llamar al número en cuestión en otras oportunidades, pudimos escuchar una mensaje de contestadora automática explicando que estábamos llamando a Conatel.

Así mismo, se pudo conseguir en un sitio web de pasantías de la UNEFA
Caracas que éste número telefónico había sido
referenciado el 15 de Octubre de 2018 por Gabriel Porco para su pasantía
en NIC.ve, en CONATEL. (La URL del sitio web se tiene preservada, así como
los contenidos preservados en servicios de archivo web; pero no se
publican para cuidar los datos personales de otras personas que se encuentran en los mismos)

![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/14.png)

NIC.ve fnciona bajo CONATEL, y es responsable de los dominios en la zona
del TLD .ve y Gabriel Porco es el encargado de NIC.ve. Su número está
enlazado con un email fachada.

El mecanismo que ha usado NIC.ve previamente para re-adquirir dominios
ha sido asignándolos a una especie de agujeros negros donde el titular
es NIC VE y el correo asociado es del tipo
\"[domainer4@nic.ve](mailto:domainer@nic.ve)\". Esto
puede verse en el whois de dominios recuperados durante procesos de
censura contra medios de comunicación como ntn24.com.ve,
vivoplay.com.ve, vpitv.com.ve, entre otros.

Se realizaron llamadas a este número de teléfono y la persona que respondió
el número de teléfono asociado con estos registros en primera instancia
dijo llamarse Gabriel. Luego de hacerse viral el hilo en Twitter con
todos estos elementos, los registros fueron rápidamente cambiados a un
número telefónico que envía a un correo de voz
0212-5554545![](/res/post_img/2019-02-15_Phishing_impulsado_por_gobierno_de_Venezuela/15.png)

Gabriel Porco trabaja en la operación en de los dominios en el root .ve.
El correo fachada posiblemente pertenece a él o alguien que trabaja en esa oficina,
pues se usó ese número de CONATEL para confirmar el email fachada, y
además tiene la posición en NIC.ve para hacer estos cambios rápidamente;
cambios que para el resto de los usuarios debe pasar por tickets de
soporte o emails y tiempos de espera de varias semanas por no haber plataforma automatizada del nic.ve.

Conclusiones
============

Este caso resulta sumamente grave por los precedentes de persecución a
activistas, voluntarios y opositores en Venezuela; particularmente el
uso de listas de ciudadanos usadas para ejercer discriminación en contra
de opositores al gobierno, que [datan al menos desde el año
2004](https://prodavinci.com/la-lista-tascon-y-la-persecucion-politica-a-proposito-de-la-sentencia-de-la-corte-interamericana/).
Esta situación pone en riesgo no sólo los datos de identificación de los ciudadanos
que deseaban inscribirse en el sitio web anunciado, sino además
información personal, privada o con la que pueden ser incriminados en la
medida en que algunos hayan sido víctimas de otros ataques usando sitios
falsos de redes sociales o correos electrónicos. Estimamos de forma
conservadora un número de decenas de miles de víctimas del phishing a
voluntariosxvenezuela.com, si bien es posible que sean más.

En el caso puntual del ataque de suplantación de identidad del sitio
voluntariosxvenezuela.com observamos el uso conjunto de 2 técnicas
diferentes: la primera es la configuración de un sitio falso con un
dominio similar en donde las personas que accedieron podían ingresar sus
datos como voluntarios de la misma forma que en el sitio original. La
segunda técnica es la intercepción y alteración de solicitudes DNS
hechas dentro del ISP más importante del país, CANTV, tanto a sus
propios servidores DNS como a cualquier otro fuera de este (DNS
*injection*), sugiriendo el uso de inspección de paquetes como
estrategia de interceptación. Estas solicitudes eran redirigidas al
sitio clon descubierto.

Para este caso se pudo recabar evidencia suficiente para demostrar que
no sólo se trató de un episodio de bloqueo sino de un ataque de
suplantación a un sitio web lanzado por la oposición a la administración
de Nicolás Maduro, para recopilar datos personales de
ciudadanos críticos con fines desconocidos. Además se pudo recabar
evidencia que conecta por primera vez un ataque de suplantación de
identidad con personas asociadas a instituciones públicas.

Recomendaciones
===============

### Para usuarios

-   Es sumamente importante reconocer el URL (dirección) del sitio que
uno está visitando y asegurarse de que haya una conexión segura
(HTTPS://) sin errores o alertas de parte del navegador. Si el
navegador dice que la conexión no es segura, desconfía
inmediatamente del sitio.

-   Hay que tener especial atención a potenciales sitios que intenten
suplantar a portales de redes sociales.

-   Como mecanismo de mitigación de estos riesgos, el cambio de
servidores DNS en dispositivos y routers resulta insuficiente,
dado que las peticiones a servidores confiables pueden ser
interceptadas. Se recomienda el uso de servicios VPN o Tor.

-   Como medida avanzada de mitigación de riesgos, el uso de
administradores de contraseñas que detectan el sitio web en donde
se está navegando puede ayudar a detectar dominios falsos y evitar
ingresar credenciales en estos sitios.

    -   También para usuarios con niveles altos de riesgo, el uso de
    llaves de seguridad USB para realizar inicios de sesión en
    servicios que las soportan como Google o Facebook entre otros
    ayuda a detectar cuando se quiere inciar sesión en un sitio
    falso.

### Para administradores de sitios web

-   Asegurarse de colocar certificados SSL/TLS en los sitios web
    administrados y proteger muy bien estos certificados.

-   Redirigir siempre el tráfico HTTP a HTTPS usando las configuraciones
    de servidores virtuales, redirección por .htaccess, inclusión de
    la cabecera HSTS, etc.

-   Sólo compartir URLS con HTTPS de sus sitios en comunicaciones
    oficiales.

-   Usar DNSsec para minimizar las probabilidades de éxito de ataques de
    phishing (engaños dirigidos) a sus usuarios.

-   Específicamente para la respuesta a incidentes similares y al
    equipo de VoluntariosXVenezuela.com:

-   Alertar de forma clara sobre incidentes de seguridad como el observado.

-   Educar a los usuarios sobre cómo detectar cambios de URLS, uso de HTTPS
    y tomar en serio advertencias de seguridad de los navegadores.

-   Tener protocolos claros de comunicación y funcionamiento:

    -   Explicar por qué canales se van a comunicar con los voluntarios
    o miembros de la plataforma. Al saber de dónde vendrían las
comunicaciones posteriores al registro las víctimas y no
víctimas podrán saber si la información es oficial, y evitar
seguir siendo victimizados.

    -   Ofrecer una forma sencilla y clara basada en correo electrónico
para identificar si una persona está o no en la lista de
registro, y así cada quién pueda saber si fue afectado o no
por el phishing.\
Posible implementación: Enviar un mensaje a este correo que diga si
ese correo fue registrado antes del 13 de febrero, si la
persona creía haberse registrado probablemente fue víctima del phishing.
Ofrecer más información y ayuda.

Por: [Andrés Azpúrua](https://twitter.com/andresAzp), [Carlos Guerra](https://twitter.com/cguerrave), [Jose Luis Rivas](https://twitter.com/joseluisrivas)
