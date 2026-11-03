#!/usr/bin/env python3
"""Generate covers and share images for posts that lack a suitable one.

    python3 _imagenes/generar.py            # generate what is missing, update front matter and the review list
    python3 _imagenes/generar.py --forzar   # re-render every generated image (after changing plantilla.html)

What gets an image:
  * posts with no `image`, or whose image file is missing: a text cover (1200 x 630) set as `image`
    (a missing original stays in front matter as a comment ending in "# faltante, generada")
  * posts whose image is too tall, too square or too small to share: a share card set as `share_image`
  * reports whose `reporte.portada` file does not exist: a typographic report cover (707 x 1000)

Every line this script adds to front matter ends in "# generada", so it can be undone.
To reject an image, add the post's file name to _imagenes/rechazadas.txt and run the script again:
its generated lines are removed and the image is not made.

Needs Google Chrome (set CHROME=/path/to/chrome elsewhere) and macOS `sips` for sizes and JPEG export.
"""
import html, json, os, re, subprocess, sys, time, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "_imagenes")
BUILD = os.path.join(HERE, "build")
OUT = "/res/post_img/generadas"
MINI = "/res/post_img/miniaturas"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
FORCE = "--forzar" in sys.argv
TIPOS_EN = {"Alerta": "Alert", "Comunicado": "Statement", "Análisis": "Analysis", "Carta abierta": "Open letter", "Noticia": "News", "Reporte": "Report", "Guía": "Guide"}
SERIES_EN = {"Informe anual": "Annual report", "Especial": "Special report", "Política tecnológica": "Tech policy", "Estudio": "Study"}
GLYPHS = ["404", "NXDOMAIN", "†", "0.0.0.0", "SNI", "TCP", "RST", "451", "DNS", "ND", "TIMEOUT", "HTTP", "403", "ERR", "IP", "000", "404", "451"]

def fm_split(s):
    return re.match(r"\A---\s*\n(.*?\n)---\s*\n", s, re.S)

def field(fm, k):
    # [ \t] rather than \s: an empty field must not read the next line as its value
    m = re.search(rf"^{k}:[ \t]*(.*?)[ \t]*(?:# generada)?$", fm, re.M)
    if not m: return None
    v = m.group(1).strip()
    return v[1:-1] if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'" else v

def sub_field(fm, block, k):
    m = re.search(rf"^{block}:\s*\n((?:[ \t]+.*\n)+)", fm, re.M)
    return field(re.sub(r"^[ \t]+", "", m.group(1), flags=re.M), k) if m else None

def size_of(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path], capture_output=True, text=True).stdout
    try: return int(out.split("pixelWidth:")[1].split()[0]), int(out.split("pixelHeight:")[1].split()[0])
    except Exception: return None

