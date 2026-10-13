from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import xml.etree.ElementTree as ET
import time

HOST="https://akg-photography.pages.dev"
URLS=["/","/robots.txt","/sitemap.xml","/assets/site.js","/assets/style.css",
"/fotografia-inmobiliaria-valencia/","/fotografia-apartamentos-turisticos-valencia/",
"/fotografia-hoteles-valencia/","/fotografia-para-inmobiliarias/",
"/fotografo-inmobiliario-sagunto/","/fotografia-inmobiliaria-castellon/",
"/portfolio/","/contacto/","/public/index.html"]

class HTMLAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title="";self.description="";self.canonical="";self.h1=0;self.robots=""
        self.in_title=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="title":self.in_title=True
        if tag=="h1":self.h1+=1
        if tag=="meta" and a.get("name")=="description":self.description=a.get("content","")
        if tag=="meta" and a.get("name")=="robots":self.robots=a.get("content","")
        if tag=="link" and "canonical" in (a.get("rel") or "").split():self.canonical=a.get("href","")
    def handle_endtag(self,tag):
        if tag=="title":self.in_title=False
    def handle_data(self,s):
        if self.in_title:self.title+=s

def fetch(path):
    time.sleep(1)
    req=Request(HOST+path,headers={"User-Agent":"Mozilla/5.0 (compatible; AKGSiteAudit/1.0)"})
    try:
        with urlopen(req,timeout=15) as r:
            return r.status,r.read(1000000).decode("utf-8","replace")
    except HTTPError as e:return e.code,""
    except (URLError,TimeoutError) as e:return 0,str(e)

data={}
for path in URLS:
    data[path]=fetch(path)
    print(path,data[path][0],flush=True)

home=data["/"][1];js=data["/assets/site.js"][1]
sitemap=data["/sitemap.xml"][1]
try:urls=[e.text for e in ET.fromstring(sitemap).findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc") if e.text]
except ET.ParseError:urls=[]

report=[
"# AKG Photography — auditoría externa",
"",
"Comprobación UTC: "+datetime.now(timezone.utc).isoformat(),
"El informe muestra HTTP y HTML visible para el robot; no prueba indexación ni ejecución real de JavaScript.",
"",
"## Publicación",
"- Home HTTP: "+str(data["/"][0]),
"- Versión multipágina detectada: "+str("/assets/site.js" in home),
"- Sitemap HTTP: "+str(data["/sitemap.xml"][0]),
"- Número de URL en sitemap: "+str(len(urls)),
"- robots.txt HTTP: "+str(data["/robots.txt"][0]),
"- site.js HTTP: "+str(data["/assets/site.js"][0]),
"- Etiqueta GA4 correcta dentro de site.js: "+str("G-7888FPYJP1" in js),
"- Home enlaza a site.js: "+str("/assets/site.js" in home),
"- Gestión de consentimiento: "+str("cookieBanner" in js and "getConsent" in js),
"- Eventos de contacto: "+str("whatsapp_click" in js and "phone_click" in js),
"",
"## Páginas comerciales",
"| Ruta | HTTP | H1 | Canonical propia | Meta descripción |",
"|---|---:|---:|:---:|:---:|"
]
anomalies=0
for path in URLS:
    if path=="/" or not path.endswith("/") or path.startswith("/public/"):continue
    code,html=data[path]
    p=HTMLAudit()
    if code==200:p.feed(html)
    own=(p.canonical.rstrip("/")== (HOST+path).rstrip("/")) if code==200 else None
    desc=bool(p.description) if code==200 else None
    report.append(f"| {path} | {code} | {p.h1 if code==200 else '—'} | {own} | {desc} |")
    if code!=200 or not own or not desc or p.h1!=1 or "noindex" in p.robots:
        anomalies+=1

report+=["","## Publicación de mejoras locales (13-10-2026)",
"- Castellón: ampliación contextual activa: "+str("Cobertura en Castellón y entrega de las imágenes" in data["/fotografia-inmobiliaria-castellon/"][1]),
"- Sagunto: checklist práctica activa: "+str("Preparación práctica antes del reportaje" in data["/fotografo-inmobiliario-sagunto/"][1]),
"- Sitemap actualizado Castellón: "+str("https://akg-photography.pages.dev/fotografia-inmobiliaria-castellon/</loc><lastmod>2026-10-13" in sitemap),
"- Sitemap actualizado Sagunto: "+str("https://akg-photography.pages.dev/fotografo-inmobiliario-sagunto/</loc><lastmod>2026-10-13" in sitemap),
]

# Diagnose sitemap fetches with two user agents, recording headers and XML parseability.
# Spoofing Googlebot's user agent does NOT reproduce Google's IP or actual Google crawl.
def sitemap_diagnostic(agent, method):
    req = Request(HOST + "/sitemap.xml", headers={
        "User-Agent": agent,
        "Accept": "application/xml,text/xml,*/*",
    }, method=method)
    try:
        with urlopen(req, timeout=15) as response:
            body = response.read(1000000) if method == "GET" else b""
            parsed = "n/a"
            if method == "GET":
                try:
                    parsed = str(len(ET.fromstring(body).findall(
                        ".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"
                    ))) + " entries"
                except ET.ParseError as err:
                    parsed = "XML parse error: " + str(err)
            return {
                "code": response.status,
                "type": response.headers.get("Content-Type", ""),
                "robots": response.headers.get("X-Robots-Tag", ""),
                "cache": response.headers.get("Cache-Control", ""),
                "redirect": response.geturl(),
                "parsed": parsed,
            }
    except HTTPError as err:
        return {"code": err.code, "type": err.headers.get("Content-Type", ""),
                "robots": err.headers.get("X-Robots-Tag", ""), "cache": "",
                "redirect": err.geturl(), "parsed": "not readable"}
    except (URLError, TimeoutError) as err:
        return {"code": 0, "type": "", "robots": "", "cache": "",
                "redirect": "", "parsed": str(err)}

agents = [
    ("generic", "Mozilla/5.0 (compatible; AKGSiteAudit/1.0)"),
    ("Googlebot UA", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
]
report += [
    "", "## Diagnóstico de obtención del sitemap",
    "La prueba con Googlebot UA simula solo la cabecera; NO acredita acceso del Googlebot auténtico.",
    "| User-Agent | Método | HTTP | Content-Type | X-Robots-Tag | XML |",
    "|---|---|---:|---|---|---|",
]
for label, user_agent in agents:
    for method in ("GET", "HEAD"):
        time.sleep(1)
        check = sitemap_diagnostic(user_agent, method)
        report.append(
            f"| {label} | {method} | {check['code']} | {check['type']} | "
            f"{check['robots'] or '—'} | {check['parsed']} |"
        )

report+=["","## Interpretación",f"- Filas con comprobación incompleta o problema técnico: {anomalies}",
"- HTTP 429 puede ser bloqueo temporal de robots, no caída.",
"- Confirmar despliegue Cloudflare desde carpeta public si la home no enlaza site.js.",
"- Comprobar el estado de indexación de las URL en Google Search Console.",
"- Analítica solo se activa con consentimiento; confirmar eventos en GA4 Tiempo real.",
]
out=Path("audits/AKG-LIVE-AUDIT-LATEST.md")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text("\n".join(report)+"\n",encoding="utf-8")
