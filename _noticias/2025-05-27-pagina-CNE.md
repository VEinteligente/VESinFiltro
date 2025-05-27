---
layout: post
title: "<span style='font-size: 0.8em;'>¿Dónde está la página web del CNE?</span><br><br>El CNE mantiene inhabilitado su sitio oficial e impide el acceso a resultados electorales"
small: "El sitio web oficial del CNE, www.cne.gob.ve, lleva casi un año inaccesible, incluso 48 horas después de las elecciones, impidiendo el acceso a resultados e información oficial. A diferencia de los bloqueos externos, el propio CNE lo desactivó al eliminar sus registros DNS. Aunque servicios como el correo siguen operativos, esta omisión deliberada compromete la transparencia electoral y el derecho ciudadano a la información."
excerpt: "A casi un año desde su desactivación, el sitio web oficial del Consejo Nacional Electoral (CNE), www.cne.gob.ve, continúa inaccesible tanto desde Venezuela como desde el exterior. Esta situación reviste especial gravedad hoy, 48 horas después de celebrarse las elecciones regionales y legislativas, cuyos resultados e información oficial no pueden ser consultados por la ciudadanía."
permalink: /noticias/2025-05-27-pagina-CNE/
date: 2025-05-27 11:20:00 -0400
categories: reporte
image: /res/post_img/2024-08-01/image.jpg
---
A casi un año desde su desactivación, el sitio web oficial del Consejo Nacional Electoral (CNE), www.cne.gob.ve, continúa inaccesible tanto desde Venezuela como desde el exterior. Esta situación reviste especial gravedad hoy, 48 horas después de celebrarse las elecciones regionales y legislativas, cuyos resultados e información oficial no pueden ser consultados por la ciudadanía.

La página web del CNE no estuvo disponible en ningún momento antes ni durante el proceso electoral del 25 de mayo. Desde julio de 2024, luego de las elecciones presidenciales, el sitio web ha permanecido inaccesible. A diferencia de los bloqueos tradicionales realizados por proveedores de servicios de internet (ISP), en este caso es el propio CNE quien ha decidido mantener fuera de línea su página, hecho que hemos confirmado técnicamente.

Resulta injustificable que, luego de diez meses desde que el propio CNE retiró su sitio web, aún no lo haya restaurado ni haya publicado una plataforma nueva. El acceso a la información electoral, decisiones del directorio y resultados oficiales completos de las votaciones es fundamental. Esta omisión constituye un incumplimiento grave del deber institucionales del CNE de garantizar el acceso público a información relevante.

Esto comenzó luego de las presidenciales de 2024, cuando las direcciones IP del sitio dejaron de estar accesibles desde conexiones internacionales y algunos ISP venezolanos, una decisión implementada en la infraestructura de red del Estado. Luego, el mismo CNE eliminó los registros DNS necesarios para conocer las direcciones IP de www.cne.gob.ve (algunas de las direcciones IP a las que apuntaba este dominio eran: 190.9.130.14, 190.9.130.15, 200.11.144.25 y 200.44.45.5).

Técnicamente,  las computadoras se conectan con sitios web haciendo uso del Sistema de Nombres de Dominio (DNS), que actúa como un directorio o páginas amarillas, traduciendo nombres de dominio como www.cne.gob.ve, a direcciones IP específicas como por ejemplo 200.11.144.25. Esta dirección IP es necesaria para realizar la conexión real entre el dispositivo del usuario y el servidor del sitio web.

Desde antes del 28 de julio de 2024, www.cne.gob.ve empleaba un sistema de balanceo de carga, aparentemente basado en una arquitectura GSLB (Global Server Load Balancing), que distribuye el tráfico entre múltiples servidores, cada uno con una dirección IP, según la disponibilidad y ubicación del usuario. 
<figure>
  <br>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <img src="/res/post_img/2025-05-27/2025-05-27-cne.png" alt="Resultados de mediciones DNS al dominio www.cne.gob.ve. Fuente: RIPE Atlas" style="width: 48%;">
    <img src="/res/post_img/2025-05-27/2025-05-27-gslb.png" alt="Resultados de mediciones DNS al dominio www.gslb.cne.gob.ve. Fuente: RIPE Atlas" style="width: 48%;">
  </div>
  <figcaption style="text-align: center; margin-top: 10px; font-style: italic; color: #555;">
    <strong>Imagen 1:</strong> Resultados de mediciones DNS para www.cne.gob.ve (izquierda) y www.gslb.cne.gob.ve (derecha). Fuente: RIPE Atlas.
  </figcaption>
