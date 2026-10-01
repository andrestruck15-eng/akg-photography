# Propietario Práctico — SEO Operations

Actualizado: 2026-09-29

## Objetivo
Construir Propietario Práctico como publicación SEO para propietarios en España, monetizando primero con AdSense y leads hacia AKG Photography, y más adelante con afiliación. Presupuesto: 0 €.

## Estado verificado
- Producción: https://proprietariopractico.blogspot.com/
- 13 artículos publicados.
- Sitemap de Blogger accesible.
- ads.txt válido para pub-2762317170112827.
- AdSense: revisión iniciada el 28/09/2026.
- Portada y artículos funcionan.
- Imágenes temáticas corregidas en la capa visual del tema.
- Privacidad/cookies visibles.
- El último arreglo runtime CSS está preparado en GitHub pero todavía no está activo en Blogger.
- Search Console de Propietario Práctico ya está verificada: https://proprietariopractico.blogspot.com/. Sitemap enviado con estado Correcto y 13 URLs descubiertas. El informe de indexación aún está procesando datos.
- GA4 de Propietario Práctico recibió datos en tiempo real antes del último cambio de tema, pero debe volver a verificarse después de estabilizar el tema.

## Auditoría de los 13 artículos live
Rango de longitud: 463–664 palabras.
Todos tienen una imagen con alt.
Todos contienen CTA a AKG.
Debilidad principal: 11/13 artículos tienen 0 enlaces internos a otras guías de Propietario Práctico; solo 2 tienen 1 enlace interno.
Cobertura temática:
- Airbnb: 5
- Fotografía: 4
- Preparación: 3
- Valencia/local: 1
- Venta de vivienda: 0 piezas específicas
- Alquiler residencial para propietarios: 0 piezas específicas
- Gestión del propietario: 0 piezas específicas
- Equipamiento fuera de acceso Airbnb: prácticamente 0

## Hallazgos competitivos
### Idealista / Fotocasa
Fortaleza: gran cobertura de las decisiones del propietario antes, durante y después de vender/alquilar.
Huecos que PP debe cubrir:
- poner un piso en alquiler paso a paso
- vender un piso entre particulares
- documentación para vender
- preparar vivienda para alquilar
- anuncio de alquiler
- selección y gestión práctica del inquilino (con cuidado legal)
- inventario y entrega de vivienda

### Lodgify / Avaibook
Fortaleza: profundidad operativa en alquiler vacacional.
Huecos que PP debe cubrir:
- check-in autónomo
- guía de bienvenida
- equipamiento práctico
- protección del alojamiento
- costes y rentabilidad (solo con fuentes actuales)
- regulación/registro: únicamente con fuentes oficiales actualizadas

## Oportunidad SEO prioritaria
La búsqueda exacta "preparar piso para alquilar" muestra mucha menos saturación visible que los grandes términos genéricos de venta/alquiler. Se prioriza como primera pieza del nuevo cluster.

## Arquitectura objetivo
1. Vender vivienda
2. Alquiler residencial
3. Alquiler vacacional
4. Fotografía
5. Preparación / Home staging
6. Equipamiento
7. Gestión del propietario
8. Normativa (solo con fuentes oficiales)

## Prioridad de ejecución
P0
- Publicar/validar el tema final estable.
- Verificar Analytics después del tema.
- Revisar Pages/Indexing e inspección de URLs cuando Search Console termine de procesar los datos iniciales.
- Incrementar enlazado interno de las 13 entradas.

P1
- Abrir cluster "Alquiler residencial".
- Abrir cluster "Vender vivienda".
- Publicar piezas de intención práctica antes de contenido legal complejo.

P2
- Afiliación de equipamiento cuando exista cuenta.
- Medir clics PP -> AKG.
- Crear páginas locales solo cuando tengan contenido diferenciable real.

## Próximas piezas
1. Cómo preparar un piso para alquilar: checklist completo
2. Cómo poner un piso en alquiler: guía para propietarios
3. Cómo hacer un anuncio de alquiler que reciba mejores contactos
4. Qué revisar antes de entregar un piso en alquiler
5. Cómo vender un piso entre particulares: pasos y documentos
6. Documentos para vender una vivienda en España
7. Qué fotos poner en Idealista para vender o alquilar
8. Caja de llaves para Airbnb: qué mirar antes de comprar
9. Check-in autónomo para Airbnb: opciones y errores
10. Guía de bienvenida para huéspedes: qué incluir

## Regla editorial
- No inventar autoridad ni experiencia profesional.
- Separar claramente información práctica de información legal/fiscal.
- Temas normativos, fiscales o registrales: revisar fuentes oficiales vigentes antes de publicar.
- Evitar artículos masivos finos; priorizar utilidad, navegación e intención concreta.
- Cada nueva pieza debe enlazar como mínimo 3 guías internas relevantes y recibir enlaces desde 2 piezas existentes.

