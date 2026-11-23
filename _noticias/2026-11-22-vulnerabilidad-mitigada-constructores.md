---
layout: post
title: "Vulnerabilidad expuso datos personales de la plataforma Constructores"
excerpt: "Conexión Segura y Libre notificó al equipo de Vente Venezuela sobre una vulnerabilidad crítica en los sistemas de su plataforma Constructores, la cual exponía datos personales de usuarios registrados en la plataforma."
permalink: /noticias/2026-11-22-vulnerabilidad-mitigada-constructores/
date:   2026-11-22 11:57:00 -0400
type: Alerta
topics: ["Ciberseguridad y protección de datos"]
lang: es
image: /res/post_img/2026-11-22-vulnerabilidad-mitigada-constructores-actualizacion.png
---
> Actualizado 2026-11-23

El 21 de Noviembre a la 1:30 pm hora de Venezuela un actor de amenaza publicó en un canal público de Telegram las vulnerabilidad que pudieron explotar en dos *endpoints* que responden datos personales sensibles sin autenticación.

Investigadores de VE sin Filtro (parte de Conexión Segura y Libre) verificaron las fallas de seguridad en dos rutas del sistema y evaluaron su impacto. 

Ayer mismo, pocas horas después de conocer las vulnerabilidades, se envió una comunicación responsable a los administradores de la web por email y otros medios al equipo de Constructores y Monitoreo Ciudadano de Vente Venezuela. La comunicación fue posible y recibida hoy 22 de noviembre a las 8:30 am (VET).

Las vulnerabilidades identificadas corresponden a dos endpoints pertenecientes a hastaelfinal.app, backend de la plataforma monitoreociudadano.net y venteavente.org, que carecían de medidas de seguridad mínimas y no requerían autenticación para su acceso. El acceso a datos por esta vía era trivial, y potencialmente podría usarse para extraer datos de forma automatizada.

A las 9:00 am las mitigaciones implementadas impedían la explotación de las vulnerabilidades mediante los vectores que habían sido difundidos, confirmado de forma independiente por nuestro equipo. Nuestra validación se extiende únicamente a esos métodos de explotación, **no hemos realizado ninguna auditoría de seguridad sobre las plataformas de Vente Venezuela**.

Agradecemos al equipo de Constructores por actuar con rapidez una vez estuvieron al tanto de la vulnerabilidad, y les urgimos que investiguen el posible acceso a estos datos y su alcance de ser el caso, para poder comunicarse de forma efectiva con los usuarios que pudieran haber sido afectados.

Es necesario que la plataforma aclare públicamente el alcance real del abuso de esta vulnerabilidad, especialmente de existir un esfuerzo de exfiltración de datos, reciente o en el pasado; los tipos de datos vulnerados; y notificar individualmente a los afectados.  Así como un análisis técnico que explique el incidente y sus medidas de mitigación. 

Insistimos en la importancia de una auditoria de seguridad independiente. Recomendamos que se mejore la seguridad de la plataforma y que se permita a los usuarios registrarse sin datos biométricos y con la menor cantidad de datos sensibles posibles, para que cada persona pueda ajustar su riesgo frente a posibles vulneraciones.

## Datos expuestos:

Entre los datos expuestos y accesibles públicamente se encuentran: nombres completos, nacionalidad, cédula, emails, números de teléfono, país de residencia, centro de votación, afiliación política, **plantillas de identificación biométrica generadas a través de modelos de reconocimiento facial**. 

Una parte de los datos expuestos podía accederse a través de un feed RSS que registraba cambios en la plataforma, incluyendo el registro de nuevos usuarios. A través de esta ruta era posible ver en texto plano datos relacionados con la plantilla biométrica generada en base a la foto de la cédula y *selfie* que los usuarios suben a la plataforma.

Otro *endpoint* inseguro permitía a cualquier persona sin autenticación acceder a información histórica de la plataforma, incluyendo datos personales de personas que participaron en el proceso electoral del 2024 y miembros adscritos al partido Vente Venezuela**.**

Si bien la vulnerabilidad se hizo conocida el día 21 de noviembre de 2026, no podemos determinar de manera independiente desde hace cuánto tiempo estos datos han estado expuestos ni quiénes pudieron tener acceso a ellos.

## Actualización 2026-11-23: puntodeacuerdo.info

Investigadores de VE sin Filtro identificaron dos vulnerabilidades en un segundo sitio web relacionado, puntodeacuerdo.info, que fueron remediadas rápidamente luego de ser reportadas de forma privada.

Estas vulnerabilidades no habían sido publicadas por actores de amenaza ni por terceros antes de nuestro reporte. Estaban expuestos los perfiles de usuarios, y los creadores de los "Puntos de Acuerdo" con los siguientes datos:

- Nombre completo
- Nacionalidad (venezolana o extranjera)
- Cédula de identidad
- Teléfono
- Organización o comunidad
- Cargo o rol
- Presentación personal escrita por el usuario
- La [parte local](https://en.wikipedia.org/wiki/Email_address#Local-part)  (antes de @dominio.com) de los correos electrónicos usados como nombre de usuario en el sistema, de los creadores de los mismos, identificando cual fue creado por cada usuario.

Estas fallas son distintas de las encontradas en hastaelfinal.app, aunque son similares. La primera es un feed RSS con lo que parecen ser los últimos 10 "Puntos de Acuerdo" registrados y el usuario que creó cada uno. La segunda es una página que muestra datos personales de usuarios, entre otros objetos del sistema, identificados con un ID secuencial.

En ninguno de los casos VE sin Filtro tiene forma de saber si estas vulnerabilidades ya estaban siendo abusadas. Esperamos que el reporte temprano de estas fallas de seguridad haya servido para evitar cualquier ataque de exfiltración de datos del sistema. 

