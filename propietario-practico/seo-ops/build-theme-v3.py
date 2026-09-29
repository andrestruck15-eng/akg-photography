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
    js_guard = """function enforceSingleArticle(){
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

dst.write_text(text, encoding="utf-8")
ET.parse(dst)

required = [
    "PP-SINGLE-ARTICLE-HOTFIX-V3",
    "enforceSingleArticle",
    "id='Blog1'",
    "type='Blog'",
    "pp-runtime-styles",
]
for item in required:
    if item not in text:
        raise SystemExit(f"Missing required marker: {item}")

print(f"Built and validated {dst}")
