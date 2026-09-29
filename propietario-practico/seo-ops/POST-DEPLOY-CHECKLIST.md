# Post-deploy checklist — Blogger V3

Usar inmediatamente después de subir la plantilla V3.

## Portada
- [ ] Hero visible.
- [ ] Rutas por objetivo visibles.
- [ ] Imágenes correctas.
- [ ] No aparece sidebar.
- [ ] Navegación funciona.
- [ ] AKG abre correctamente.
- [ ] Privacidad/cookies presentes en footer.

## Artículo individual
URL de control:
https://proprietariopractico.blogspot.com/2026/09/como-hacer-fotos-de-un-piso-para-vender.html

Debe cumplirse:
- [ ] Solo el artículo objetivo aparece en contenido principal.
- [ ] NO aparece "Precio de fotógrafo inmobiliario en Valencia" antes.
- [ ] FeaturedPost oculto.
- [ ] PopularPosts oculto.
- [ ] Sidebar oculta.
- [ ] Un único H1 principal visible.
- [ ] Cuerpo completo.
- [ ] Imagen correcta.
- [ ] No aparece "Publicar un comentario".
- [ ] Bloque "Sigue explorando" visible.
- [ ] Links del bloque funcionan.

## SEO técnico
- [ ] Canonical sigue apuntando a URL Blogger.
- [ ] robots.txt HTTP 200.
- [ ] sitemap.xml HTTP 200.
- [ ] sitemap conserva 13 URLs hasta publicar nuevas.
- [ ] old Cloudflare URL sigue redirigiendo a Blogger.
- [ ] No hay noindex accidental.

## Analytics
- [ ] GA4 recibe page_view.
- [ ] Clic en AKG genera evento akg_click.
- [ ] No hay duplicación evidente de page_view.
- [ ] Consentimiento se respeta.

## AdSense
- [ ] ads.txt sigue mostrando pub-2762317170112827.
- [ ] widgets de anuncios no rompen layout.
- [ ] no confundir anuncios con navegación.
- [ ] no volver a solicitar revisión si ya está en curso.

## Responsive
Desktop:
- [ ] portada limpia.
- [ ] artículos legibles.
Tablet:
- [ ] tarjetas no desbordan.
Móvil:
- [ ] navegación usable.
- [ ] texto sin overflow.
- [ ] imágenes dentro del viewport.
- [ ] bloque de enlaces relacionados en una columna.

## Criterio de rollback
Si ocurre cualquiera:
- artículos desaparecen;
- Blog1 deja de renderizar;
- canonical cambia;
- layout móvil queda inutilizable;
- Analytics/AdSense desaparecen;

restaurar inmediatamente el tema estable anterior y registrar el fallo antes de otra modificación.
