#!/usr/bin/env python3
"""Generates the Hugo content/ tree from the Jekyll sources.

Run from the repository root:  python3 migracion/convertir.py
content/ is generated and git-ignored until cutover, so posts edited on master keep flowing in:
merge master into this branch and run the script again.

What it changes (everything else in the front matter is kept as it is):
  permalink      -> url
  sites, type    -> sitios, tipo (Hugo reserves both: `type` picks the template folder)
  layout: page   -> layout: pagina (page.html is Hugo's template for all regular pages)
  redirect_from  -> aliases
  date           -> RFC 3339; from the filename when missing (Jekyll's rule)
  {: .a .b}      -> {.a .b}         (kramdown block attributes to Goldmark)
  {{page.x}} / {{ site.url }} in page bodies -> the literal value
  root pages whose body is only {% include X.html lang="..." %} -> layout X, the body is dropped
It prints a warning for any Liquid left in a body: that page needs a template or a shortcode.
"""
import os
import re
import shutil
import sys
from datetime import datetime

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "content")
COLECCIONES = ["noticias", "bloqueos", "documenta"]
# Root pages of the Jekyll site (everything at the root with front matter that Jekyll publishes).
PAGINAS = ["noticias.html", "inicio-en.html", "about.html", "nosotros.html", "publicaciones.html",
           "publications.html", "reportes.html", "reports.html", "bloqueos.html", "jump_point.html",
           "psiphon-jump_point.html", "reporta.html", "test.md", "test-medios.md", "test-puntual.md"]

FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)
FECHA_ARCHIVO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
INCLUDE_SOLO = re.compile(r"\A\s*\{%\s*include\s+([\w-]+)\.html(?:\s+lang=\"(\w+)\")?\s*%\}\s*\Z")
IAL = re.compile(r"^\{:\s*([^}]*)\}\s*$", re.M)
RENOMBRAR = {"sites": "sitios", "type": "tipo"}
# Jekyll layouts whose name means something else in Hugo: page.html is the template for every regular page.
LAYOUTS = {"page": "pagina"}
avisos = []


class Fecha(yaml.SafeLoader):
    """Keeps dates as strings, so the original offset is not lost on the way."""


Fecha.yaml_implicit_resolvers = {k: [r for r in v if r[0] != "tag:yaml.org,2002:timestamp"]
                                 for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def fecha_iso(valor, archivo):
    if valor is None:
        m = FECHA_ARCHIVO.match(os.path.basename(archivo))
        if not m:
            return None
        return "%s-%s-%sT00:00:00-04:00" % m.groups()
    s = str(valor).strip()
    for fmt in ("%Y-%m-%d %H:%M:%S %z", "%Y-%m-%d %H:%M %z", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            d = datetime.strptime(s, fmt)
        except ValueError:
            continue
        if d.tzinfo is None:  # Jekyll reads it in the site's timezone (America/Caracas, -04:00 today)
            return d.strftime("%Y-%m-%dT%H:%M:%S") + "-04:00"
        return d.isoformat()
    avisos.append("%s: fecha sin formato conocido: %r" % (archivo, s))
    return s


def ial(m):
    clases = re.findall(r"\.([\w-]+)", m.group(1))
    ids = re.findall(r"#([\w-]+)", m.group(1))
    partes = ["#" + i for i in ids] + ["." + c for c in clases]
    return "{" + " ".join(partes) + "}"


def convertir(origen, destino, extra=None):
    texto = open(origen, encoding="utf-8").read()
    m = FM.match(texto)
    if not m:
        avisos.append("%s: sin front matter, no se publica" % origen)
        return
    fm = yaml.load(m.group(1), Loader=Fecha) or {}
    cuerpo = m.group(2)
    fm.update(extra or {})

    for viejo, nuevo in RENOMBRAR.items():  # keys that Hugo reserves
        if viejo in fm:
            fm[nuevo] = fm.pop(viejo)
    if fm.get("layout") in LAYOUTS:
        fm["layout"] = LAYOUTS[fm["layout"]]
    if "permalink" in fm:
        fm["url"] = fm.pop("permalink")
    if "redirect_from" in fm:
        r = fm.pop("redirect_from")  # can be empty: redirect_from with no value
        r = [x for x in (r if isinstance(r, list) else [r]) if x]
        if r:
            fm["aliases"] = r
    fecha = fecha_iso(fm.get("date"), origen)
    if fecha:
        fm["date"] = fecha

    inc = INCLUDE_SOLO.match(cuerpo)
    if inc:
        fm["layout"] = inc.group(1)
        if inc.group(2):
            fm["include_lang"] = inc.group(2)
        cuerpo = ""
    else:
        for clave, valor in fm.items():
            if isinstance(valor, str):
                cuerpo = re.sub(r"\{\{\s*page\.%s\s*\}\}" % re.escape(clave), valor, cuerpo)
        cuerpo = re.sub(r"\{\{\s*site\.url\s*\}\}", "https://vesinfiltro.org", cuerpo)
        cuerpo = re.sub(r"\{%\s*for media in page\.sites\s*%\}.*?\{%\s*endfor\s*%\}", "{{< sitios >}}", cuerpo, flags=re.S)
        cuerpo = IAL.sub(ial, cuerpo)
        if fm.get("layout") == "home-6d":
            cuerpo = ""  # the layout never printed its content
        resto = re.findall(r"\{%.*?%\}|\{\{(?!<).*?\}\}", cuerpo)
        if resto:
            avisos.append("%s: Liquid sin convertir: %s" % (origen, ", ".join(sorted(set(resto)))[:200]))

    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000))
        f.write("---\n")
        f.write(cuerpo)


def main():
    if os.path.isdir(SALIDA):
        shutil.rmtree(SALIDA)
    n = 0
    for col in COLECCIONES:
        carpeta = os.path.join(RAIZ, "_" + col)
        for nombre in sorted(os.listdir(carpeta)):
            if nombre.startswith("."):
                continue
            # Spaces in a filename are fine in Jekyll; in Hugo they only change the file path, the url comes from front matter.
            convertir(os.path.join(carpeta, nombre), os.path.join(SALIDA, col, nombre), {"collection": col})
            n += 1
    # Section index pages would clash with /noticias/ (an alias of the home) and /bloqueos/ (a page): headless sections.
    for col in COLECCIONES:
        with open(os.path.join(SALIDA, col, "_index.md"), "w") as f:
            f.write("---\nbuild:\n  render: never\n  list: never\n---\n")
    for nombre in PAGINAS:
        base, ext = os.path.splitext(nombre)
        # noticias.html is the Spanish home (url /): in Hugo that is the home page, content/_index.html.
        destino = os.path.join(SALIDA, "_index.html") if base == "noticias" else os.path.join(SALIDA, "paginas", nombre)
        convertir(os.path.join(RAIZ, nombre), destino)
        n += 1
    with open(os.path.join(SALIDA, "paginas", "_index.md"), "w") as f:
        f.write("---\nbuild:\n  render: never\n  list: never\n---\n")
    print("%d archivos convertidos en content/" % n)
    for a in avisos:
        print("AVISO", a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
