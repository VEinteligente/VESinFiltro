---
layout: post
title: "Vulnerabilidad expuso datos personales de la plataforma Constructores"
excerpt: "Conexión Segura y Libre notificó al equipo de Vente Venezuela sobre una vulnerabilidad crítica en los sistemas de su plataforma Constructores, la cual exponía datos personales de usuarios registrados en la plataforma."
permalink: /noticias/2026-11-22-vulnerabilidad-mitigada-constructores/
date:   2026-11-22 11:57:00 -0400
type: Alerta
topics: ["Ciberseguridad y protección de datos"]
lang: es
image: res/post_img/2026-11-22-vulnerabilidad-mitigada-constructores.png
---
> Información en desarrollo

El 21 de Noviembre a la 1:30 pm hora de Venezuela un actor de amenaza publicó en un canal público de Telegram las vulnerabilidad que pudieron explotar en dos *endpoints* que responden datos personales sensibles sin autenticación.

Investigadores de VE sin Filtro (parte de Conexión Segura y Libre) verificaron las fallas de seguridad en dos rutas del sistema y evaluaron su impacto. 

Ayer mismo, pocas horas después de conocer las vulnerabilidades, se envió una comunicación responsable a los administradores de la web por email y otros medios al equipo de Constructores y Monitoreo Ciudadano de Vente Venezuela. La comunicación fue posible y recibida hoy 22 de noviembre a las 8:30 am (VET).

Las vulnerabilidades identificadas corresponden a dos endpoints pertenecientes a hastaelfinal\[.\]app, backend de la plataforma monitoreociudadano\[.\]net y venteavente\[.\]org, que carecían de medidas de seguridad mínimas y no requerían autenticación para su acceso. El acceso a datos por esta vía era trivial, y potencialmente podría usarse para extraer datos de forma automatizada.

A las 9:00 am las mitigaciones implementadas impedían la explotación de las vulnerabilidades mediante los vectores que habían sido difundidos y confirmados de forma independiente por nuestro equipo. Verificamos esta mitigación, pero nuestra validación se extiende únicamente a esos métodos de explotación, **no hemos realizado ninguna auditoría de seguridad sobre las plataformas de Vente Venezuela**.

Agradecemos al equipo de Constructores por actuar con rapidez una vez estuvieron al tanto de la vulnerabilidad, y les urgimos que se comuniquen de forma efectiva con todos los usuarios afectados. Es necesario un reconocimiento público de la filtración de datos personales y su alcance real, así como un análisis técnico que explique el incidente y sus medidas de mitigación.

# **Datos expuestos:**

Entre los datos expuestos y accesibles públicamente se encuentran: nombres completos, nacionalidad, cédula, emails, números de teléfono, país de residencia, centro de votación, afiliación política, **plantillas de identificación biométrica generadas a través de modelos de reconocimiento facial**. 

Una parte de los datos expuestos podía accederse a través de un feed RSS que registraba cambios en la plataforma, incluyendo el registro de nuevos usuarios. A través de esta ruta era posible ver en texto plano datos relacionados con la plantilla biométrica generada en base a la foto de la cédula y *selfie* que los usuarios suben a la plataforma.

Otro *endpoint* inseguro permitía a cualquier persona sin autenticación acceder a información histórica de la plataforma, incluyendo datos personales de **personas que participaron en el proceso electoral del 2024** y miembros adscritos al partido Vente Venezuela**.**

Si bien la vulnerabilidad se hizo conocida el día 21 de noviembre de 2026, no podemos determinar de manera independiente desde hace cuánto tiempo estos datos han estado expuestos ni quiénes pudieron tener acceso a ellos.