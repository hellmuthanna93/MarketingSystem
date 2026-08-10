/**
 * Anna Hellmuth design system - interactive components
 */
document.addEventListener('DOMContentLoaded', () => {
  setupStickyHeader();
  setupMobileMenu();
  setupSliders();
  setupSidebarNav();
});

function setupStickyHeader() {
  const header = document.querySelector('[data-ds-header]');
  if (!header) return;

  const threshold = 40;
  const onScroll = () => {
    header.classList.toggle('site-header--scrolled', window.scrollY > threshold);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

function setupMobileMenu() {
  const toggle = document.querySelector('[data-nav-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (!toggle || !menu) return;

  const links = menu.querySelectorAll('a');

  const setOpen = (open) => {
    menu.classList.toggle('open', open);
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-hidden', String(!open));
    document.body.style.overflow = open ? 'hidden' : '';
  };

  toggle.addEventListener('click', () => setOpen(!menu.classList.contains('open')));

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('open')) {
      setOpen(false);
      toggle.focus();
    }
  });

  links.forEach((link) => link.addEventListener('click', () => setOpen(false)));
}

function setupSliders() {
  document.querySelectorAll('[data-slider]').forEach((slider) => {
    const track = slider.querySelector('[data-slider-track]');
    const slides = slider.querySelectorAll('[data-slider-slide]');
    const prevBtn = slider.querySelector('[data-slider-prev]');
    const nextBtn = slider.querySelector('[data-slider-next]');
    const dotsHost = slider.querySelector('[data-slider-dots]');

    if (!track || slides.length === 0) return;

    let index = 0;

    const dots = [];
    if (dotsHost) {
      slides.forEach((_, i) => {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'slider-dot';
        dot.setAttribute('role', 'tab');
        dot.setAttribute('aria-label', `Slide ${i + 1} of ${slides.length}`);
        dot.setAttribute('aria-selected', i === 0 ? 'true' : 'false');
        dot.addEventListener('click', () => goTo(i));
        dotsHost.appendChild(dot);
        dots.push(dot);
      });
    }

    const update = () => {
      track.style.transform = `translateX(-${index * 100}%)`;
      slides.forEach((slide, i) => {
        slide.setAttribute('aria-hidden', i !== index ? 'true' : 'false');
      });
      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
        dot.setAttribute('aria-selected', i === index ? 'true' : 'false');
      });
      if (prevBtn) prevBtn.disabled = slides.length <= 1;
      if (nextBtn) nextBtn.disabled = slides.length <= 1;
    };

    const goTo = (i) => {
      index = (i + slides.length) % slides.length;
      update();
    };

    if (prevBtn) prevBtn.addEventListener('click', () => goTo(index - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => goTo(index + 1));

    slider.setAttribute('tabindex', '0');
    slider.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { e.preventDefault(); goTo(index + 1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); goTo(index - 1); }
    });

    update();
  });
}

function setupSidebarNav() {
  const links = document.querySelectorAll('.ds-sidebar a[href^="#"]');
  if (!links.length) return;

  const sections = [...links]
    .map((link) => document.querySelector(link.getAttribute('href')))
    .filter(Boolean);

  if (!sections.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.id;
        links.forEach((link) => {
          link.setAttribute('aria-current', link.getAttribute('href') === `#${id}` ? 'true' : null);
        });
      });
    },
    { rootMargin: '-20% 0px -60% 0px', threshold: 0 }
  );

  sections.forEach((section) => observer.observe(section));
}