MESES = {"es": "ENE FEB MAR ABR MAY JUN JUL AGO SEP OCT NOV DIC".split(), "en": "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()}
FONDO_TIPO = {"Alerta": "glifos", "Análisis": "datos", "Comunicado": "abstracto", "Carta abierta": "abstracto"}
LETRAS = "bcdefg"

def fecha_larga(iso, lang):
    y, m, d = iso[:10].split("-")
    return f"{int(d)} {MESES[lang][int(m) - 1]} {y}"

def site_file(path):
    return os.path.join(ROOT, urllib.parse.unquote(path.split("?")[0]).lstrip("/"))

def file_url(path):
    return "file://" + urllib.parse.quote(site_file(path))

def crop_style(path, crop, bw, bh, pos="center"):
    """Background CSS that covers a bw x bh box with the [x, y, w, h] region of an image."""
    W, H = size_of(site_file(path))
    x, y, w, h = crop or [0, 0, W, H]
    k = max(bw / w, bh / h)
    ox = -x * k - (w * k - bw) * {"left": 0, "right": 1}.get(pos, .5)
    oy = -y * k - (h * k - bh) / 2
    return f"background-image:url('{file_url(path)}');background-size:{W * k:.0f}px {H * k:.0f}px;background-position:{ox:.0f}px {oy:.0f}px"

def partes_titulo(title):
    """Main line, the part after the first colon, and trailing hashtags (each goes on its own line)."""
    t = re.sub(r"\s+", " ", title).strip()
    tags = re.findall(r"(?:\s+#[\wÀ-ÿ]+)+\s*$", t)
    tag = tags[0].strip() if tags else ""
    if tag: t = t[: -len(tags[0])].rstrip()
    main, sep, sub = t.partition(": ")
    if not sep or len(main) < 4: main, sub = t, ""
    return main.strip(), sub.strip(), tag

def extracto(text):
    body = re.sub(r"\A---.*?\n---\s*\n", "", text, flags=re.S)
    for par in re.split(r"\n\s*\n", body):
        p = re.sub(r"<[^>]+>|!\[[^\]]*\]\([^)]*\)|\{[%{].*?[%}]\}", "", par)
        p = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", p)
        p = re.sub(r"[*_#>`]", "", p).strip()
        if len(p) > 80: return p
    return ""

def share_body(post, d, lang, tipo_l):
    """HTML for a 1200 x 630 card. d holds the post's design choices (see disenos.json)."""
    plantilla = d.get("plantilla", "texto")
    fecha = fecha_larga(post["date"], lang)
    top = f'<div class="top"><img class="logo" src="../../res/VeSinFiltro-long.svg" alt=""><span class="fecha">{fecha}</span></div>'
    bar = '<div class="bar"><span class="url"><b>vesinfiltro</b>.org</span><span class="handle">@vesinfiltro</span></div>'
    if plantilla == "recorte":
        return f'<div class="f share" style="{crop_style(d["original"], d.get("recorte"), 1200, 630)};background-repeat:no-repeat"></div>'
    if plantilla == "original":
        kick = "Report" if lang == "en" else "Reporte"
        top = top.replace('src="../../res/VeSinFiltro-long.svg"', f'src="{file_url("/_imagenes/recursos/vsf-logo-oscuro.png")}"')
        return (f'<div class="f share original">{top}<span class="kicker" style="margin-top:22px">{kick}</span></p>'
                f'<div class="lado"><div class="lienzo"><img src="{file_url(d["original"])}" alt=""></div><p class="ot">{html.escape(d.get("titulo") or post["title"].strip())}</p></div>{bar}</div>')
    main, sub, tag = partes_titulo(d.get("titulo") or post["title"])
    def enf(x):
        x = html.escape(x)
        for w in d.get("enfasis", []):
            x = x.replace(html.escape(w), f'<em class="e">{html.escape(w)}</em>')
        return x
    h = f'<span class="m">{enf(main)}</span>' + (f'<span class="s">{enf(sub)}</span>' if sub else "") + (f'<span class="tag">{html.escape(tag)}</span>' if tag else "")
    clases, ground, media, extra = ["f", "share"], "", "", ""
    if post["tipo"] == "Reporte" and plantilla == "texto": clases.append("k-fuerte")
    kicker = html.escape(tipo_l)
    if plantilla == "bloqueo":
        clases.append("bloqueo"); kicker = "Bloqueado" if lang == "es" else "Blocked"
        desde = fecha_larga(d["desde"], lang); hasta = fecha_larga(d["hasta"], lang) if d.get("hasta") else ""
        lbl = ("desde", "hasta") if lang == "es" else ("since", "until")
        extra = ((f'<p class="sitios">{html.escape(", ".join(d["sitios"]))}</p>' if d.get("sitios") else "") + f'<div class="rango"><small>{lbl[0]}</small>{desde}' + (f'<span class="flecha">→</span>{hasta}' if hasta else "") + "</div>"
                 + ("" if d.get("sitios") else '<div class="isps">' + "".join(f"<span>{html.escape(i)}</span>" for i in d.get("isps", [])) + "</div>"))
        ground = '<div class="g g-puntos"></div>'
        if d.get("sitios"): clases.append("sin-pildoras")
        if d.get("captura") or d.get("logo"):
            clases.append("ventana")
            if d.get("metodo"): extra += f'<p class="metodo">{html.escape(d["metodo"])}</p>'
            dominio = d.get("dominio", "")
            if d.get("captura"):
                src, ts = captura(d["captura"], d["desde"])
                cuando = fecha_larga(f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", lang).lower()
                pie = (f"Captura del {cuando} · web.archive.org" if lang == "es" else f"Captured {cuando} · web.archive.org")
                vista = f'<div class="pantalla"><img src="{file_url(src)}" alt=""></div>'
            elif d.get("solo_logo"):
                media = f'<div class="media logo-bloque"><img src="{file_url(d["logo"])}" alt=""></div>'
            else:
                pie = d.get("logo_pie", "")
                vista = f'<div class="pantalla logo-sola"><img src="{file_url(d["logo"])}" alt=""></div>'
            if not d.get("solo_logo"): media = (f'<div class="media"><figure class="navegador"><div class="barra"><i></i><i></i><i></i><span class="dir"><s>{html.escape(dominio)}</s></span></div>'
                     f'{vista}<figcaption>{html.escape(pie)}</figcaption></figure></div>')
    elif plantilla == "reporte":
        c = d["colores"]; clases.append("reporte")
        style = f' style="--c0:{c[0]};--c1:{c[1]};--c2:{c[2]}"'
        light = int(c[0][1:3], 16) > 128
        if light: top = top.replace('src="../../res/VeSinFiltro-long.svg"', f'src="{file_url("/_imagenes/recursos/vsf-logo-oscuro.png")}"')  # official dark logo
        fondo = "" if light else '<div class="g g-puntos"></div><i class="glow"></i>'
        if d.get("arte"):
            clases.append("arte")
            return (f'<div class="{" ".join(clases)}"{style}>{top}<div class="main"><div class="col"><span class="kicker">{kicker}</span>'
                    f'<img class="t" src="{file_url(d["arte"][0])}" alt="" style="margin-top:18px;max-height:380px"></div>'
                    f'<div class="media"><img src="{file_url(d["arte"][1])}" alt=""></div></div>{bar}</div>')
        if d.get("antetitulo"): h = f'<span class="ante">{html.escape(d["antetitulo"])}</span>' + h
        return (f'<div class="{" ".join(clases)}"{style}>{fondo}{top}<div class="main"><div class="col"><span class="kicker">{kicker}</span>'
                f'<div class="hlbox"><h1 class="hl" data-max="110">{h}</h1></div></div></div>{bar}</div>')
    else:
        fondo = d.get("fondo") or FONDO_TIPO.get(post["tipo"], "puntos")
        if fondo == "glifos":
            ground = '<div class="g g-glifos">' + "".join(f'<span class="a">{c}</span>' if i in (7, 25, 40, 58) else f"<span>{c}</span>" for i, c in enumerate(GLYPHS[i % len(GLYPHS)] for i in range(72))) + "</div>"
        elif fondo == "datos":
            seed = sum(map(ord, post["title"]))
            ground = '<div class="g g-datos">' + "".join(f'<i class="{"a" if i == seed % 14 else ""}" style="height:{60 + (seed * (i + 3) * 37) % 330}px"></i>' for i in range(14)) + "</div>"
        elif fondo == "abstracto":
            ground = '<div class="g g-abstracto"></div>'
        elif fondo == "foto":
            pos = d.get("foto_pos", "right")
            clases.append("con-foto")
            fw = d.get("foto_w", 680)
            if pos == "right": style = f"left:{1200 - fw + d.get('foto_dx', 0)}px;width:{fw}px;right:auto;" + crop_style(d["foto"], d.get("recorte"), fw, 630, "right")
            else: style = crop_style(d["foto"], d.get("recorte"), 1200, 630)
            cls = {"right": "", "toma": "toma"}.get(pos, "full")
            if pos == "toma": clases.append("toma")
            ground = f'<div class="g g-foto {cls}" style="{style}"><div class="tram"></div></div>'
        else:
            ground = '<div class="g g-puntos"></div>'
        if d.get("inserto"):
            if d.get("inserto_forma") == "telefono":
                media = f'<div class="media" style="width:300px;align-items:flex-start"><div class="telefono"><img src="{file_url(d["inserto"])}" alt=""></div></div>'
            else:
                media = f'<div class="media"><figure class="marco" style="margin:0"><img src="{file_url(d["inserto"])}" alt=""></figure></div>'
        if d.get("extracto") and post.get("extracto"):
            extra = f'<p class="ex">{html.escape(post["extracto"])}</p>'
        if d.get("aliado"):
            extra += f'<span class="aliado" style="width:170px;height:112px;{crop_style(d["aliado"], d.get("aliado_recorte"), 170, 112)}"></span>'
    return (f'<div class="{" ".join(clases)}">{ground}<i class="glow"></i>{top}<div class="main"><div class="col"><span class="kicker">{kicker}</span>'
            f'<div class="hlbox"><h1 class="hl" data-max="{72 if plantilla == "bloqueo" else 96}">{h}</h1></div>{extra}</div>{media}</div>{bar}</div>')

def cover_body(main, sub, year, kicker):
    return (f'<div class="f cover"><div class="g g-puntos"></div><i class="glow"></i><span class="kicker">{html.escape(kicker)}</span>'
            f'<div class="t">{html.escape(main)}</div><div class="sub">{html.escape(sub)}</div>'
            f'<div class="foot"><span class="yr">{year}</span><img class="logo" src="../../res/VeSinFiltro-long.svg" alt=""></div></div>'), 62

def render(name, body, w, h, out_path, out_w):
    tpl = open(os.path.join(HERE, "plantilla.html"), encoding="utf-8").read()
    lang = "en" if "lang=en" in name else "es"
    page = tpl.replace("{{body}}", body).replace("{{lang}}", lang)
    os.makedirs(BUILD, exist_ok=True)
    src = os.path.join(BUILD, name + ".html"); png = os.path.join(BUILD, name + ".png")
    open(src, "w", encoding="utf-8").write(page)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2", f"--window-size={w},{h}",
                    "--virtual-time-budget=8000", f"--screenshot={png}", "file://" + src], capture_output=True)
    dest = os.path.join(ROOT, out_path.lstrip("/"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "80", "--resampleWidth", str(out_w), png, "--out", dest], capture_output=True)

