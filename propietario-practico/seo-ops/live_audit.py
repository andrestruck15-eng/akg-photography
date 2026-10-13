from __future__ import annotations

from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import re
import xml.etree.ElementTree as ET

BASE = "https://proprietariopractico.blogspot.com"
URLS = [
    "/2026/09/precio-de-fotografo-inmobiliario-en.html",
    "/2026/09/checklist-para-preparar-una-vivienda.html",
    "/2026/09/cerradura-inteligente-para-airbnb-en.html",
    "/2026/09/fotografia-para-airbnb-en-valencia-que.html",
    "/2026/09/como-mejorar-un-anuncio-de-airbnb-guia.html",
    "/2026/09/fotos-para-airbnb-y-booking-guia-para.html",
    "/2026/09/fotografia-inmobiliaria-con-movil-guia.html",
    "/2026/09/que-comprar-para-preparar-un-piso-para.html",
    "/2026/09/como-fotografiar-un-apartamento-pequeno.html",
    "/2026/09/10-errores-en-fotografia-inmobiliaria.html",
    "/2026/09/caja-de-llaves-o-cerradura-inteligente.html",
    "/2026/09/home-staging-barato-mejorar-una.html",
    "/2026/09/como-hacer-fotos-de-un-piso-para-vender.html",
    "/2026/09/como-preparar-piso-para-alquilar.html",
]

def get(url: str) -> tuple[int, str]:
    req = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; PropietarioPracticoAudit/1.1)",
        "Accept-Language": "es-ES,es;q=0.9",
    })
    try:
        with urlopen(req, timeout=25) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except URLError as e:
        return 0, str(e)

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.h1 = []
        self.all_links = []
        self.body_links = []
        self.body_imgs = 0
        self.body_imgs_no_alt = 0
        self.depth = 0
        self.article_depth = None
        self.in_title = False
        self.in_h1 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "div":
            self.depth += 1
            if self.article_depth is None and "post-body" in classes:
                self.article_depth = self.depth
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.in_h1 = True
            self.h1.append("")
        if tag == "meta":
            name = (a.get("name") or "").lower()
            if name == "description":
                self.description = a.get("content") or ""
            if name == "robots":
                self.robots = a.get("content") or ""
        if tag == "link" and "canonical" in (a.get("rel") or "").lower().split():
            self.canonical = a.get("href") or ""
        if tag == "a" and a.get("href"):
            self.all_links.append(a["href"])
            if self.article_depth is not None:
                self.body_links.append(a["href"])
        if tag == "img" and self.article_depth is not None:
            self.body_imgs += 1
            if not (a.get("alt") or "").strip():
                self.body_imgs_no_alt += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False
        if tag == "div":
            if self.article_depth == self.depth:
                self.article_depth = None
            self.depth = max(self.depth - 1, 0)

    def handle_data(self, text):
        if self.in_title:
            self.title += text
        if self.in_h1 and self.h1:
            self.h1[-1] += text

def parse(html: str) -> PageParser:
    p = PageParser()
    p.feed(html)
    return p

def local_article(link: str) -> bool:
    u = urlsplit(link)
    return (u.hostname in (None, "proprietariopractico.blogspot.com")
            and (u.path or "").startswith("/2026/09/"))

def akg(link: str) -> bool:
    return urlsplit(link).hostname == "akg-photography.pages.dev"

def safe(s: str) -> str:
    return re.sub(r"\s+", " ", s).replace("|", "/").strip()

lines = [
    "# Live audit — Propietario Práctico",
    "",
    f"Generado: {datetime.now(timezone.utc).isoformat()}",
    "",
    "Este informe comprueba el HTML público. No acredita indexación en Google,",
    "conversiones GA4, ni la apariencia final en pantalla.",
    "",
]

home_status, home_html = get(BASE + "/")
home = parse(home_html) if home_status == 200 else PageParser()
robots_status, robots = get(BASE + "/robots.txt")
sitemap_status, sitemap = get(BASE + "/sitemap.xml")

sitemap_urls = []
if sitemap_status == 200:
    try:
        root = ET.fromstring(sitemap)
        sitemap_urls = [
            (node.text or "").strip()
            for node in root.findall(".//{*}loc")
            if node.text and "/2026/" in node.text
        ]
    except ET.ParseError:
        pass

