document.addEventListener('DOMContentLoaded', () => {
  setupThemeToggle();
  setupStickyHeader();
  setupMobileMenu();
  setupAboutSlider();
  setupScrollReveal();
});

/**
 * Light / dark theme toggle.
 * The saved preference is applied pre-paint by a tiny inline <head> script;
 * here we build the control and let the visitor switch and persist it.
 */
function setupThemeToggle() {
  const root = document.documentElement;
  const media = window.matchMedia('(prefers-color-scheme: dark)');

  const readStored = () => {
    try {
      return localStorage.getItem('theme');
    } catch (e) {
      return null;
    }
  };

  const effectiveTheme = () => {
    const stored = readStored();
    if (stored === 'dark' || stored === 'light') return stored;
    return media.matches ? 'dark' : 'light';
  };

  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'theme-toggle';
  button.innerHTML = `
    <svg class="icon-moon" aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
    </svg>
    <svg class="icon-sun" aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="4"></circle>
      <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"></path>
    </svg>`;

  const body = document.body;
  const labelLight = body.dataset.themeLabelLight || 'Switch to light theme';
  const labelDark = body.dataset.themeLabelDark || 'Switch to dark theme';

  const syncLabel = () => {
    const isDark = effectiveTheme() === 'dark';
    button.setAttribute('aria-label', isDark ? labelLight : labelDark);
    button.setAttribute('aria-pressed', String(isDark));
  };

  button.addEventListener('click', () => {
    const next = effectiveTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try {
      localStorage.setItem('theme', next);
    } catch (e) {
      /* storage unavailable — toggle still applies for this session */
    }
    syncLabel();
  });

  // Keep an unset (system-driven) preference in sync if the OS theme changes.
  media.addEventListener('change', () => {
    if (!readStored()) syncLabel();
  });

  syncLabel();
  document.body.appendChild(button);
}

/**
 * Sticky Header on Scroll
 */
function setupStickyHeader() {
  const header = document.querySelector('header');
  const scrollThreshold = 50;

  function checkScroll() {
    if (window.scrollY > scrollThreshold) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  // Initial check
  checkScroll();
  window.addEventListener('scroll', checkScroll);
}

/**
 * Mobile Navigation Toggle Menu
 */
function setupMobileMenu() {
  const navToggle = document.querySelector('.nav-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileMenuLinks = document.querySelectorAll('.mobile-menu-links a');

  if (!navToggle || !mobileMenu) return;

  const navLabel = document.body.dataset.navLabel || 'Toggle navigation';
  navToggle.setAttribute('aria-label', navLabel);

  function setMenuOpen(isOpen) {
    mobileMenu.classList.toggle('open', isOpen);
    navToggle.classList.toggle('open', isOpen);
    navToggle.setAttribute('aria-expanded', String(isOpen));
    mobileMenu.setAttribute('aria-hidden', String(!isOpen));
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }

  function toggleMenu() {
    setMenuOpen(!mobileMenu.classList.contains('open'));
  }

  navToggle.addEventListener('click', toggleMenu);

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && mobileMenu.classList.contains('open')) {
      setMenuOpen(false);
      navToggle.focus();
    }
  });

  mobileMenuLinks.forEach(link => {
    link.addEventListener('click', () => setMenuOpen(false));
  });
}

/**
 * About page hypnotherapy testimonials slider (#about-slider only)
 */
function setupAboutSlider() {
  const slider = document.getElementById('about-slider');
  if (!slider) return;

  const track = slider.querySelector('.testimonials-track');
  const slides = slider.querySelectorAll('.testimonial-slide');
  const prevBtn = slider.querySelector('.slider-btn.prev');
  const nextBtn = slider.querySelector('.slider-btn.next');
  const dotsContainer = slider.querySelector('.slider-dots');

  if (!track || slides.length === 0 || !dotsContainer) return;

  let currentIndex = 0;
  const totalSlides = slides.length;

  // Create dot indicators
  slides.forEach((_, index) => {
    const dot = document.createElement('button');
    dot.classList.add('slider-dot');
    if (index === 0) dot.classList.add('active');
    dot.setAttribute('aria-label', `Go to testimonial slide ${index + 1}`);
    dot.addEventListener('click', () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });

  const dots = slider.querySelectorAll('.slider-dot');

  function updateSlider() {
    // Translate the track by index
    track.style.transform = `translateX(-${currentIndex * 100}%)`;
    
    // Update dots
    dots.forEach((dot, index) => {
      if (index === currentIndex) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  function goToSlide(index) {
    currentIndex = index;
    updateSlider();
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlider();
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateSlider();
  }

  // Click events
  if (nextBtn) nextBtn.addEventListener('click', nextSlide);
  if (prevBtn) prevBtn.addEventListener('click', prevSlide);

  // Auto slide option (runs every 8 seconds)
  let autoSlideTimer = setInterval(nextSlide, 8000);

  const stopAutoSlide = () => {
    clearInterval(autoSlideTimer);
    autoSlideTimer = setInterval(nextSlide, 12000);
  };

  if (nextBtn) nextBtn.addEventListener('click', stopAutoSlide);
  if (prevBtn) prevBtn.addEventListener('click', stopAutoSlide);
  dots.forEach(dot => dot.addEventListener('click', stopAutoSlide));

  slider.setAttribute('tabindex', '0');
  slider.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') {
      event.preventDefault();
      stopAutoSlide();
      nextSlide();
    } else if (event.key === 'ArrowLeft') {
      event.preventDefault();
      stopAutoSlide();
      prevSlide();
    }
  });

  // Touch Swipe support for Mobile
  let startX = 0;
  let endX = 0;

  track.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
  }, { passive: true });

  track.addEventListener('touchend', (e) => {
    endX = e.changedTouches[0].clientX;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const diff = startX - endX;
    const swipeThreshold = 50; // pixels

    if (Math.abs(diff) > swipeThreshold) {
      stopAutoSlide();
      if (diff > 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
  }
}

/**
 * Fade-in sections and staggered children on scroll
 */
function setupScrollReveal() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const main = document.querySelector('main');
  if (!main) return;

  const childSelectors = [
    '.service-card',
    '.testimonial-card',
    '.about-card',
    '.step-circle',
    '.step-card',
    '.eye-card',
    '.pricing-card',
    '.accordion-item',
    '.personal-gallery-img',
    '.contact-prompt',
    '.assessment-panel',
    '.opportunity-card',
    '.opportunity-list li'
  ].join(', ');

  const sections = main.querySelectorAll('section');
  const revealTargets = [];

  if (main.classList.contains('legal-content')) {
    main.classList.add('reveal');
    revealTargets.push(main);
  }

  sections.forEach((section) => {
    section.classList.add('reveal');

    const children = section.querySelectorAll(childSelectors);
    children.forEach((child, index) => {
      child.classList.add('reveal-child');
      child.style.setProperty('--reveal-delay', `${Math.min(index * 0.07, 0.42)}s`);
    });

    revealTargets.push(section);
  });

  const pageHeader = main.querySelector('.page-header');
  if (pageHeader) {
    pageHeader.classList.add('reveal');
    revealTargets.push(pageHeader);
  }

  if (prefersReducedMotion) {
    revealTargets.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  const hero = main.querySelector('.hero');
  if (hero) {
    requestAnimationFrame(() => hero.classList.add('is-visible'));
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    },
    {
      threshold: 0.1,
      rootMargin: '0px 0px -5% 0px'
    }
  );

  revealTargets.forEach((el) => {
    if (el === hero) return;
    observer.observe(el);
  });
}
