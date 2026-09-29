# Indexación — Propietario Práctico

Actualizado: 2026-09-29

## Evidencia pública
Consulta Google: site:proprietariopractico.blogspot.com
Resultado visible en la comprobación: 1 URL, la portada.

Interpretación operativa:
- No asumir que los 13 artículos están indexados.
- Priorizar descubrimiento e indexación antes de escalar fuerte la producción.
- El sitemap de Blogger está accesible en /sitemap.xml.
- Las URLs canónicas de los artículos live apuntan a Blogger.

## Estado real en Search Console — 2026-09-29
- Propiedad URL-prefix verificada y seleccionada: https://proprietariopractico.blogspot.com/
- Sitemap enviado: sitemap.xml
- Estado del sitemap: Correcto
- URLs descubiertas por sitemap: 13
- Fecha de envío: 2026-09-29
- Informe de indexación: todavía procesando datos; Search Console pide volver a comprobar mañana.
- Inspección individual: todavía sin datos utilizables mientras termina el procesamiento inicial.
- Solicitudes de indexación: no realizadas todavía; esperar a disponer de estado real por URL.

## Acción prioritaria en Search Console
Esperar a que termine el procesamiento inicial y después inspeccionar portada + URLs representativas antes de solicitar indexación manual.

## Comprobaciones después del alta
1. Verificar que Search Console acepta la propiedad.
2. Enviar sitemap.xml una sola vez.
3. Inspeccionar portada + 3 artículos representativos:
   - precio fotógrafo inmobiliario Valencia
   - cómo hacer fotos de un piso
   - cerradura inteligente Airbnb
4. Registrar si cada URL aparece como:
   - indexada
   - descubierta/no indexada
   - rastreada/no indexada
   - no descubierta
5. No solicitar indexación masiva de las 13 URLs a ciegas; usar la inspección para diagnosticar primero.
6. Volver a revisar impresiones y páginas indexadas tras varios días.

## Señales internas que ayudan
- Añadir 3–5 enlaces internos por artículo.
- Evitar páginas huérfanas.
- Mantener sitemap y canonical estables.
- No cambiar URLs de los 13 artículos.
- No duplicar el contenido en Cloudflare; mantener los 301 existentes.
- Publicar nuevas piezas dentro de clusters y enlazarlas desde contenido existente.

## Qué NO hacer
- No crear sitemaps alternativos innecesarios para Blogger.
- No volver a publicar los mismos 13 artículos con nuevas URLs.
- No romper la redirección desde propietario-practico.pages.dev.
- No generar decenas de artículos finos mientras la indexación base no esté verificada.

## Siguiente paso
Cuando Search Console termine de procesar datos, revisar Pages/Indexing, inspeccionar 4 URLs representativas y solicitar indexación solo para las que aparezcan explícitamente como no indexadas.


## Verificación adicional 2026-09-29
- El HTML live de la página "Sobre Propietario Práctico" contiene meta `google-site-verification` con el token configurado.
- El sitemap live responde HTTP 200 y lista las 13 entradas.
- robots.txt responde HTTP 200, permite la raíz y declara sitemap.xml.
- Las 13 URLs auditadas responden HTTP 200 y canonical propio.
- Esto deja la web técnicamente preparada para verificación de propiedad; todavía debe comprobarse dentro de la cuenta de Search Console si la propiedad Blogger está creada y qué estado de indexación registra.
- No volver a enviar sitemap si ya figura como "Correcto"; primero consultar cobertura/inspección.
