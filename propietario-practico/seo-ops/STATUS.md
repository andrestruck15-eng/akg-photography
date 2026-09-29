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
- Search Console específica de Propietario Práctico todavía requiere verificación/confirmación operativa.
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
- Dar de alta/verificar la propiedad Blogger en Search Console y sitemap.
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
