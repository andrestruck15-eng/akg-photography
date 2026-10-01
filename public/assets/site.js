// Google Analytics 4
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}
gtag('js',new Date());
gtag('config','G-7888FPYJP1');

const gaScript=document.createElement('script');
gaScript.async=true;
gaScript.src='https://www.googletagmanager.com/gtag/js?id=G-7888FPYJP1';
document.head.appendChild(gaScript);

function trackLead(eventName,link){
  gtag('event',eventName,{
    link_url:link.href,
    link_text:(link.textContent||'').trim(),
    page_location:window.location.href
  });
}

document.addEventListener('click',e=>{
  const a=e.target.closest('a');
  if(!a) return;
  const href=a.getAttribute('href')||'';
  if(href.startsWith('https://wa.me/')) trackLead('whatsapp_click',a);
  else if(href.startsWith('tel:')) trackLead('phone_click',a);
  else if(href==='/contacto/' || /presupuesto/i.test((a.textContent||''))) trackLead('quote_click',a);
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
