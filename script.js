const header = document.getElementById('header');
const menuButton = document.getElementById('menuButton');
const mobileNav = document.getElementById('mobileNav');

window.addEventListener('scroll', () => {
  header.classList.toggle('is-scrolled', window.scrollY > 24);
}, { passive: true });

menuButton?.addEventListener('click', () => {
  const open = mobileNav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
});

mobileNav?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    mobileNav.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
  });
});

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', (event) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    event.preventDefault();
    const y = target.getBoundingClientRect().top + window.scrollY - 82;
    window.scrollTo({ top: y, behavior: 'smooth' });
  });
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('visible');
    observer.unobserve(entry.target);
  });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.target-card,.field-card,.profile-panel,.profile-card,.career-card,.method-list li,.course-card,.contact-list div,.contact-note,.section-heading').forEach((el, index) => {
  el.classList.add('fade-up');
  el.style.transitionDelay = `${Math.min(index * 25, 180)}ms`;
  observer.observe(el);
});
