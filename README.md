# VE sin Filtro

Código del sitio [vesinfiltro.org](https://vesinfiltro.org). VE sin Filtro es un programa de [Conexión Segura y Libre](https://conexionsegura.org/). Documenta la censura, la vigilancia y los ataques digitales en Venezuela.

La lista de bloqueos documentada está en otro sitio: [bloqueos.vesinfiltro.org](https://bloqueos.vesinfiltro.org/).

## Build local

El sitio usa Jekyll.

```sh
bundle install
LC_ALL=en_US.UTF-8 bundle exec jekyll serve
```

Abre `http://localhost:4000/`.

- Jekyll lee `_config.yml` solo al iniciar. Si cambias `_config.yml`, reinicia el servidor.
- Con Ruby 3.4 o posterior, el `Gemfile` necesita `csv`, `base64`, `bigdecimal` y `logger`. El `Gemfile` ya los incluye.

## Publicación

GitHub Pages publica el sitio desde `master`. GitHub Pages usa Jekyll 3.10, no Jekyll 4.

- No uses `and` ni `or` en `where_exp`. Jekyll 3.10 no los soporta y el `build` falla. Usa filtros de una condición, `concat` y `sort`.
- No uses `plugins` fuera de la lista de GitHub Pages.
- Un `build` local sin errores no garantiza un `build` sin errores en GitHub Pages.

## Estructura

| Ruta | Contenido |
|---|---|
| `_noticias/` | Las publicaciones: alertas, comunicados, análisis, noticias, reportes y guías. |
| `_bloqueos/` | Las guías para evadir bloqueos (`/bloqueos/`). |
| `_layouts/` | `post.html` para las publicaciones, `reporte.html` para los reportes largos, `default.html` para todas las páginas. |
| `_includes/` | Partes de las páginas: `header`, `footer`, `home` (`inicio.html`), listas, idioma. |
| `_data/ui.yml` | Los textos de la interfaz, en español y en inglés. |
| `_data/fields.yml` | La referencia de los campos del `front matter`. |
| `_data/nosotros.yml` | El texto de Nosotros/About, sin cambios desde el reporte 2025. |
| `assets/css/vsf.css` | Todos los estilos. |
| `res/` | Imágenes, PDFs y logos. Las imágenes generadas están en `res/post_img/generadas/`. Las miniaturas están en `res/post_img/miniaturas/`. |

Páginas principales: `/` y `/en/` (`home`), `/publicaciones/` y `/en/publications/`, `/reportes/`, `/nosotros/` y `/en/about/`.

## Nueva publicación

1. Crea un archivo en `_noticias/` con el nombre `AAAA-MM-DD-titulo.md`.
2. Completa el `front matter`. Los nombres de los campos están en inglés. Los valores están en español. Consulta `_data/fields.yml`.

```yaml
---
layout: post
title: "Título de la publicación"
permalink: /noticias/2026-11-03-titulo/
date: 2026-11-03 12:00:00 -0400
type: Alerta            # Alerta | Comunicado | Análisis | Noticia | Reporte | Guía
topics: ["Censura y bloqueos"]
excerpt: "Resumen de una o dos oraciones."
lang: es
image: /res/post_img/2026-11-03/portada.jpg
---
```

- Para un reporte largo, usa `layout: reporte` y el bloque `report:` (`cover`, `pdf`, `pages`, `series`). Consulta `_data/fields.yml`.
- `image` es la portada. Usa una imagen de 1200 × 630. Si la imagen no es apta para compartir, agrega `share_image`.

## Imágenes

| Campo | Uso |
|---|---|
| `image` | La imagen propia del post. El post la muestra como portada. |
| `share_image` | Tarjeta de 1200 × 630 para los previews de RRSS. Úsala si `image` es muy alta, cuadrada o pequeña. |
| `report.cover` | Portada vertical del reporte. La usan la página del reporte, `/reportes/` y el `home`. |
| `list_image` | Opcional. Miniatura de `/publicaciones/`. |

- **Previews de RRSS** (`og:image`, `twitter:image`): el sitio usa `share_image`. Si no existe, usa `image`. Si no hay ninguna, usa `/res/TWcard.png`.
- **`home`:** usa `share_image`, después `image`. Si falta el archivo, muestra un `placeholder`.
- **`/publicaciones/`:** usa una miniatura de `res/post_img/miniaturas/`, en este orden: `list_image`, `report.cover`, `share_image`, `image`. `_data/miniaturas.yml` asigna las miniaturas.
- Las imágenes generadas están en `res/post_img/generadas/`. El generador está fuera del `repo`.

## Publicaciones en dos idiomas

- Cada versión es un archivo propio, con `lang: es` o `lang: en`.
- Cada versión tiene `translation` con el `permalink` de la otra versión. Agrega `translation` en las dos versiones.
- El sitio usa `translation` para los `chips` [ES] [EN], el aviso de la otra versión, las listas y el `home` en inglés.

## Idioma del lector

- El idioma es el del navegador, o el del marcador `?lang=es` / `?lang=en` en la `URL`.
- Los enlaces de idioma agregan el marcador. Después de una elección, los enlaces internos lo mantienen.
- El sitio no usa `localStorage` ni `cookies`.
- El código está en `_includes/idioma.html`.

## URLs

- Todas las `URLs` publicadas deben seguir activas.
- Si cambias un `permalink`, agrega la `URL` anterior en `redirect_from`.
- Los `redirects` recuperados del historial de git tienen el comentario `# url-historica`.

## Reglas de contenido

- No reescribas el texto de los artículos. Solo se permiten correcciones mínimas: `links` rotos, posición de imágenes, estilo de tablas.
- Los cambios de metadatos están permitidos.
- Las publicaciones recuperadas de 2014 a 2017 tienen `legado: true`. Un comentario en su `front matter` indica el texto generado.

## Licencia

El contenido (no el sitio web) usa la licencia [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), salvo indicación contraria.
