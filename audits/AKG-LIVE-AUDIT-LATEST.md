# AKG Photography — auditoría externa

Comprobación UTC: 2026-10-25T11:54:56.126842+00:00
El informe muestra HTTP y HTML visible para el robot; no prueba indexación ni ejecución real de JavaScript.

## Publicación
- Home HTTP: 200
- Versión multipágina detectada: False
- Sitemap HTTP: 200
- Número de URL en sitemap: 19
- robots.txt HTTP: 200
- site.js HTTP: 200
- Etiqueta GA4 correcta dentro de site.js: True
- Home enlaza a site.js: False
- Gestión de consentimiento: True
- Eventos de contacto: True

## Páginas comerciales
| Ruta | HTTP | H1 | Canonical propia | Meta descripción |
|---|---:|---:|:---:|:---:|
| /fotografia-inmobiliaria-valencia/ | 200 | 1 | True | True |
| /fotografia-apartamentos-turisticos-valencia/ | 200 | 1 | True | True |
| /fotografia-hoteles-valencia/ | 200 | 1 | True | True |
| /fotografia-para-inmobiliarias/ | 200 | 1 | True | True |
| /fotografo-inmobiliario-sagunto/ | 200 | 1 | True | True |
| /fotografia-inmobiliaria-castellon/ | 200 | 1 | True | True |
| /portfolio/ | 200 | 1 | True | True |
| /contacto/ | 200 | 1 | True | True |

## Mejoras de contenidos (13-10-2026)
- Apartamentos turísticos: checklist y orden de fotos: True
- Hoteles: planificación por canal y checklist presupuesto: True
- Sitemap con lastmod apartamentos: True
- Sitemap con lastmod hoteles: True

## Publicación de mejoras locales (13-10-2026)
- Castellón: ampliación contextual activa: True
- Sagunto: checklist práctica activa: True
- Sitemap actualizado Castellón: True
- Sitemap actualizado Sagunto: True

## Diagnóstico de obtención del sitemap
La prueba con Googlebot UA simula solo la cabecera; NO acredita acceso del Googlebot auténtico.
| User-Agent | Método | HTTP | Content-Type | X-Robots-Tag | XML |
|---|---|---:|---|---|---|
| generic | GET | 200 | application/xml | — | 19 entries |
| generic | HEAD | 200 | application/xml | — | n/a |
| Googlebot UA | GET | 200 | application/xml | — | 19 entries |
| Googlebot UA | HEAD | 200 | application/xml | — | n/a |

## Interpretación
- Filas con comprobación incompleta o problema técnico: 0
- HTTP 429 puede ser bloqueo temporal de robots, no caída.
- Confirmar despliegue Cloudflare desde carpeta public si la home no enlaza site.js.
- Comprobar el estado de indexación de las URL en Google Search Console.
- Analítica solo se activa con consentimiento; confirmar eventos en GA4 Tiempo real.