</figure>
<br>
La resolución del dominio, es decir, la traducción del nombre de dominio a la dirección IP, para www.cne.gob.ve depende de la resolución de www.gslb.cne.gob.ve, configurado mediante un registro CNAME. El resultado final debería ser una respuesta con la dirección IP de uno de los servidores para distribuir la carga de las visitas. En esta arquitectura típicamente sería una dirección IP óptima considerando la carga en los servidores y desde cuál red viene la solicitud del usuario.

Sin embargo, actualmente no es posible resolver el dominio www.cne.gob.ve porque www.gslb.cne.gob.ve no existe en los servidores DNS autoritativo correspondiente, como se ha verificado repetidamente desde diversos puntos internacionales y desde todos los principales proveedores de internet venezolanos. 

<figure>
  <br>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <img src="/res/post_img/2025-05-27/2025-05-27-traceroute.png" alt="Resultados de mediciones DNS al dominio www.cne.gob.ve. Fuente: RIPE Atlas" style="width: 48%;">
    <img src="/res/post_img/2025-05-27/2025-05-27-image2.png" alt="Resultados de mediciones DNS al dominio www.gslb.cne.gob.ve. Fuente: RIPE Atlas" style="width: 48%;">
  </div>
  <figcaption style="text-align: center; margin-top: 10px; font-style: italic; color: #555;">
    <strong>Imagen 2:</strong> Resultados de mediciones DNS para www.cne.gob.ve (izquierda) y www.gslb.cne.gob.ve (derecha). Fuente: RIPE Atlas.
  </figcaption>
</figure>
<br>

Además, las direcciones IP conocidas previamente para este sitio web tampoco responden. Dependiendo de la dirección IP y la red desde que se le consulta o están completamente inaccesibles o no dan respuesta ya no aloja el sitio web.

<figure>
  <br>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <img src="/res/post_img/2025-05-27/2025-05-27-cne-20044.png" alt="Resultados de pruebas de ping a la dirección IP 200.44.45.5. Fuente: RIPE Atlas." style="width: 48%;">
    <img src="/res/post_img/2025-05-27/2025-05-27-pin-200.png" alt="Resultados de pruebas de ping a la dirección IP 200.11.144.25. Fuente: RIPE Atlas." style="width: 48%;">
  </div>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <img src="/res/post_img/2025-05-27/2025-05-27-ping-190.png" alt="Resultados de pruebas de ping a la dirección IP 190.9.130.14. Fuente: RIPE Atlas" style="width: 48%;">
    <img src="/res/post_img/2025-05-27/2025-05-27-ping.png" alt="Resultados de pruebas de ping a la dirección IP 200.44.45.9. Fuente: RIPE Atlas" style="width: 48%;">
  </div>
  <figcaption style="text-align: center; margin-top: 10px; font-style: italic; color: #555;">
    <strong>Imagen 3:</strong> Resultados de pruebas de ping a las direcciones IP 200.44.45.5, 200.11.144.25, 190.9.130.14 y 200.44.45.9. Fuente: RIPE Atlas.
  </figcaption>
</figure>
<br>
Cabe destacar que no todos los servicios del CNE están afectados. Siguen operativos el sistema de correos electrónicos institucional, el campus virtual del Instituto de Altos Estudios del Poder Electoral "Tibisay Lucena" (virtualiaepe.cne.gob.ve) y varios portales privados del CNE que requieren credenciales para acceso.

Durante las recientes elecciones del 25 de mayo, el CNE utilizó el portal doe.postulaciones.org.ve para difundir información sobre los candidatos. Este portal dejó de estar operativo tras la votación y actualmente responde con un error 503: Servicio no disponible.

Todo esto evidencia una decisión deliberada por parte del CNE de no publicar su sitio web principal o no reemplazarlo oportunamente por otro que ofrezca información oficial sobre las elecciones, el funcionamiento del Poder Electoral y los resultados electorales.

Esta situación compromete gravemente la transparencia de los procesos electorales en Venezuela. La ciudadanía no puede acceder a los resultados oficiales ni a información clave sobre la jornada electoral, vulnerando su derecho fundamental a estar informada.

En un contexto donde los bloqueos informativos se han vuelto comunes, el caso del portal del CNE marca un precedente aún más alarmante: no se trata ya de censura impuesta, sino de una autocensura institucional que erosiona la legitimidad del proceso democrático.