CAPTURAS = "/_imagenes/capturas"

def captura(url, antes):
    """Screenshot of the last Wayback Machine capture of url before the date antes (YYYY-MM-DD), saved once in _imagenes/capturas/."""
    import datetime
    dia_antes = (datetime.date.fromisoformat(antes) - datetime.timedelta(days=1)).strftime("%Y%m%d")
    q = urllib.parse.urlencode({"url": url, "to": dia_antes, "output": "json", "limit": "-1", "filter": "statuscode:200", "fl": "timestamp"})
    os.makedirs(site_file(CAPTURAS), exist_ok=True)
    nombre = re.sub(r"[^a-z0-9]+", "-", urllib.parse.urlparse(url).netloc + urllib.parse.urlparse(url).path.lower()).strip("-")
    hechas = sorted(f for f in os.listdir(site_file(CAPTURAS)) if f.startswith(nombre + "-"))
    if hechas and not FORCE:
        f = hechas[-1]; return f"{CAPTURAS}/{f}", f.rsplit("-", 1)[1][:8]
    for intento in range(5):  # the archive refuses requests that come too fast
        out = subprocess.run(["curl", "-s", "-m", "60", "https://web.archive.org/cdx/search/cdx?" + q], capture_output=True, text=True).stdout
        try: ts = json.loads(out)[1][0]; break
        except (ValueError, IndexError): time.sleep(15 * (intento + 1))
    else: raise SystemExit(f"Wayback Machine: no capture of {url} before {antes}")
    png = os.path.join(BUILD, f"{nombre}-{ts}.png"); os.makedirs(BUILD, exist_ok=True)
    # "if_" serves the archived page without the Wayback toolbar
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2", "--window-size=1280,800", "--virtual-time-budget=20000",
                    f"--screenshot={png}", f"https://web.archive.org/web/{ts}if_/{url}"], capture_output=True)
    dest = f"{CAPTURAS}/{nombre}-{ts}.jpg"
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82", png, "--out", site_file(dest)], capture_output=True)
    return dest, ts[:8]

