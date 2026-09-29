from __future__ import annotations
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from datetime import datetime, timezone
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
]

def get(url: str) -> tuple[int, str]:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PropietarioPracticoAudit/1.0)", "Accept-Language": "es-ES,es;q=0.9"})
    try:
        with urlopen(req, timeout=25) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except URLError as e:
        return 0, str(e)

def one(pattern: str, text: str) -> str:
    m = re.search(pattern, text, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

lines = [
    "# Live audit — Propietario Práctico",
    "",
    f"Generado: {datetime.now(timezone.utc).isoformat()}",
    "",
]

robots_status, robots = get(BASE + "/robots.txt")
sitemap_status, sitemap = get(BASE + "/sitemap.xml")
lines += [
    "## Crawl",
    f"- robots.txt HTTP: {robots_status}",
    f"- sitemap.xml HTTP: {sitemap_status}",
    f"- robots declara sitemap: {'sí' if '/sitemap.xml' in robots else 'NO'}",
    f"- robots permite raíz: {'sí' if 'Allow: /' in robots else 'revisar'}",
    "",
    "## Artículos",
    "",
    "| URL | HTTP | Canonical propio | Title |",
    "|---|---:|:---:|---|",
]

errors = 0
for path in URLS:
    status, html = get(BASE + path)
    canonical = one(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html)
    if not canonical:
        canonical = one(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', html)
    title = one(r"<title[^>]*>(.*?)</title>", html)
    own = canonical.rstrip("/") == (BASE + path).rstrip("/")
    if status != 200 or not own:
        errors += 1
    lines.append(f"| {path} | {status} | {'sí' if own else 'NO'} | {title.replace('|','-')} |")

lines += [
    "",
    "## Alertas automáticas",
    f"- Errores HTTP/canonical detectados: {errors}",
    "- Nota: este test analiza HTML descargable; la auditoría visual/JS debe complementarse con navegador renderizado.",
    "",
]

out = Path("propietario-practico/seo-ops/LIVE-AUDIT-LATEST.md")
out.write_text("\n".join(lines), encoding="utf-8")

print(f"Audit completed with {errors} HTTP/canonical alerts")
