# On-page audit — Propietario Práctico

Actualizado: 2026-09-29

## Canonicals
Comprobación live de las 13 entradas:
- las 13 devuelven canonical hacia su propia URL de Blogger;
- no se detectó canonical apuntando al antiguo dominio Cloudflare;
- no cambiar las URLs actuales.

## Longitud de títulos live
- Precio de fotógrafo inmobiliario en Valencia en 2026 — 52
- Checklist para preparar una vivienda antes de hacer fotos — 57
- Cerradura inteligente para Airbnb en España: guía 2026 — 54
- Fotografía para Airbnb en Valencia: qué debe incluir — 52
- Cómo mejorar un anuncio de Airbnb: guía práctica 2026 — 53
- Fotos para Airbnb y Booking: guía para propietarios en 2026 — 59
- Fotografía inmobiliaria con móvil: guía práctica 2026 — 53
- Qué comprar para preparar un piso para fotos sin gastar de más — 62
- Cómo fotografiar un apartamento pequeño sin deformarlo — 54
- 10 errores en fotografía inmobiliaria que empeoran un anuncio — 61
- Caja de llaves o cerradura inteligente para Airbnb: comparativa — 63
- Home staging barato: mejorar una vivienda sin reformar — 54
- Cómo hacer fotos de un piso para vender o alquilar — 50

### Títulos a revisar por longitud / foco
No es necesario cambiar URL.
1. Qué comprar para preparar un piso para fotos sin gastar de más
   - opción futura: "Qué comprar para preparar un piso para hacer fotos"
2. 10 errores en fotografía inmobiliaria que empeoran un anuncio
   - opción futura: "10 errores de fotografía inmobiliaria que empeoran tu anuncio"
3. Caja de llaves o cerradura inteligente para Airbnb: comparativa
   - opción futura: "Caja de llaves vs cerradura inteligente para Airbnb"

No hacer cambios masivos de títulos mientras la indexación inicial siga débil.

## Problema crítico de página individual
Auditoría con navegador renderizado en:
`/2026/09/como-hacer-fotos-de-un-piso-para-vender.html`

Resultado:
- FeaturedPost ajeno aparece antes del artículo objetivo.
- Se ven dos H1 en el contenido principal.
- El FeaturedPost incluye "Publicar un comentario".
- Sidebar muestra Profile, Archive, Labels, PopularPosts y ReportAbuse.
- PopularPosts introduce más títulos H1 ajenos.
- El cuerpo del artículo objetivo está completo.

## Remediación
Tema V3 generado y validado:
- fuerza clase item-view por pathname;
- oculta FeaturedPost en artículo/página;
- oculta sidebar y PopularPosts en artículo/página;
- conserva Blog1, Analytics, AdSense, privacidad/cookies y runtime styling.

Estado: preparado; pendiente de subir a Blogger para afectar producción.

## Contenido
Los 13 artículos actuales:
- 463–664 palabras;
- 1 imagen cada uno;
- alt presente;
- CTA AKG presente;
- enlazado interno muy débil: 11/13 sin links internos.

Prioridad editorial:
1. arreglar plantilla individual;
2. reforzar enlaces internos;
3. abrir alquiler residencial y venta;
4. ampliar piezas actuales solo donde Search Console muestre impresiones/intención.
