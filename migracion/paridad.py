#!/usr/bin/env python3
"""Parity check between the published Jekyll site and the Hugo build.

  python3 migracion/paridad.py extraer _site > base.json                    # snapshot of a Jekyll build
  python3 migracion/paridad.py comparar base.json migracion/salida/hugo
  python3 migracion/paridad.py comparar migracion/salida/jekyll migracion/salida/hugo   # also compares the text of <main>

For every HTML page it records the element ids (anchors that links and the TOC rely on), the <title> and the canonical
URL; a page with a meta refresh is recorded as a redirect and its target. "otros" lists the non-HTML files at the root.
comparar only compares the fields that both sides have, so the older baseline (ids and redirects only) still works.
Standard library only.
"""
import difflib
import json
import os
import re
import sys
from html.parser import HTMLParser

SITIO = "https://vesinfiltro.org"
VACIAS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Lector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.titulo, self.canonica, self.redirige = set(), None, None, None
        self._en_titulo = False
        self.texto, self._prof_main, self._ignorar = [], 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self._prof_main and tag not in VACIAS:
            self._prof_main += 1
        elif tag == "main":
            self._prof_main = 1
        if tag in ("script", "style"):
            self._ignorar += 1
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "title" and self.titulo is None:
            self._en_titulo, self.titulo = True, ""
        elif tag == "link" and a.get("rel") == "canonical" and self.canonica is None:
            self.canonica = a.get("href")
        elif tag == "meta" and (a.get("http-equiv") or "").lower() == "refresh":
            m = re.search(r"url=(.*)$", a.get("content") or "", re.I)
            if m:
                self.redirige = m.group(1).strip().replace(SITIO, "") or "/"

    def handle_endtag(self, tag):
        if tag == "title":
            self._en_titulo = False
        if tag in ("script", "style"):
            self._ignorar = max(0, self._ignorar - 1)
        if self._prof_main and tag not in VACIAS:
            self._prof_main -= 1

    def handle_data(self, data):
        if self._en_titulo:
            self.titulo += data
        if self._prof_main and not self._ignorar:
            self.texto.append(data)


def url_de(rel):
    rel = "/" + rel.replace(os.sep, "/")
    return rel[: -len("index.html")] if rel.endswith("/index.html") else rel


def extraer(raiz, con_texto=False):
    paginas, otros = {}, []
    for carpeta, _, archivos in os.walk(raiz):
        for nombre in archivos:
            ruta = os.path.join(carpeta, nombre)
            rel = os.path.relpath(ruta, raiz)
            if not nombre.endswith(".html"):
                if os.sep not in rel and "." in nombre:
                    otros.append("/" + rel)
                continue
            p = Lector()
            p.feed(open(ruta, encoding="utf-8", errors="replace").read())
            if p.redirige is not None:
                paginas[url_de(rel)] = {"redirige": p.redirige}
            else:
                d = {"ids": sorted(p.ids)}
                if p.titulo is not None:
                    d["titulo"] = re.sub(r"\s+", " ", p.titulo).strip()
                if p.canonica:
                    d["canonica"] = p.canonica.replace(SITIO, "")
                if con_texto:
                    d["texto"] = re.sub(r"\s+", " ", "".join(p.texto)).strip()
                paginas[url_de(rel)] = d
    return {"paginas": dict(sorted(paginas.items())), "otros": sorted(otros)}


def clave(url):
    """/x.html, /x/ and /x are the same address on GitHub Pages."""
    u = url[:-5] if url.endswith(".html") else url
    return u.rstrip("/") or "/"


def comparar(base, nuevo):
    b = {clave(k): (k, v) for k, v in base["paginas"].items()}
    n = {clave(k): (k, v) for k, v in nuevo["paginas"].items()}
    faltan = sorted(set(b) - set(n))
    sobran = sorted(set(n) - set(b))
    difs = []
    for k in sorted(set(b) & set(n)):
        (kb, vb), (kn, vn) = b[k], n[k]
        if "redirige" in vb or "redirige" in vn:
            if clave(vb.get("redirige", "?")) != clave(vn.get("redirige", "!")):
                difs.append((kb, "redirige", vb.get("redirige"), vn.get("redirige")))
            continue
        if "texto" in vb and "texto" in vn and vb["texto"] != vn["texto"]:
            r = difflib.SequenceMatcher(None, vb["texto"], vn["texto"], autojunk=False)
            if r.ratio() < 0.999:
                op = next(o for o in r.get_opcodes() if o[0] != "equal")
                difs.append((kb, "texto %.3f" % r.ratio(), vb["texto"][max(0, op[1] - 40):op[2] + 40], vn["texto"][max(0, op[3] - 40):op[4] + 40]))
        for campo in ("ids", "titulo", "canonica"):
            if campo in vb and campo in vn:
                x, y = vb[campo], vn[campo]
                if campo == "ids":
                    menos, mas = sorted(set(x) - set(y)), sorted(set(y) - set(x))
                    if menos or mas:
                        difs.append((kb, "ids", menos, mas))
                elif campo == "canonica" and clave(x) == clave(y):
                    continue
                elif x != y:
                    difs.append((kb, campo, x, y))
    otros = sorted(set(base.get("otros", [])) - set(nuevo.get("otros", [])))
    total = len(b)
    iguales = total - len(faltan) - len({d[0] for d in difs})
    print("Paridad: %d de %d direcciones iguales; %d faltan, %d con diferencias, %d nuevas.\n"
          % (iguales, total, len(faltan), len({d[0] for d in difs}), len(sobran)))
    if faltan:
        print("## Faltan en el build nuevo")
        for k in faltan:
            print("  ", b[k][0])
    if difs:
        print("\n## Diferencias (dirección, campo, antes, ahora)")
        for kb, campo, x, y in difs:
            if campo == "ids":
                print("  %s  ids  -%s  +%s" % (kb, x, y))
            else:
                print("  %s  %s  %r -> %r" % (kb, campo, x, y))
    if sobran:
        print("\n## Nuevas en el build nuevo")
        for k in sobran:
            print("  ", n[k][0])
    if otros:
        print("\n## Archivos de la raíz que faltan")
        for o in otros:
            print("  ", o)
    return 1 if (faltan or difs or otros) else 0


def main(argv):
    if len(argv) == 3 and argv[1] == "extraer":
        json.dump(extraer(argv[2]), sys.stdout, ensure_ascii=False, indent=1)
        print()
        return 0
    if len(argv) == 4 and argv[1] == "comparar":
        # Two build folders: the text of <main> is compared as well (difflib ratio under 0.999 is reported).
        dirs = os.path.isdir(argv[2]) and os.path.isdir(argv[3])
        base, nuevo = [extraer(a, dirs) if os.path.isdir(a) else json.load(open(a, encoding="utf-8")) for a in argv[2:4]]
        return comparar(base, nuevo)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
