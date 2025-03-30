---
layout: post
title: "Bloquean 52 dominios relacionados a MagisTV y FlujoTV por órden judicial"
excerpt: "Juez del estado Zulia ordena a CONATEL el bloqueo de dominios relacionados a Magis TV y Flujo TV, apps de piratería por IPTV y streaming. VE sin Filtro registró un total de 52 de estos dominios con bloqueos activos."
permalink: /noticias/2025-03-30-bloqueo-magistv/
date: 2025-03-30 10:30:00 -0400
categories: comunicado

---

El 26 de marzo del 2025 un juez del estado Zulia ordenó a CONATEL el bloqueo de dominios relacionados a Magis TV y Flujo TV, apps de piratería por IPTV y streaming, como parte de una investigación criminal en curso.

Hemos documentado el bloqueo de 52 dominios de los listados en la orden del juez desde que se conoció públicamente el 26 de marzo.  **La inmensa mayoría de los bloqueos en Venezuela no surgen de una orden judicial, sino directamente de una decisión administrativa de CONATEL.**

MagisTV y FlujoTV son apps que ofrecen acceso a contenido audiovisual, como películas, series, y televisión en vivo a través de internet (IPTV). Estas plataformas no cuentan con derechos sobre los contenidos que ofrecen, infringiendo los derechos de autor. Al operar de forma ilegal, estas apps no se encuentran en las tiendas de aplicaciones oficiales. En su lugar, se pueden descargar sus APKs desde diversos sitios web, algunos de los cuales incluyen **software malicioso.**

La orden del Tribunal Octavo de Control del Circuito Judicial Penal de Maracaibo lista más de 100 dominios. Varios de los cuales no están operativos y algunos tienen aparentes errores de tipeo. Además del bloqueo de las páginas web, también ordena el *“bloqueo del proveedor DNS”*, una instrucción poco clara, que parece ser un error por una confusión sobre el funcionamiento de internet. Bloquear los servidores DNS autoritativos para estos dominios podría tener consecuencias colaterales gravísimas dependiendo de dónde estén hospedados.

Según el documento, el bloqueo se ordena *“en virtud de que estos* [dominios]  *guardan vinculación con el procedimiento llevado en contra del ciudadano ROMER GABRIEL CAPUZZI GONZALEZ”* quién fue capturado el 26 de marzo y tenía orden de arresto captura del mismo tribunal. 

Resulta difícil imaginar que una sola persona pueda estar detrás de la coordinación de una vasta red de sitios web dedicados a la promoción y comercialización de servicios de piratería, como se ha sugerido. La orden tampoco aclara cuál es la base legal que sustenta la **órden de bloqueo**.

### Lista preliminar de sitios web bloqueados en al menos un ISP

<div class="table-responsive">
<table class="blocklist">
    <thead>
        <tr>
        <th rowspan="2"><strong>Dominio</strong></th>
        <th colspan="8"><strong>Mecanismo de Bloqueo por ISP</strong></th>
        </tr>
        <tr>
        <th><strong>CANTV</strong></th>
        <th><strong>Inter</strong></th>
        <th><strong>Movistar</strong></th>
        <th><strong>Digitel</strong></th>
        <th><strong>NetUno</strong></th>
        <th><strong>AirTek</strong></th>
        <th><strong>G-Network</strong></th>
        <th><strong>Thundernet</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>flujotv.mx</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>ww1.magistvya.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
            <td class="block">HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>www.magistvya.com</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>www.magistvmexico.net</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="partial">DNS</td>
            <td class="block">HTTPS/HTTP</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>www.magistv.pro</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>www.magistv.app</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
            <td class="block">HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujo-tv.me</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>www.magistv.info</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
            <td class="block">HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="orange">DNS + TCP IP</td>
        </tr>
        <tr>
            <td>tv.magistv.app</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="block">DNS + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="partial">DNS</td>
            <td class="block">HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotvonline.com</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotvoficial.net</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotvapp.org</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotvapk.org</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotv.tv</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotv.la</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujoapk.com</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>apkflujotv.com</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>flujotvla.com</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>www.magistv.to</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>www.magistv.page</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>www.magistv.cool</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>www.magistv-pc.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>tvflujolatino.com</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>magistv-vip.net</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>magistv-latino.net</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>magistv-app.net</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>magis-tv.vip</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>futbollibretv.tv</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujo-tv.co</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
        </tr>
        <tr>
            <td>www.flujotvmundo.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>serveriks.com</td>
            <td class="accesible">No</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>panelflujotv.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>mastertv.fun</td>
            <td class="accesible">No</td>
            <td class="orange">DNS + TCP IP</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>magisapp.app</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>futemax.mx</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="block">TCP IP + HTTPS/HTTP</td>
        </tr>
        <tr>
            <td>flujotvpro.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvperu.org</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvoriginal.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvmundo.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvlat.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvecuador.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvcr.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotvapp.app</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotv.vip</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotv.co</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujotv.ai</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujoapp.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujo-tv.app</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>flujo-tv-app.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>descargarflujotv.com</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
        <tr>
            <td>apkwd.magistv.news</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="partial">DNS</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
            <td class="accesible">No</td>
        </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="2"><img src="/res/VeSinFiltro-long.svg" /></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td class="social">@VEsinFiltro<br> vesinfiltro.com</td>
        </tr>
    </tfoot>
</table>
</div>
