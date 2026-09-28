// Google Analytics 4
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}
gtag('js',new Date());
gtag('config','G-7888FPYJP1');
const gaScript=document.createElement('script');
gaScript.async=true;
gaScript.src='https://www.googletagmanager.com/gtag/js?id=G-7888FPYJP1';
document.head.appendChild(gaScript);
const m=document.getElementById('menuBtn'),n=document.getElementById('navLinks');if(m&&n){m.addEventListener('click',()=>{const o=n.classList.toggle('open');m.setAttribute('aria-expanded',o?'true':'false')});n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{n.classList.remove('open');m.setAttribute('aria-expanded','false')}));}document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
