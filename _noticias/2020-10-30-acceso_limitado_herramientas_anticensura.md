---
layout: post
title: "Acceso limitado a herramientas anti-censura en Venezuela"
#small:   ""
excerpt: "Desde servidores DNS bloqueados al bloqueo de los sitios web de varios VPNs. Regresa el apetito por bloquear herramientas para evadir censura."
permalink: /noticias/2020-10-30-acceso_limitado_herramientas_anticensura/
date:   2020-10-30 12:00:00 -0400
categories: bloqueos
image: /res/post_img/2020-10-30-es.png
---
![](/res/post_img/2020-10-30-es.png)

## Introducción
Por muchos años Venezuela ha sufrido bloqueos de páginas web, afectando desde medios de comunicación hasta iniciativas en respuesta a la pandemia de COVID-19. Adicionalmente, el proveedor de internet del estado, CANTV, ha implementado bloqueos para impedir el uso de herramientas de circunvención de censura. En 2018 [denunciamos](https://twitter.com/vesinfiltro/status/1009596837911826432?s=20) y posteriormente [documentamos](https://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/) el [bloqueo de Tor](https://vesinfiltro.com/noticias/CANTV_bloquea_Tor_2017-06-26/), una importante red para navegar de forma privada y evadir censura, además de registrar otras acciones dirigidas por el poder ejecutivo nacional que atentan en contra de las libertades digitales de los venezolanos.

Las precarias condiciones en las que se encuentra la libertad en internet en Venezuela han sido registradas por distintos organismos internacionales, incluyendo un [reporte de la oficina del alto comisionado de las Naciones Unidas para los Derechos Humanos](https://ohchr.org/EN/HRBodies/HRC/RegularSessions/Session41/Documents/A_HRC_41_18_SP.docx) y [Freedom House](https://freedomhouse.org/). En su último reporte, [Freedom on the net 2020](https://freedomhouse.org/country/venezuela/freedom-net/2020), Freedom House ha concluido que existen censuras directas a portales de noticias y de contenido político, limitando así su accesibilidad desde los mayores proveedores de internet en el país, lo que implica una clara violación de los derechos de los usuarios.

Las herramientas para poder evadir la censura o la intromisión del gobierno se han vuelto necesarias, no solo para los usuarios que buscan acceder a noticias sobre la realidad de Venezuela, sino también para los periodistas que buscan proteger tanto su información como a ellos mismos y a quienes los rodean.

**Este reporte actualiza qué herramientas para evasión de censura siguen disponibles para los usuarios de internet en Venezuela en los distintos proveedores de internet para Octubre del 2020.**

Uso de herramientas anti-censura
===

Las herramientas anti-censura consisten en varios métodos e instrumentos para evitar la censura en Internet, como por ejemplo servidores proxy, VPNs, Tor o técnicas de anonimización. Estas herramientas también pueden proporcionar una capa adicional de protección para aquellas personas que manejan información sensible como periodistas, activistas o líderes políticos.

En países donde el internet es fuertemente censurado y vigilado, el uso de herramientas de anti-censura se ha vuelto esencial. Los venezolanos durante muchos años han usado VPNs y cambiando sus DNS para evitar la censura del gobierno y proteger su privacidad digital. Sin embargo, estas prácticas también pueden verse afectadas por las mismas restricciones que intentan evadir.

El [informe del 2018](https://vesinfiltro.com/noticias/state_of_internet_censorship_2018-08-16/) llamado *"The State of Internet Censorship in Venezuela"* documenta cómo el proveedor de servicio de internet (ISP) del Estado venezolano bloqueó acceso a la red de Tor y a sus puentes públicos usados para evadir la censura aplicada sobre Tor. Adicionalmente, en 2019 VE sin Filtro alertó y documentó el bloqueo a los servicios de VPN Tunnelbear y Windscribe; así como identificó el bloqueo a la función "VPN" integrada en el navegador web Opera.

Hace apenas unos meses, el 28 de agosto de 2020, [VeSinFiltro informó](https://vesinfiltro.com/noticias/2020-08-28-block-VPNs/) sobre una nueva ola de restricciones de acceso por parte de los principales proveedores de Internet en Venezuela. En esta ocasión, el bloqueo afectó a Psiphon y Tunnelbear, ambos servicios VPN, y al proxy web Anonymouse, con la intención de frenar el programa de salud para el personal médico impulsado por el presidente de la Asamblea Nacional, Juan Guaidó, en medio de la crisis por el COVID-19.

Censura actual de VPNs y herramientas anti-censura
===
Para el 5 de abril del 2020, después de un incendio en una instalación clave que [provocó la caída de casi la mitad de su red nacional](https://twitter.com/vesinfiltro/status/1246985092045639686), la censura de CANTV hacia Tunnelbear, Windscribe y el VPN integrado de Opera cesó para la mayoría de sus usuarios, así como varios bloqueos HTTP (HTTP host y filtrado SNI) que también dejaron de ser efectivos, como se [reportó el 7 de abril del 2020](https://vesinfiltro.com/noticias/2020-04-06-levantados_multiples_bloqueos_cantv).

Sin embargo, para el 2020-08-20 tres nuevos bloqueos DNS fueron implementados en herramientas de circunvención, de las cuales dos aún se mantienen en todos los grandes ISPs, afectado así el acceso a sus sitios web aunque sin limitaciones en la funcionalidad dentro de sus apps.

| Página web | URL | CANTV | Movistar | Digitel | Inter | Supercable
|--|--|--|--|--|--|--
| Tunnelbear | https://tunnelbear.com | Bloqueado | DNS Block | Bloqueado | DNS Block |  DNS Block
| Psiphon | https://psiphon.ca | Bloqueado | DNS Block | Bloqueado | DNS Block |  DNS Block

Esta nueva ola de bloqueos DNS vino después del anuncio de un plan creado por Juan Guaidó y la Asamblea Nacional para brindarle ayuda monetaria a los trabajadores de la salud en plena pandemia causada por el COVID-19. El dinero fue transferido a través de la plataforma AirTm, la cual rápidamente fue [bloqueada en los mayores proveedores de internet](https://twitter.com/vesinfiltro/status/1296564174198276102?s=20), por lo que muchas personas comenzaron a usar VPNs para evadir la censura. Tunnelbear y Psiphon fueron las herramientas [más recomendadas por nosotros](https://twitter.com/vesinfiltro/status/1296570595065331712), y [este video](https://youtu.be/iYQQTE1-Thk) sobre cómo usar un VPN se hizo viral después del bloqueo a AirTm.

A la fecha de publicación no se encontraron bloqueos impidiendo el funcionamiento de ningún VPN u otra herramienta de evasión de censura una vez ya instalada en el dispositivo. Sólo identificamos el bloqueo de las dos páginas web de los servicios previamente mencionados.

Bloqueos y limitaciones de servidores DNS
===
Límites en el uso normal de servidores DNS diferentes a los provistos por el ISPs fueron evidenciados en dos proveedores privados. El ISP de propiedad estatal no mostró ninguna restricción, pero la pena destacar cómo CANTV ha usado repetidamente inyecciones de respuesta DNS incluso cuando los usuarios usaban un servidor DNS de terceros durante [campañas masivas de phishing](https://vesinfiltro.com/noticias/Phishing_by_Venezuelan_government_targets_activists/) patrocinadas por el Estado.

{:.table-responsive.thead-dark.table-striped.table-sm}
| DNS Públicos | IP | CANTV | Movistar | Digitel | Inter | Dupercable |  
|-------------------------|-----------------|-------|-------------|-----------|-------|------------|  
| [a.resolvers.level3.net](http://a.resolvers.level3.net). | 4.2.2.1 | | | Bloqueado | | |  
| [b.resolvers.Level3.net](http://b.resolvers.Level3.net). | 4.2.2.2 | | | Bloqueado | | |  
| [c.resolvers.level3.net](http://c.resolvers.level3.net). | 4.2.2.3 | | | Bloqueado | | |  
| Cloudfare | 1.1.1.1 | | Inaccesible | Bloqueado | | |  
| Cloudfare | 1.0.0.1 | | | Bloqueado | | |  
| [cns1.cw.net](http://cns1.cw.net). | 141.1.1.1 | | | Bloqueado | | |  
| Comodo Secure DNS | 8.26.56.26 | | | Bloqueado | | |  
| Comodo Secure DNS | 8.20.247.20 | | | Bloqueado | | |  
| DNS Advantage | 156.154.70.1 | | | Bloqueado | | |  
| DNS Advantage | 156.154.71.1 | | | Bloqueado | | |  
| [dns-fra.de.ignite.net](http://dns-fra.de.ignite.net). | 195.182.110.132 | | | Bloqueado | | |  
| [dns-muc.de.ignite.net](http://dns-muc.de.ignite.net). | 62.134.11.4 | | | Bloqueado | | |  
| [dns1.nyc.dns-roots.net](http://dns1.nyc.dns-roots.net). | 208.78.24.238 | | | Bloqueado | | |  
| Dyn | 216.146.35.35 | | | Bloqueado | | |  
| Dyn | 216.146.36.36 | | | Bloqueado | | |  
| Google DNS | 8.8.8.8 | | | | | |  
| Google DNS | 8.8.4.4 | | | Bloqueado | | |  
| Open DNS | 208.67.222.222 | | | Bloqueado | | |  
| Open DNS | 208.67.222.220 | | | Bloqueado | | |  
| Quad 9 | 9.9.9.9 | | | Bloqueado | | |  
| Quad 9 | 149.112.112.112 | | | Bloqueado | | |  
| Yandex | 77.88.8.8 | | | Bloqueado | | |  
| Yandex | 77.88.8.1 | | | Bloqueado | | |  
| Yandex Family | 77.88.8.7 | | | Bloqueado | | |  
| Yandex Family | 77.88.8.3 | | | Bloqueado | | |  
| Yandex safe | 77.88.8.88 | | | Bloqueado | | |  
| Yandex safe | 77.88.8.2 | | | Bloqueado | | |  
| [cns2.cw.net](http://cns2.cw.net) | 195.27.1.1 | | | Bloqueado | | |  
| [uneeda.telstra.net](http://uneeda.telstra.net) | 139.130.4.4 | | | Bloqueado | | |

Digitel
---
Nuestras pruebas cubrieron una lista de 30 servidores DNS, los cuales todos se encontraron bloqueados por Digitel a excepción del más conocido, 8.8.8.8, el servidor DNS público de Google.

Digitel bloqueó cualquier conexión UDP o TCP en el puerto 53, independientemente de su contenido o protocolo en la capa de aplicación. Las solicitudes a estos servidores desde otros puertos funcionaron cuando estaban disponibles, con la excepción de las conexiones a 8.8.8.8 de Google que no estaban bloqueadas en lo absoluto.

**Podemos concluir que, con excepción del servidor 8.8.8.8 de Google, todos los demás servicios DNS se encuentran bloqueados para usuarios de Digitel.**

Movistar
---
En el caso de Movistar se encuentra inaccesible el 1.1.1.1, principal servidor DNS público de Cloudflare y APNIC. En vista que el resto de los DNS más populares, incluyendo 8.8.8.8 de Google, no presentan censura, es muy probable que este no sea un caso de censura sino un conflicto de operaciones interno con la dirección IP 1.1.1.1 por parte de Movistar.

El servidor DNS alternativo de Cloudflare 1.0.0.1 funciona completamente así como los servicios de la app móvil "1.1.1.1" de Cloudfare.

CANTV, Inter y Supercable
---
Todos los servidores DNS probados funcionan en CANTV, Inter y Supercable.

Recomendaciones
===
Recomendamos tener instalado y probado al menos un VPN en los dispositivos personales como celulares y computadoras, incluso si no se planea usarlos inmediatamente.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iYQQTE1-Thk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

El VPN que más recomendamos es Psiphon, pero Tunnelbear también es una buena opción que es muy fácil de usar. Para descargarlos desde Venezuela se pueden usar los siguientes links alternativos que hasta le fecha de publicación no han sido bloqueados:

**Psiphon:**

-   [psiphon3.com](http://psiphon3.com/es/download.html)

-   [Android: Play Store](https://play.google.com/store/apps/details?id=com.psiphon3.subscription)

-   [iOS: Apple App Store](https://apps.apple.com/us/app/psiphon/id1276263909?ls=1)

-   Proxy: [https://58685.info](https://58685.info/)

-   E-mail: get@psiphon3.com

**Tunnelbear:**

-   [Android: Play Store](https://play.google.com/store/apps/details?id=com.tunnelbear.android)

-   [iOS: Apple App Store](https://geo.itunes.apple.com/app/tunnelbear-vpn-unblock-websites/id564842283?mt=8&at=1010l9nk)

-   [tuneloso.com](http://tuneloso.com/)

Recomendamos usar un VPN de confianza, especialmente al acceder a sitios web de contenido político o participar en actividades en línea que puedan estar en conflicto con el oficialismo en Venezuela. Además, un VPN permite acceder a medios de comunicación y sitios web bloqueados.

Tampoco es mala idea cambiar los servidores DNS, mientras se esté consciente que esto no te ayuda a evadir todos los bloqueos en Venezuela ni te protege de manipulaciones sofisticadas de DNS que ha usado el Gobierno de Venezuela contra sus ciudadanos. Opciones de CNS públicas hay muchas, entre ellas las más reconocidas son: 8.8.8.8 y 8.8.8.4 (Google); 1.1.1.1 y 1.0.0.1 (Cloudflare y APNIC); o 9.9.9.9 y 149.112.112.112 (Quad 9). Para conocer cómo cambiar los DNS de tu computadora o dispositivo móvil, puedes revisar [este enlace](https://vesinfiltro.com/bloqueos/dns/).

Métodos
===
Todas las pruebas fueron realizadas en los meses de septiembre y octubre desde los siguientes ISPs: CANTV (AS8048), Movistar (AS6306), Digitel (AS264731), Inter (AS21826) y Supercable (AS22313). Es conocido que CANTV comparte su infraestructura clave y se comporta de la misma forma en cuanto a pruebas de anti-censura que su subsidiaria móvil, Movilnet (AS27889).

Revisión de herramientas bloqueadas
---
Para todas las herramientas se realizó una nueva instalación de la aplicación en un teléfono móvil conectado para cada ISP y se probó su funcionalidad realizando el caso de uso más común: utilizando la configuración predeterminada de la app o la herramienta. Si la herramienta requería que un usuario iniciase sesión, se realizaba el proceso de inicio de sesión conectado al ISP que se estaba probando en ese momento sin ninguna técnica anti-censura.

Para Tor específicamente se realizó la prueba [Vanilla Tor](https://ooni.torproject.org/nettest/vanilla-tor/) de OONI y las pruebas [Tor Bridge Reachability](https://ooni.torproject.org/nettest/tor-bridge-reachability/).



Las siguientes herramientas se probaron en todos los ISP:

-   “VPN” integrado del navegador Opera

-   Lantern

-   Tor

-   Tunnelbear

-   Psiphon

-   Windscribe VPN

-   hotspotshield

-   Intra

-   Outline

-   Open VPN

-   Hyde My Ass

-   1.1.1.1 app (DoT / DoH)

-   1.1.1.1 app (1.1.1.1 + Warp)

Revisión de páginas web bloqueadas
---

La lista de sitios web se probó utilizando la [prueba de conectividad web](https://ooni.torproject.org/nettest/web-connectivity/) de OONI, así como pruebas manuales para cualquier URL que produjera resultados anómalos de dicha prueba.

Se probaron las siguientes URL:

- “VPN” integrado del navegador Opera https://www.opera.com

-   Lantern https://getlantern.org

-   Tor https://www.torproject.org

-   Tor https://bridges.torproject.org

-   Tunnelbear http://tunnelbear.com

-   Tunnelbear http://tuneloso.com

-   Psiphon http://psiphon.ca

-   Psiphon http://psiphon3.com

-   Windscribe VPN https://windscribe.com

-   hotspotshield https://www.hotspotshield.com

-   Intra http://getintra.org

-   Outline http://getoutline.org

-   Guardster.com

-   multiproxy.org

-   Open VPN openVPN.net

-   proxy.org

-   Ultrasurf ultrasurf.us

-   Hyde My Ass https://www.hidemyass.com/

-   get2ip geti2p.net

-   Pure VPN purevpn.com

Revisión de servidores DNS bloqueados
-------------------
Para probar el acceso a consultas de DNS estándar se intentaron consultar programáticamente varios dominios conocidos de la siguiente lista de servidores DNS, y evaluando los casos en que no se obtuvieron respuestas en los ISP probados. Estas pruebas se repitieron varias veces en diferentes fechas.

También se probó DNS sobre TLS y DNS sobre HTTPS utilizando herramientas de línea de comandos.

-   Cada servidor DNS de los ISPs (generalmente privados)

-   a.resolvers.level3.net. 4.2.2.1

-   b.resolvers.Level3.net. 4.2.2.2

-   c.resolvers.level3.net. 4.2.2.3

-   Cloudfare 1.1.1.1

-   Cloudfare 1.0.0.1

-   cns1.cw.net. 141.1.1.1

-   Comodo Secure DNS 8.26.56.26

-   Comodo Secure DNS 8.20.247.20

-   DNS Advantage 156.154.70.1

-   DNS Advantage 156.154.71.1

-   dns-fra.de.ignite.net. 195.182.110.132

-   dns-muc.de.ignite.net. 62.134.11.4

-   dns1.nyc.dns-roots.net. 208.78.24.238

-   Dyn 216.146.35.35

-   Dyn 216.146.36.36

-   Google DNS 8.8.8.8

-   Google DNS 8.8.4.4

-   Open DNS 208.67.222.222

-   Open DNS 208.67.222.220

-   Quad 9 9.9.9.9

-   Quad 9 149.112.112.112

-   Yandex 77.88.8.8

-   Yandex 77.88.8.1

-   Yandex Family 77.88.8.7

-   Yandex Family 77.88.8.3

-   Yandex safe 77.88.8.88

-   Yandex safe 77.88.8.2

-   cns2.cw.net 195.27.1.1

-   uneeda.telstra.net 139.130.4.4

-   Two test servers, IPs not published.

### Bloqueos de Digitel
El bloqueo por parte de Digitel se identificó como un bloqueo de cualquier paquete UDP o TCP en el puerto 53, independientemente de su contenido o protocolo de capa de aplicación. Esto se probó utilizando herramientas para enviar diferentes tipos de solicitudes en diferentes puertos, incluidos paquetes ICPM a los servidores DNS e intentar las mismas solicitudes en nuestros servidores de prueba.

Podríamos confirmar que las solicitudes de DNS en diferentes puertos funcionaron y que el ISP está bloqueando los paquetes UDP y TCP en el puerto 53.
