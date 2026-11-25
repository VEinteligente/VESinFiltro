---
layout: post
title: "Actualización sobre las vulnerabilidades en la plataforma Constructores"
excerpt: "Tres días después de que la plataforma Constructores corrigiera dos fallas de seguridad que expusieron datos personales, incluyendo datos biométricos, siguen sin respuesta las preguntas más importantes: desde cuándo estaban expuestos esos datos, quién los obtuvo y cuántas personas resultaron afectadas."
permalink: /noticias/2026-11-25-actualizacion-vulnerabilidades-constructores/
date:   2026-11-25 15:01:00 -0400
type: Comunicado
topics: ["Ciberseguridad y protección de datos", "Datos personales"]
lang: es
image: /res/post_img/2026-11-25-actualizacion-vulnerabilidades-constructores.png
---

**Tres días después de que la plataforma Constructores corrigiera dos fallas de seguridad que expusieron datos personales, incluyendo datos biométricos, siguen sin respuesta las preguntas más importantes: desde cuándo estaban expuestos esos datos, quién los obtuvo y cuántas personas resultaron afectadas.**

El 21 de noviembre a la 1:30 pm (hora de Venezuela), un grupo de actores de amenaza (hackers) publicó en su canal de Telegram, con cientos de seguidores, las vulnerabilidades que pudieron explotar en dos *endpoints* que entregaban datos personales sensibles sin autenticación. Como [informamos inicialmente](/noticias/2026-11-22-vulnerabilidad-mitigada-constructores/), verificamos las fallas y las comunicamos de forma responsable al equipo de Constructores. Alrededor de 12 horas después, nuestra notificación fue respondida y las fallas fueron corregidas a los pocos minutos.

[Dos vulnerabilidades similares](/noticias/2026-11-22-vulnerabilidad-mitigada-constructores/) en la web puntodeacuerdo.info también fueron informadas siguiendo protocolos de comunicación responsable antes de que, a nuestro conocimiento, fuesen conocidas o discutidas públicamente.

El caso de Constructores es distinto: la vulnerabilidad ya era del conocimiento de terceros. Incluso si sólo los seguidores del canal las conocieron en ese momento, es probable que varias personas hayan intentado extraer grandes cantidades de datos de forma sistemática. El abuso de estas fallas era trivial.

No tenemos certeza de cuándo se originaron estas vulnerabilidades, pero la evidencia sugiere que los datos estaban expuestos desde el inicio del proyecto.

Agradecemos que Constructores haya corregido las fallas al poco tiempo de conocer nuestro reporte. Recomendamos reforzar el monitoreo de amenazas y del comportamiento del sitio web para identificar nuevos ataques, así como realizar auditorías de seguridad periódicas e independientes.

## Preguntas que siguen abiertas

Tomamos nota del [reciente comunicado de Vente Venezuela](https://x.com/VenteVenezuela/status/2125189412405256429), pero hace falta un informe público mucho más completo, que responda las preguntas que quedan abiertas:

- ¿Desde cuándo eran explotables estas vulnerabilidades?  
- ¿Ha habido ataques sistemáticos para extraer datos de la plataforma, independientemente de las vulnerabilidades usadas? ¿Tuvieron éxito y cuál fue su alcance?  
- ¿Cuántos usuarios de Constructores se vieron afectados?  
- ¿Qué tipos de datos personales fueron extraídos?  
- ¿Cómo se ha mitigado el riesgo de nuevos ataques y qué mejoras de seguridad y de protección de datos se han hecho?

Debemos tener estándares altos al exigir protección de datos personales al Estado, a la industria y a todos los actores, sobre todo cuando se trata de información especialmente sensible.

Tenemos años documentando y combatiendo ciberataques del Estado venezolano y de actores asociados a éste contra iniciativas cívicas. También hemos exigido transparencia y responsabilidad frente a filtraciones de empresas e instituciones venezolanas. Esa exigencia se extiende a iniciativas como ésta.

## Lo que exigimos

Lo más urgente es informar. Constructores debe notificar individualmente a los usuarios afectados y aclararles qué datos fueron obtenidos. La Asociación Vente Venezuela España debe cumplir con su obligación de informar del incidente a la [Agencia Española de Protección de Datos](https://www.aepd.es/) (AEPD), si no lo ha hecho. Y hace falta un informe público que responda las preguntas abiertas.

El [Reglamento General de Protección de Datos](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (RGPD) de la Unión Europea fija plazos para una brecha de seguridad como esta:

> - **A la autoridad, en 72 horas (artículo 33).** El responsable debe notificar la brecha a la autoridad de control sin dilación indebida y, de ser posible, a más tardar 72 horas después de haber tenido constancia de ella. Si lo hace más tarde, debe explicar los motivos del retraso.  
> - **A los afectados, sin dilación indebida (artículo 34).** Cuando la brecha puede suponer un alto riesgo para los derechos y libertades de las personas, el responsable debe comunicársela directamente. Los datos biométricos y los que revelan opiniones políticas son categorías especiales de datos (artículo 9).

Recalcamos la importancia de proteger datos tan sensibles como la biometría y la afiliación a iniciativas políticas en un contexto de represión política en Venezuela.

Precisamente porque ningún sistema es completamente invulnerable ante ataques con suficientes recursos y sofisticación, es necesario recolectar **la menor cantidad posible de datos sensibles**, anonimizar todo lo posible y estar vigilantes ante las comunicaciones y amenazas de otros actores.

Por eso la exigencia de un acceso biométrico, que no está justificada por las funcionalidades ni por el objetivo del sistema, debe ser retirada. Los usuarios deben tener la opción de eliminar sus datos biométricos y pasar a autenticarse con contraseña en su próximo inicio de sesión o fácilmente en cualquier momento. El almacenamiento y tratamiento de cualquier dato biométrico debe ser reautorizado para cada propósito, claramente definido.

El proyecto necesita cambios fundamentales de diseño para poder operar de manera responsable: recolectar sólo los datos indispensables para cada función, explicar correctamente los objetivos de los datos, eliminar datos biométricos no autorizados y los históricos que ya no son necesarios, y tratar con especial precaución los datos biométricos y los que revelan la afiliación política.

Insistimos, como hemos hecho por más de un mes, en la necesidad de una auditoría independiente que ayude a fortalecer la seguridad del sistema y, ahora, a evaluar el alcance de posibles ataques con estas y otras vulnerabilidades.

La manera correcta de construir confianza en iniciativas de participación cívica es invertir el tiempo y los recursos necesarios para garantizar los más altos estándares de seguridad posibles, que lamentablemente no hemos observado.

Venezuela merece y necesita un futuro en el que la gente confíe, use y se beneficie de iniciativas y plataformas digitales porque sus datos están protegidos. Un futuro que deje atrás los esquemas de vigilancia estatal, con una ley de protección de datos personales, estándares técnicos y una cultura de seguridad y protección de datos.