lines += [
    "## Disponibilidad y descubrimiento",
    f"- Inicio HTTP: {home_status}",
    f"- robots.txt HTTP: {robots_status}",
    f"- sitemap.xml HTTP: {sitemap_status}",
    f"- robots declara sitemap: {'sí' if '/sitemap.xml' in robots else 'NO'}",
    f"- robots permite raíz: {'sí' if 'Allow: /' in robots else 'revisar'}",
    f"- Artículos en sitemap leído: {len(sitemap_urls)}",
    f"- Artículos esperados por lista de auditoría: {len(URLS)}",
    f"- URLs auditadas ausentes del sitemap: {', '.join(p for p in URLS if BASE + p not in sitemap_urls) or 'ninguna'}",
    "",
    "## Portada (HTML, no captura de pantalla)",
    f"- HTTP: {home_status}",
    f"- Title: {safe(home.title)}",
    f"- Meta description ({len(home.description)} caracteres): {safe(home.description)}",
    f"- H1 ({len(home.h1)}): {', '.join(safe(h) for h in home.h1) or '(no detectado)'}",
    f"- Canonical propio: {'sí' if home.canonical.rstrip('/') == BASE else 'NO / ausente'}",
    f"- Enlaces HTML a artículos: {sum(local_article(h) for h in home.all_links)}",
    f"- Enlaces HTML a AKG: {sum(akg(h) for h in home.all_links)}",
    f"- Texto 'lead_click' incluido en HTML: {'sí' if 'lead_click' in home_html else 'no detectado'} (NO acredita recepción por GA4)",
    "",
    "## Artículos — SEO técnico y enlaces contextuales",
    "",
    "| URL | HTTP | Canonical | H1 | Meta (car.) | Enlaces a artículos desde cuerpo | Enlaces AKG desde cuerpo |",
    "|---|---:|:---:|---:|---:|---:|---:|",
]

failures = []
missing_meta = []
low_links = []
for path in URLS:
    status, html = get(BASE + path)
    p = parse(html) if status == 200 else PageParser()
    own = p.canonical.rstrip("/") == (BASE + path).rstrip("/")
    context_links = [u for u in p.body_links if local_article(u)]
    akg_links = [u for u in p.body_links if akg(u)]
    if status != 200 or not own or "noindex" in p.robots.lower():
        failures.append(path + f" (HTTP {status}, canonical={own}, robots={p.robots})")
    if not p.description:
        missing_meta.append(path)
    if len(context_links) < 3:
        low_links.append(path)
    lines.append(
        f"| {path} | {status} | {'sí' if own else 'NO'} | {len(p.h1)} | "
        f"{len(p.description)} | {len(context_links)} | {len(akg_links)} |"
    )

lines += [
    "",
    "## Pendientes y alertas",
    f"- Alertas HTTP, canonical o noindex: {len(failures)}",
    *[f"  - {x}" for x in failures],
    f"- Artículos sin meta description: {len(missing_meta)}",
    *[f"  - {x}" for x in missing_meta],
    f"- Artículos con menos de 3 enlaces contextuales entre guías: {len(low_links)}",
    *[f"  - {x}" for x in low_links],
    "",
    "### Límites de este control",
    "- Un HTTP 429 aislado puede ser rate limiting; no debe tratarse automáticamente como caída.",
    "- Los enlaces de gadgets en footer no se cuentan como enlaces contextuales dentro del cuerpo del artículo.",
    "- Los datos GA4/GSC deben comprobarse en sus plataformas; este script no dispone de acceso a esas métricas.",
    "- El diseño responsive (3/2/1), tarjetas, snippets visibles y eventos JS requieren navegador renderizado.",
    "",
]

out = Path("propietario-practico/seo-ops/LIVE-AUDIT-LATEST.md")
out.write_text("\n".join(lines), encoding="utf-8")
print(f"Auditoría: {len(URLS)} URLs; alertas HTTP/canonical/noindex={len(failures)}; "
      f"sin metadescripción={len(missing_meta)}; menos de 3 enlaces={len(low_links)}")
