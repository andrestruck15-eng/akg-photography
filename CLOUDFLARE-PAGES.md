# Cloudflare Pages deployment

Recommended free production setup for AKG Photography.

- Provider: Cloudflare Pages Free
- Git repository: andrestruck15-eng/akg-photography
- Production branch: main
- Framework preset: None
- Build command: exit 0
- Root directory: repository root
- Build output directory: public
- Preferred project name: akgphotography
- Fallback project names: akgfotografia, akgphoto
- Expected free URL: https://<project-name>.pages.dev
- Automatic deployments: enabled on main
- HTTPS: automatic

The repository also includes a Cloudflare-compatible _headers file for security and caching.

No paid services are required.

## Production verification (2026-10-13)
- Production Cloudflare Pages serves the multi-page website from public/, not the old root index.html.
- The root index.html and root sitemap.xml remain historical and must not replace public/index.html or public/sitemap.xml in Cloudflare Pages.
- The Wrangler assets configuration also points to ./public.
- Live verification: https://github.com/andrestruck15-eng/akg-photography/blob/main/audits/AKG-LIVE-AUDIT-LATEST.md
