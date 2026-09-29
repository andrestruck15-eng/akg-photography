from pathlib import Path
import xml.etree.ElementTree as ET

src = Path("propietario-practico/blogger-migration/blogger-theme-optimized.xml")
dst = Path("propietario-practico/blogger-migration/blogger-theme-v3.xml")
text = src.read_text(encoding="utf-8")

marker = "/* PP-SINGLE-ARTICLE-HOTFIX-V3 */"
if marker not in text:
    css_anchor = "'.sidebar-container{display:none!important}',"
    css_extra = (
        "    '" + marker + "',\n"
        "    'body.item-view .FeaturedPost,.item-view .FeaturedPost{display:none!important}',\n"
        "    'body.item-view .sidebar-container,.item-view .sidebar-container{display:none!important}',\n"
        "    'body.item-view .PopularPosts,.item-view .PopularPosts{display:none!important}',"
    )
    if css_anchor not in text:
        raise SystemExit("Runtime CSS anchor not found")
    text = text.replace(css_anchor, css_anchor + "\n" + css_extra, 1)

    run_anchor = "function run(){"
    js_guard = """function wireConversionTracking(){
    if(document.documentElement.getAttribute('data-pp-tracking')==='1') return;
    document.documentElement.setAttribute('data-pp-tracking','1');
    document.addEventListener('click',function(ev){
      var a=ev.target && ev.target.closest ? ev.target.closest('a[href]') : null;
      if(!a) return;
      var href=a.href||'';
      if(href.indexOf('akg-photography.pages.dev')!==-1 && typeof window.gtag==='function'){
        window.gtag('event','akg_click',{link_url:href,link_text:(a.textContent||'').trim(),page_path:location.pathname});
      }
    },true);
  }
  function enforceSingleArticle(){
    var isArticle=/^\\/\\d{4}\\/\\d{2}\\//.test(location.pathname) || location.pathname.indexOf('/p/')===0;
    if(!isArticle) return;
    document.body.classList.add('item-view');
    document.querySelectorAll('.FeaturedPost,.sidebar-container,.PopularPosts').forEach(function(el){el.style.display='none';});
  }
  """
    if run_anchor not in text:
        raise SystemExit("run() anchor not found")
    text = text.replace(run_anchor, js_guard + run_anchor, 1)
    text = text.replace("function run(){\n", "function run(){\n    enforceSingleArticle();\n", 1)

internal_marker = "PP-STATIC-INTERNAL-LINKS"
if internal_marker not in text:
    anchor = "                </b:section>\n              </main>"
    block = """                </b:section>
                <b:if cond='data:view.isSingleItem'>
                  <section class='pp-discover' aria-label='Guías relacionadas'>
                    <div class='pp-discover-kicker'>PP-STATIC-INTERNAL-LINKS</div>
                    <h2>Sigue explorando</h2>
                    <div class='pp-discover-grid'>
                      <a href='/2026/09/como-hacer-fotos-de-un-piso-para-vender.html'>Cómo hacer fotos de un piso</a>
                      <a href='/2026/09/checklist-para-preparar-una-vivienda.html'>Checklist para preparar una vivienda</a>
                      <a href='/2026/09/home-staging-barato-mejorar-una.html'>Home staging barato</a>
                      <a href='/2026/09/fotografia-inmobiliaria-con-movil-guia.html'>Fotografía inmobiliaria con móvil</a>
                      <a href='/2026/09/como-mejorar-un-anuncio-de-airbnb-guia.html'>Cómo mejorar un anuncio de Airbnb</a>
                      <a href='/2026/09/cerradura-inteligente-para-airbnb-en.html'>Cerradura inteligente para Airbnb</a>
                    </div>
                  </section>
                </b:if>
              </main>"""
    if anchor not in text:
        raise SystemExit("Main closing anchor not found")
    text = text.replace(anchor, block, 1)

    css_anchor2 = "'.pp-legal p,.pp-legal li{color:#aaa99f!important;font-size:12px!important;line-height:1.65!important}',"
    css2 = (
        "    '.pp-discover{max-width:920px!important;margin:24px auto 0!important;padding:28px!important;background:var(--pp-paper)!important;border:1px solid var(--pp-line)!important;border-radius:22px!important}',\n"
        "    '.pp-discover-kicker{font-size:0!important;height:0!important;overflow:hidden!important}',\n"
        "    '.pp-discover h2{font-family:Georgia,\\\"Times New Roman\\\",serif!important;color:var(--pp-ink)!important;font-size:28px!important;margin:0 0 16px!important}',\n"
        "    '.pp-discover-grid{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:10px!important}',\n"
        "    '.pp-discover-grid a{display:block!important;padding:13px 15px!important;background:var(--pp-sage)!important;color:var(--pp-dark)!important;border-radius:12px!important;text-decoration:none!important;font-weight:800!important}',\n"
        "    '@media(max-width:680px){.pp-discover-grid{grid-template-columns:1fr!important}}',"
    )
    if css_anchor2 not in text:
        raise SystemExit("Legal CSS anchor not found")
    text = text.replace(css_anchor2, css_anchor2 + "\n" + css2, 1)

dst.write_text(text, encoding="utf-8")
ET.parse(dst)

required = [
    "PP-SINGLE-ARTICLE-HOTFIX-V3",
    "enforceSingleArticle",
    "id='Blog1'",
    "type='Blog'",
    "pp-runtime-styles",
    "PP-STATIC-INTERNAL-LINKS",
    "pp-discover-grid",
    "AKG-CTA-TRACKING",
    "akg_click",
]
for item in required:
    if item not in text:
        raise SystemExit(f"Missing required marker: {item}")

print(f"Built and validated {dst}")
