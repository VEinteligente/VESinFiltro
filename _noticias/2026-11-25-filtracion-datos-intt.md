---
layout: post
title: "Alegan filtración de datos y contraseñas de millones de usuarios del INTT"
excerpt: "Dos actores de amenaza aseguran tener los datos personales y las contraseñas de millones de usuarios del INTT. Aunque no ha sido verificado, recomendamos cambiar la contraseña del INTT y la de cualquier otro servicio donde se use la misma."
permalink: /noticias/2026-11-25-filtracion-datos-intt/
date:   2026-11-25 07:00:00 -0400
type: Alerta
subtype: Aviso de seguridad
topics: ["Ciberseguridad y protección de datos", "Datos personales"]
lang: es
image: /res/post_img/2026-11-25-filtracion-datos-intt.png
---
En el último mes, dos actores de amenaza distintos aseguraron haber obtenido los datos personales y las contraseñas de millones de usuarios de los sistemas del Instituto Nacional de Transporte Terrestre (INTT).

El anuncio más reciente, del 23 de noviembre de 2026, asegura contener los datos de más de 4 millones de usuarios y funcionarios. El primero, del 26 de octubre, no había sido identificado previamente y asegura contener la base de datos de usuarios completa, sin especificar el número de registros.

Ninguna de estas filtraciones ha sido verificada, pero los datos son muy verosímiles. Según las publicaciones, incluyen:

- Nombre
- Cédula
- Correo electrónico
- Dirección
- Datos de licencias
- Contraseñas hasheadas

No está clara la fecha de la exfiltración o exfiltraciones. Conexión Segura y Libre notificó a Suscerte y al INTT (a este último, a través del único correo público que pudo encontrar) y les solicitó tomar medidas urgentes.

## Por qué las contraseñas son lo más grave

Las contraseñas parecen estar hasheadas con MD5 sin *salt*, un método obsoleto. Con él, las contraseñas comunes o cortas pueden recuperarse en poco tiempo con herramientas de uso libre, y varias ya aparecen en texto plano en las publicaciones de los actores de amenaza.

Muchas personas usan la misma contraseña en varios servicios. Una contraseña del INTT expuesta puede dar acceso a su correo, a sistemas como el SAIME, a bancos o a los sistemas de su trabajo. Si no se toman medidas, estos datos ponen en grave riesgo la seguridad digital de millones de venezolanos y de todo tipo de instituciones.

## Recomendaciones

Si tienes o tuviste una cuenta en los sistemas del INTT:

1. **Cambia la contraseña de cualquier servicio donde uses la misma o una parecida.** Empieza por tu correo electrónico: quien controla tu correo puede recuperar el acceso a casi todas tus otras cuentas. Sigue con bancos, SAIME, redes sociales y los sistemas de tu trabajo.
2. **Usa una contraseña distinta para cada servicio.** Un gestor de contraseñas te ayuda a crearlas y recordarlas. Video: [¿Cómo crear contraseñas seguras?](https://www.youtube.com/watch?v=SJnjXOPZiu8)
3. **Activa la verificación en dos pasos** en tu correo, bancos y redes sociales. De ser posible, usa una aplicación de autenticación en lugar de SMS. Videos: [¿Cómo protegerte con verificación de dos pasos?](https://www.youtube.com/watch?v=jHH8qsTlTgo), [parte 2, con llaves de seguridad](https://www.youtube.com/watch?v=y0XYc49mNM4) y [cómo activarla en WhatsApp](https://www.youtube.com/watch?v=t8-NrDx3jss)
4. **Desconfía de llamadas, mensajes o correos que digan venir del INTT, de tu banco o de otra institución** y usen tus datos (nombre, cédula, dirección o licencia) para parecer legítimos. Estos datos facilitan el *phishing* y la suplantación de identidad. Nunca compartas contraseñas ni códigos de verificación. Video: [¿Cómo no caer en páginas falsas y phishing?](https://www.youtube.com/watch?v=HUyMo6o5kBc)
5. **No busques ni descargues los datos filtrados.** Los archivos que circulan pueden contener software malicioso, y su difusión expone aún más a las personas afectadas.

Más tutoriales de seguridad digital en el canal de YouTube de [Conexión Segura](https://www.youtube.com/@ConexionSegura).

## Exigimos al INTT y al Estado venezolano

- Mitigar cualquier vulnerabilidad activa.
- Investigar la veracidad de la filtración y los vectores usados.
- Obligar a los usuarios expuestos a cambiar su contraseña.
- Notificar a todos los usuarios afectados, para que puedan protegerse y cambiar con urgencia sus contraseñas en otros servicios y plataformas.
- Informar al público general sobre el alcance de la filtración.

El Estado venezolano tiene la responsabilidad de proteger los datos de sus ciudadanos y no puede seguir siendo un factor de riesgo para nuestra seguridad digital.

Actualizaremos esta publicación si hay nueva información.
