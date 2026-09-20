# TU PARTE — publicar AKG gratis en Cloudflare Pages

Todo el código ya está preparado. No necesitas editar nada en GitHub.

## 1. Crear o entrar en Cloudflare
Ve a https://dash.cloudflare.com/

Crea una cuenta gratuita o inicia sesión.

No añadas tarjeta y no contrates ningún plan de pago.

## 2. Crear el proyecto Pages
En Cloudflare:

1. Entra en **Workers & Pages**.
2. Pulsa **Create application** o **Create**.
3. Elige **Pages**.
4. Elige **Connect to Git** / **Import an existing Git repository**.
5. Autoriza GitHub cuando Cloudflare lo pida.

## 3. Elegir el repositorio
Selecciona:

`andrestruck15-eng/akg-photography`

Si GitHub pregunta qué repositorios puede leer Cloudflare, puedes autorizar únicamente este repositorio.

## 4. Nombre del proyecto
Prueba, por este orden:

1. `akgphotography`
2. `akgfotografia`
3. `akgphoto`

Cloudflare generará una URL como:

`https://akgphotography.pages.dev`

Si el primer nombre está ocupado, utiliza el siguiente.

## 5. Configuración de compilación
Pon exactamente:

- **Production branch:** `main`
- **Framework preset:** `None`
- **Build command:** `exit 0`
- **Build output directory:** `.`
- **Root directory:** déjalo vacío / raíz del repositorio

No añadas variables de entorno.

## 6. Publicar
Pulsa **Save and Deploy** / **Deploy**.

Cuando termine, Cloudflare te mostrará la dirección `*.pages.dev`.

## 7. Comprobar
Abre la URL que te dé Cloudflare.

Debes ver:
- AKG Photography
- portada clara
- Servicios
- Portfolio
- Tarifas
- Profesionales
- Guías
- Cobertura
- WhatsApp 691 357 701

## 8. Después
Envíame aquí únicamente la URL final que Cloudflare te haya dado, por ejemplo:

`https://akgphotography.pages.dev`

Con esa URL podré dejar preparado:
- sitemap definitivo
- robots.txt definitivo
- enlaces canónicos
- metadatos sociales
- estructura para Google Search Console
- enlace para Google Business Profile

## No hagas esto
- No compres un dominio.
- No contrates Cloudflare Pro.
- No pagues hosting.
- No cambies la rama `main`.
- No edites código manualmente.