## Siguiente punto exacto
Crear el nuevo cluster de Alquiler residencial empezando por "Cómo preparar un piso para alquilar", seguido de "Cómo poner un piso en alquiler", y diseñar el mapa de enlaces internos entre las 13 piezas actuales y las nuevas.


## Actualización 2026-09-29 21:xx — trabajo continuo

### Crawlabilidad verificada
- robots.txt live permite rastreo general y bloquea /search y /share-widget.
- robots.txt declara correctamente sitemap.xml.
- sitemap.xml live contiene 13 URLs de artículos.
- Canonical comprobado en artículo de muestra apunta a su URL Blogger correcta.
- Consulta pública `site:proprietariopractico.blogspot.com`: solo 1 resultado visible (portada) en la comprobación actual.

### Hallazgo crítico de plantilla
En una URL individual de artículo se comprobó con navegador renderizado:
- aparece un FeaturedPost de "Precio de fotógrafo inmobiliario en Valencia en 2026" ANTES del artículo solicitado;
- existen dos H1 principales visibles en la zona de contenido;
- el FeaturedPost muestra además enlace de comentarios;
- la sidebar incluye PopularPosts y otros widgets;
- el cuerpo del artículo objetivo sí está completo.

Impacto:
- mala UX;
- dilución de intención de página;
- múltiples H1 no deseados;
- riesgo de señales de relevancia confusas para rastreo/indexación.

Solución preparada:
- build-theme-v3.py
- workflow Build Blogger theme v3
- artefacto V3 validado con éxito.
- V3 fuerza en artículos: ocultar FeaturedPost, sidebar y PopularPosts y conservar Blog1.
- Todavía requiere subir el XML V3 a Blogger para afectar producción.

### Contenido preparado
Borradores completos:
1. Cómo preparar un piso para alquilar: checklist completo 2026
2. Cómo hacer un anuncio de alquiler que reciba mejores contactos
3. Qué fotos poner en Idealista para vender o alquilar un piso

### Prioridad inmediata revisada
P0.1 — Subir y validar V3 para eliminar contenido duplicado en artículos.
P0.2 — Confirmar Search Console Blogger y estado real de indexación.
P0.3 — Implementar enlaces internos en los 13 artículos.
P1 — Publicar cluster de alquiler residencial de forma gradual, no masiva.


## Producción Blogger — 2026-09-29 noche
- Sesión autenticada de Blogger confirmada para Propietario Práctico.
- Tema actual: Contempo Light, estado modificado.
- Featured Post y Popular Posts ocultados desde Diseño mediante "Mostrar este widget" = desactivado.
- Cambio reversible; no se eliminaron posts ni gadgets.
- Validación pública: el artículo "Cómo hacer fotos de un piso para vender o alquilar" ya no muestra otro artículo por encima ni Popular Posts.
- Home sigue cargando correctamente.
- AdSense, navegación, footer y banner de consentimiento siguen visibles.


## Ajustes SEO Blogger — 2026-09-29 noche
- Descripción del blog actualizada a: "Guías prácticas para vender, alquilar, preparar y gestionar mejor una vivienda en España."
- Search description activada y configurada.
- Google Analytics ID confirmado en Blogger: G-6RSQYHEC5G.
- HTTPS redirect activo.
- Visible para buscadores: activo.
- ads.txt personalizado activo con pub-2762317170112827.
- Enlace/recuento de comentarios ocultado del feed.
- Privacidad y Política de cookies existen como páginas publicadas.
- También existen dos duplicados programados de las páginas legales; no se han eliminado todavía para evitar cambios destructivos.
- Auditoría visual: hero, navegación y tarjetas de rutas visibles; feed de posts sigue en una sola columna; sidebar visible; footer legal visible.


## Validación final — 2026-09-30 07:45 CEST

### Producción verificada con navegador renderizado
- Home pública carga correctamente; navegación principal operativa: Inicio, Fotografía, Airbnb, Preparación, Sobre y AKG Photography.
- Artículo nuevo «Cómo preparar un piso para alquilar: checklist completo 2026» ya renderiza correctamente en producción: H1/H2/H3, imagen y cuerpo visibles; el HTML escapado detectado en ciclos anteriores ya no aparece como markup literal dentro del cuerpo. P0 del cuerpo del artículo: RESUELTO.
- Muestra amplia revalidada: Checklist para preparar una vivienda, Precio de fotógrafo inmobiliario y Fotografía para Airbnb en Valencia cargan sin error; headings de artículos coherentes.
- robots.txt live: PASS. Permite raíz, bloquea /search y /share-widget y declara sitemap.xml.
- sitemap.xml live: PASS, XML válido con 14 URLs.
- Navegación interna: páginas de etiquetas Fotografía/Airbnb/Preparación, archivo y buscador funcionan.
- Página Sobre: PASS, contenido estructurado y sin HTML literal.
- Información legal de privacidad/cookies visible en footer: PASS.
- Imágenes de la muestra cargan correctamente.

