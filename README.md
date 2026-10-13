# AKG Photography

Web oficial de AKG Photography.

## Estado
El repositorio está preparado para publicarse gratis en Cloudflare Pages.

- Rama de producción: `main`
- Framework: ninguno
- Build command: `exit 0`
- Output directory: `public`
- HTTPS: Cloudflare lo activa automáticamente
- Despliegue automático: cada cambio en `main`
- URL pública definitiva: `https://akg-photography.pages.dev/`

## Archivos preparados
- `public/index.html` — web principal en producción
- `_headers` — seguridad y caché para Cloudflare Pages
- `_redirects` — compatibilidad con URL antigua
- `favicon.svg`
- `site.webmanifest`
- `public/robots.txt`
- `404.html`
- `sitemap-template.xml`
- `TU-PARTE-CLOUDFLARE.md` — instrucciones exactas para publicar

## Importante
No compres ningún servicio durante la configuración. Cloudflare Pages Free es suficiente para esta web.

La URL pública de producción es `https://akg-photography.pages.dev/`. GitHub queda como repositorio y origen de despliegues.

## Fuente de producción verificada (13-10-2026)
El sitio real https://akg-photography.pages.dev/ sirve la versión multipágina del directorio `public/`. Las copias antiguas de archivos en la raíz (como `index.html`, `sitemap.xml`) no se deben usar para desplegar Cloudflare. GA4 se carga desde `public/assets/site.js` únicamente tras aceptar las cookies; su identificador se administra ahí. La auditoría remota está automatizada en `.github/workflows/akg-live-audit.yml`.