def set_line(path, key, value):
    s = open(path, encoding="utf-8").read(); m = fm_split(s); fm = m.group(1)
    if re.search(rf"^{key}:[ \t]*\S", fm, re.M): return
    if re.search(rf"^{key}:[ \t]*$", fm, re.M):  # an empty key is replaced in place
        fm = re.sub(rf"^{key}:[ \t]*$", f"{key}: {value} # generada", fm, count=1, flags=re.M)
    else:
        fm = fm + f"{key}: {value} # generada\n"
    open(path, "w", encoding="utf-8").write(s[:m.start(1)] + fm + s[m.end(1):])

def remove_generated(path):
    s = open(path, encoding="utf-8").read(); m = fm_split(s)
    fm = re.sub(r"^.*# generada\n", "", m.group(1), flags=re.M)
    open(path, "w", encoding="utf-8").write(s[:m.start(1)] + fm + s[m.end(1):])

def main():
    rech = set()
    rp = os.path.join(HERE, "rechazadas.txt")
    if os.path.exists(rp): rech = {l.strip() for l in open(rp, encoding="utf-8") if l.strip() and not l.startswith("#")}
    disenos = json.load(open(os.path.join(HERE, "disenos.json"), encoding="utf-8"))
    posts = sorted(f for f in os.listdir(os.path.join(ROOT, "_noticias")) if f.endswith(".md"))
    for f in posts: remove_generated(os.path.join(ROOT, "_noticias", f))  # every run starts from the posts' own front matter
    meta = {f: fm_split(open(os.path.join(ROOT, "_noticias", f), encoding="utf-8").read()).group(1) for f in posts}
    by_url = {field(fm, "permalink"): f for f, fm in meta.items()}
    lista = []
    for f in posts:
        if f in rech: continue
        path = os.path.join(ROOT, "_noticias", f); fm = meta[f]
        stem = os.path.splitext(f)[0].replace(" ", "-")
        title = field(fm, "title"); date = (field(fm, "date") or "")[:10]; lang = field(fm, "lang") or "es"
        tipo = field(fm, "type") or ""; tipo_l = TIPOS_EN.get(tipo, tipo) if lang == "en" else tipo
        img = field(fm, "image")
        d = disenos.get(f, {})
        reason = None
        if d.get("usar_original"): reason = None
        elif not img or img == "no": reason, key = "sin imagen", "image"
        elif not os.path.exists(site_file(img)): reason, key = "archivo de imagen faltante", "share_image"
        else:
            wh = size_of(site_file(img))
            if wh and (wh[0] < 600 or not 1.6 <= wh[0] / wh[1] <= 2.2):
                reason, key = f"proporción inadecuada para compartir ({wh[0]}×{wh[1]})", "share_image"
        if reason:
            post = dict(title=title, date=date, tipo=tipo, extracto=extracto(open(path, encoding="utf-8").read()) if d.get("extracto") or any(v.get("extracto") for v in d.get("variantes", [])) else "")
            variantes = d.get("variantes") or [d]
            salidas = []
            for i, v in enumerate(variantes):
                v = {**{k: x for k, x in d.items() if k != "variantes"}, **v}
                out = f"{OUT}/{stem}{'' if i == 0 else '--' + LETRAS[i - 1]}.jpg"
                if FORCE or not os.path.exists(site_file(out)):
                    render(stem + ("--" + LETRAS[i - 1] if i else "") + (".lang=en" if lang == "en" else ""), share_body(post, v, lang, tipo_l), 1200, 630, out, 1600)
                salidas.append(out)
            set_line(path, key, salidas[0])
            lista.append(dict(post=f, url=field(fm, "permalink"), titulo=title, clase="portada" if key == "image" else "compartir", motivo=reason,
                              imagen=salidas[0], variantes=salidas[1:], plantilla=d.get("plantilla", "texto"), anterior=img if img and img != "no" else "", estado="propuesta"))
        portada = sub_field(fm, "report", "cover")
        # typographic covers only for reports without a PDF; PDF reports use their real first page
        if portada and not sub_field(fm, "report", "pdf"):
            if FORCE or not os.path.exists(site_file(portada)):
                year = date[:4]
                pair = field(fm, "translation")
                if lang == "en" and pair in by_url: year = (field(meta[by_url[pair]], "date") or year)[:4]
                main_t, _, sub = title.partition(":")
                body, _ = cover_body(main_t.strip(), sub.strip(), year, "Report" if lang == "en" else "Reporte")
                render(stem + "-portada" + (".lang=en" if lang == "en" else ""), body, 707, 1000, portada, 620)
            lista.append(dict(post=f, url=field(fm, "permalink"), titulo=title, clase="portada-reporte", motivo="reporte web sin PDF ni portada",
                              imagen=portada, variantes=[], plantilla="portada", anterior="", estado="propuesta"))
    with open(os.path.join(ROOT, "_data", "imagenes_generadas.yml"), "w", encoding="utf-8") as fh:
        fh.write("# Images made by _imagenes/generar.py, for review. Reject one by adding its post file to _imagenes/rechazadas.txt.\n")
        for e in lista:
            fh.write("- " + "\n  ".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in e.items()) + "\n")
    print(len(lista), "imágenes")
    miniaturas(posts)

