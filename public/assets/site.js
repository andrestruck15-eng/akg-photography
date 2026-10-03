// AKG Photography: navigation, consent and analytics
const GA_ID='G-7888FPYJP1';
const internalTest=new URLSearchParams(window.location.search).get('akg_test')==='1';
let analyticsEnabled=false;

window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}

function loadAnalytics(){
  if(analyticsEnabled) return;
  analyticsEnabled=true;
  gtag('js',new Date());
  gtag('config',GA_ID,{anonymize_ip:true});
  const gaScript=document.createElement('script');
  gaScript.async=true;
  gaScript.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA_ID);
  document.head.appendChild(gaScript);
}

function clearAnalyticsCookies(){
  document.cookie.split(';').forEach(raw=>{
    const name=raw.split('=')[0].trim();
    if(name==='_ga' || name.startsWith('_ga_')){
      document.cookie=name+'=; Max-Age=0; path=/; SameSite=Lax';
      document.cookie=name+'=; Max-Age=0; path=/; domain='+location.hostname+'; SameSite=Lax';
    }
  });
}

function getConsent(){
  try{return localStorage.getItem('akg_cookie_consent');}catch(_){return null;}
}
function setConsent(value){
  try{localStorage.setItem('akg_cookie_consent',value);}catch(_){}
}

function cookieBanner(){
  let el=document.getElementById('cookieBanner');
  if(el) return el;
  el=document.createElement('div');
  el.id='cookieBanner';
  el.className='cookie-banner';
  el.setAttribute('role','dialog');
  el.setAttribute('aria-live','polite');
  el.setAttribute('aria-label','Preferencias de cookies');
  el.innerHTML='<div class="cookie-banner__inner"><div><strong>Cookies y analítica</strong><p>Usamos cookies analíticas de Google Analytics solo si las aceptas. Sirven para medir visitas y mejorar la web. Puedes aceptar o rechazar con la misma facilidad.</p><a href="/cookies/">Más información</a></div><div class="cookie-banner__actions"><button type="button" class="cookie-btn" data-cookie-reject>Rechazar</button><button type="button" class="cookie-btn" data-cookie-accept>Aceptar</button></div></div>';
  document.body.appendChild(el);
  el.querySelector('[data-cookie-accept]').addEventListener('click',()=>{
    setConsent('accepted');
    loadAnalytics();
    el.remove();
  });
  el.querySelector('[data-cookie-reject]').addEventListener('click',()=>{
    setConsent('rejected');
    clearAnalyticsCookies();
    el.remove();
  });
  return el;
}

function openCookieSettings(){
  const current=document.getElementById('cookieBanner');
  if(current) current.remove();
  cookieBanner();
}

const consent=getConsent();
if(internalTest){
  clearAnalyticsCookies();
}else if(consent==='accepted') loadAnalytics();
else if(consent==='rejected') clearAnalyticsCookies();
else cookieBanner();

document.addEventListener('click',e=>{
  const settings=e.target.closest('[data-cookie-settings]');
  if(settings){
    e.preventDefault();
    openCookieSettings();
    return;
  }

  const a=e.target.closest('a');
  if(!a || !analyticsEnabled) return;
  const href=a.getAttribute('href')||'';
  if(href.startsWith('https://wa.me/')) gtag('event','whatsapp_click',{link_url:a.href,link_text:(a.textContent||'').trim(),page_location:window.location.href});
  else if(href.startsWith('tel:')) gtag('event','phone_click',{link_url:a.href,link_text:(a.textContent||'').trim(),page_location:window.location.href});
  else if(href==='/contacto/' || /presupuesto/i.test((a.textContent||''))) gtag('event','quote_click',{link_url:a.href,link_text:(a.textContent||'').trim(),page_location:window.location.href});
});

const m=document.getElementById('menuBtn'),n=document.getElementById('navLinks');
if(m&&n){
  m.addEventListener('click',()=>{
    const o=n.classList.toggle('open');
    m.setAttribute('aria-expanded',o?'true':'false');
  });
  n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
    n.classList.remove('open');
    m.setAttribute('aria-expanded','false');
  }));
}
document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