### Defectos / pendientes confirmados
- Home: algunos snippets muestran entidades/markup escapado (por ejemplo figure/img) en la previsualización. Defecto menor pero visible; no se ha aplicado un cambio destructivo sin aislar antes el origen del snippet.
- Home: H1 estructural «Brand» no es descriptivo. Pendiente de corrección segura en tema.
- Responsive 3/2/1: no se pudo hacer emulación real de viewport en esta pasada. V3 sigue preparado en GitHub; no marcar como desplegado sin evidencia.
- Canonical: la pasada renderizada no lo expuso de forma verificable. Se conserva como PASS histórico en las 13 legacy por LIVE-AUDIT-LATEST.md y queda pendiente revalidación específica del artículo nuevo.
- Meta descriptions legacy y enlazado interno siguen siendo P1; no confundir con fallos de disponibilidad.

### Correcciones realizadas en esta validación
- Ningún cambio inseguro en Blogger. Se actualizó la matriz de estado para retirar el falso P0 del cuerpo escapado del artículo nuevo, ya que producción lo renderiza correctamente.
- Se mantiene el principio de no desplegar CSS/tema nuevo sin validación posterior de regresión.

### Bloqueos externos / límites
- El fetch web textual directo de Blogspot volvió a rechazar las URLs, pero el navegador renderizado sí accedió y permitió validar producción.
- No se usó ningún servicio de pago ni se contrató nada.

### Siguiente punto exacto
1. Corregir de forma aislada los snippets escapados de la home y el H1 «Brand» en el tema, con rollback claro.
2. Desplegar/validar V3 solo cuando pueda comprobarse 3 columnas desktop / 2 tablet / 1 móvil y ausencia de overflow.
3. Revalidar canonical del artículo nuevo y aplicar el plan de enlazado interno.


## Validación final — 2026-10-01 07:45 CEST

### Evidencia nocturna leída
- Revisados STATUS.md y commits nocturnos: 8a6f519, d807f2e, 06c1905, a7cdb42 y auditoría automática 0aca291.
- No hubo despliegue confirmado del V3 durante la noche. V3 sigue validado solo en fuente: grid 3 columnas desktop, 2 <=980px, 1 <=680px; cards flex de altura uniforme; thumbnails con object-fit/overflow controlado.
- El artículo «Cómo preparar un piso para alquilar» permanece RESUELTO según la última validación renderizada fiable; no reabrir el falso P0 histórico de HTML escapado.

### Crawl / canonical
- La auditoría automática de 05:34 UTC obtuvo robots.txt=200 y sitemap.xml=200, pero 10 de 13 URLs legacy devolvieron HTTP 429 durante el crawl. Tres URLs sí devolvieron 200 y canonical propio.
- Los 429 se clasifican como rate limiting del crawl, NO como evidencia de caída ni de canonical roto. La auditoría anterior había obtenido 13/13 legacy con HTTP 200 + canonical propio.
- Por tanto, canonical de las URLs con 429 queda NO REVALIDADO en esta pasada, no FAIL. No se hará recrawl agresivo para evitar empeorar el rate limit.
- Canonical del artículo nuevo sigue pendiente de una comprobación específica fiable.

### Producción / visual
- No se ha obtenido una nueva sesión renderizada fiable en esta pasada: el acceso textual público a Blogspot está bloqueado desde el entorno y la auditoría automática está parcialmente limitada por 429.
- Se conserva la última evidencia renderizada válida: home y navegación cargaban; páginas Sobre/legales y muestra amplia de posts funcionaban; imágenes/headings correctos; robots/sitemap PASS; cuerpo del artículo nuevo sin HTML literal.
- P0 visual todavía abierto y no debe declararse corregido: snippets escapados en home, H1 estructural «Brand» y falta de prueba real 3/2/1 + overflow en producción.

### Cambios seguros
- No se modificó Blogger ni se desplegó V3 a ciegas.
- No se contrató ni utilizó ningún servicio de pago.
- Se corrige la interpretación de LIVE-AUDIT-LATEST: HTTP 429 no equivale a canonical NO; significa que la respuesta no permitió verificarlo.

### Bloqueo mínimo / siguiente acción
1. Cuando haya navegador Blogger/render fiable, aislar el nodo que genera «Brand» y los snippets escapados; aplicar únicamente el parche reversible correspondiente.
2. Validar home en desktop/tablet/móvil (3/2/1), overflow, cards, imágenes y navegación inmediatamente después del cambio.
3. Hacer una única comprobación del canonical del artículo nuevo y, tras disiparse el rate limit, recrawl espaciado de las URLs que dieron 429.
4. Después cerrar P0 y aplicar los tres enlaces entrantes preparados hacia el artículo de alquiler.