def miniaturas(posts):
    """Small copies of each post's list image for /publicaciones/: list_image, else the report cover, else the share image, else the image."""
    out = {}
    for f in posts:
        fm = fm_split(open(os.path.join(ROOT, "_noticias", f), encoding="utf-8").read()).group(1)
        src = field(fm, "list_image") or (sub_field(fm, "report", "cover") if field(fm, "layout") == "reporte" else None)
        src = src or field(fm, "share_image") or field(fm, "image")
        if not src or src == "no" or not os.path.exists(site_file(src)): continue
        dest = f"{MINI}/{os.path.splitext(f)[0].replace(' ', '-')}.jpg"
        d = site_file(dest)
        if FORCE or not os.path.exists(d) or os.path.getmtime(d) < os.path.getmtime(site_file(src)):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "72", "-Z", "480", site_file(src), "--out", d], capture_output=True)
        out[field(fm, "permalink") or f] = dest
    with open(os.path.join(ROOT, "_data", "miniaturas.yml"), "w", encoding="utf-8") as fh:
        fh.write("# Thumbnails for /publicaciones/, made by _imagenes/generar.py. Keys are post URLs.\n")
        for k, v in out.items(): fh.write(f"{json.dumps(k, ensure_ascii=False)}: {json.dumps(v)}\n")
    print(len(out), "miniaturas")

if __name__ == "__main__":
    main()
