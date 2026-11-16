// Pestañas, mapa y panel de transmisiones y ventana del reproductor de la recreación de 2014
(function () {
	var r = document.querySelector(".v14"); if (!r) return;
	var base = (document.currentScript && document.currentScript.src || "").replace(/v14\.js.*$/, "");  // carpeta de v14.js y res/
	var tabs = r.querySelectorAll(".v14-nav button"), paneles = r.querySelectorAll("[data-pestana]");
	function ver(id) {
		tabs.forEach(function (t) { t.setAttribute("aria-selected", t.dataset.ver === id); });
		paneles.forEach(function (p) { p.hidden = p.dataset.pestana !== id; });
		if (id === "transmisiones") cargarMapa();
	}
	tabs.forEach(function (t) { t.addEventListener("click", function () { ver(t.dataset.ver); history.replaceState(null, "", "#" + t.dataset.ver); }); });
	var h = location.hash.slice(1);
	ver(h === "transmisiones" || h === "informacion" ? h : "medios");

	var m = r.querySelector(".v14-modal"), cab = m.querySelector(".cab"), ifr = m.querySelector("iframe"), nota = m.querySelector(".nota");
	function abrir(clase, titulo, video, texto) {
		cab.className = "cab " + (clase || ""); cab.textContent = titulo || "";
		ifr.hidden = !video; ifr.src = video || ""; nota.innerHTML = texto;
		m.classList.add("on"); m.querySelector(".cerrar").focus();
	}
	function cerrar() { m.classList.remove("on"); ifr.src = ""; }
	r.querySelectorAll(".v14-tabla button").forEach(function (b) {
		b.addEventListener("click", function () { abrir(b.dataset.canal, "", b.dataset.video, b.dataset.nota); });
	});
	// panel de la derecha: la lista (mensaje de 2014 y transmisiones, filtrables por ciudad) o el detalle de una transmisión
	var panel = r.querySelector(".v14-panel"), sel = null;
	var vLista = panel.querySelector(".v14-vista-lista"), vDetalle = panel.querySelector(".v14-vista-detalle"), filtro = panel.querySelector(".v14-filtro");
	function verLista() { vDetalle.hidden = true; vLista.hidden = false; if (sel) sel.focus(); }
	function filtrar(ciudad) {
		panel.querySelectorAll(".v14-grupo").forEach(function (g) { g.hidden = !!ciudad && g.dataset.ciudad !== ciudad; });
		filtro.hidden = !ciudad; filtro.querySelector("span").textContent = ciudad || "";
	}
	filtro.querySelector("button").addEventListener("click", function () { filtrar(""); });
	panel.querySelector(".v14-volver").addEventListener("click", verLista);
	panel.querySelectorAll(".v14-ciudades button").forEach(function (b) {
		b.addEventListener("click", function () {
			sel = b; vLista.hidden = true; vDetalle.hidden = false;
			panel.querySelector(".v14-lugar").textContent = b.dataset.lugar;
			panel.querySelector(".v14-texto").textContent = b.dataset.desc;
			panel.querySelector(".v14-fecha").textContent = b.dataset.fecha;
			panel.querySelector(".v14-volver").focus();
		});
	});
	panel.querySelector(".v14-play").addEventListener("click", function () { if (sel) abrir("", sel.dataset.lugar, "", sel.dataset.nota); });

	// el mapa: OpenStreetMap con Leaflet en lugar de Google Maps; se carga al abrir la pestaña
	var mapaPedido = false;
	function cargarMapa() {
		if (mapaPedido) return; mapaPedido = true;
		var c = r.querySelector(".v14-mapa"), lf = c.dataset.leaflet;
		var css = document.createElement("link"); css.rel = "stylesheet"; css.href = lf + "/leaflet.min.css"; document.head.appendChild(css);
		var js = document.createElement("script"); js.src = lf + "/leaflet.min.js"; js.onload = function () { iniciarMapa(c); }; document.head.appendChild(js);
	}
	function iniciarMapa(c) {
		var num = function (t) { return t.split(",").map(Number); };
		var mapa = L.map(c.querySelector(".v14-lienzo"), { center: num(c.dataset.centro), zoom: +c.dataset.zoom, scrollWheelZoom: false });
		L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 19,
			attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' }).addTo(mapa);
		var pin = L.icon({ iconUrl: base + "res/mark.png", iconSize: [25, 41], iconAnchor: [12, 41] }), porCiudad = {};
		r.querySelectorAll(".v14-ciudades button").forEach(function (b) {
			var ciudad = b.closest(".v14-grupo").dataset.ciudad;
			(porCiudad[ciudad] = porCiudad[ciudad] || []).push([+b.dataset.lat, +b.dataset.lng]);
			L.marker([+b.dataset.lat, +b.dataset.lng], { icon: pin, title: b.dataset.lugar, alt: b.dataset.desc })
				.addTo(mapa).on("click", function () { b.click(); });
		});
		var boton = c.querySelector(".v14-menu-boton"), lista = c.querySelector(".v14-menu ul");
		boton.addEventListener("click", function () { lista.hidden = !lista.hidden; boton.setAttribute("aria-expanded", !lista.hidden); });
		lista.querySelectorAll("button").forEach(function (b) {
			b.addEventListener("click", function () {
				// nuevo: con varias transmisiones en la ciudad, el mapa se ajusta para mostrarlas todas (en 2014 era zoom 12 fijo)
				var pts = porCiudad[b.dataset.ciudad] || [];
				if (pts.length > 1) mapa.fitBounds(L.latLngBounds(pts), { padding: [40, 40], maxZoom: 15 });
				else mapa.setView(num(b.dataset.centro), +c.dataset.zoomCiudad);
				lista.hidden = true; boton.setAttribute("aria-expanded", "false");
				filtrar(b.dataset.ciudad); verLista();
			});
		});
		c.classList.add("listo"); mapa.invalidateSize();
	}

	m.querySelector(".cerrar").addEventListener("click", cerrar);
	m.addEventListener("click", function (e) { if (e.target === m) cerrar(); });
	document.addEventListener("keyup", function (e) { if (e.key === "Escape") cerrar(); });
})();

// Abre en una ventana las entradas de Información verificada que todavía tienen contenido
(function () {
	var r = document.querySelector(".v14"); if (!r) return;
	var m = r.querySelector(".v14-imodal"), cuerpo = m.querySelector(".cuerpo");
	function cerrar() { m.classList.remove("on"); cuerpo.innerHTML = ""; }
	r.querySelectorAll(".v14-info button.v14-entrada").forEach(function (b) {
		b.addEventListener("click", function () {
			cuerpo.innerHTML = document.getElementById(b.dataset.detalle).innerHTML;
			m.classList.add("on"); m.querySelector(".cerrar").focus();
		});
	});
	m.querySelector(".cerrar").addEventListener("click", cerrar);
	m.addEventListener("click", function (e) { if (e.target === m) cerrar(); });
	document.addEventListener("keyup", function (e) { if (e.key === "Escape") cerrar(); });
})();
