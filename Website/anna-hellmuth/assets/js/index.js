document.addEventListener('DOMContentLoaded', () => {
  setupStickyHeader();
  setupMobileMenu();
  setupAboutSlider();
  setupChapterSupportDialogs();
  setupNextChapterReliefTiles();
  setupCounselingOutcomesExpansion();
  setupScrollReveal();
});

/**
 * Sticky Header on Scroll
 */
function setupStickyHeader() {
  const header = document.querySelector('header');
  if (!header) return;

  const sentinel = document.createElement('span');
  sentinel.className = 'header-scroll-sentinel';
  sentinel.setAttribute('aria-hidden', 'true');
  document.body.prepend(sentinel);

  const observer = new IntersectionObserver(
    ([entry]) => header.classList.toggle('scrolled', !entry.isIntersecting),
    { threshold: 0 }
  );

  observer.observe(sentinel);
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

  let lastFocused = null;

  function getFocusable() {
    return Array.from(
      mobileMenu.querySelectorAll(
        'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'
      )
    ).filter((el) => !el.hasAttribute('disabled') && el.getAttribute('aria-hidden') !== 'true');
  }

  function setMenuOpen(isOpen) {
    mobileMenu.classList.toggle('open', isOpen);
    navToggle.classList.toggle('open', isOpen);
    navToggle.setAttribute('aria-expanded', String(isOpen));
    mobileMenu.setAttribute('aria-hidden', String(!isOpen));
    mobileMenu.setAttribute('aria-modal', String(isOpen));
    document.body.style.overflow = isOpen ? 'hidden' : '';

    if (isOpen) {
      lastFocused = document.activeElement;
      const focusables = getFocusable();
      const target = focusables[0] || mobileMenu;
      requestAnimationFrame(() => target.focus());
    } else if (lastFocused && typeof lastFocused.focus === 'function') {
      lastFocused.focus();
      lastFocused = null;
    }
  }

  function toggleMenu() {
    setMenuOpen(!mobileMenu.classList.contains('open'));
  }

  navToggle.addEventListener('click', toggleMenu);

  document.addEventListener('keydown', (event) => {
    if (!mobileMenu.classList.contains('open')) return;

    if (event.key === 'Escape') {
      setMenuOpen(false);
      navToggle.focus();
      return;
    }

    if (event.key !== 'Tab') return;

    const focusables = getFocusable();
    if (focusables.length === 0) {
      event.preventDefault();
      mobileMenu.focus();
      return;
    }

    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    const active = document.activeElement;

    if (event.shiftKey && (active === first || active === mobileMenu)) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && active === last) {
      event.preventDefault();
      first.focus();
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

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let autoSlideTimer = null;

  const stopAutoSlide = () => {
    if (!autoSlideTimer) return;
    clearInterval(autoSlideTimer);
    autoSlideTimer = null;
  };

  const startAutoSlide = (intervalMs) => {
    if (prefersReducedMotion) return;
    stopAutoSlide();
    autoSlideTimer = setInterval(nextSlide, intervalMs);
  };

  const deferAutoSlide = () => {
    if (prefersReducedMotion) return;
    startAutoSlide(12000);
  };

  startAutoSlide(8000);

  if (nextBtn) nextBtn.addEventListener('click', deferAutoSlide);
  if (prevBtn) prevBtn.addEventListener('click', deferAutoSlide);
  dots.forEach(dot => dot.addEventListener('click', deferAutoSlide));

  slider.setAttribute('tabindex', '0');
  slider.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') {
      event.preventDefault();
      deferAutoSlide();
      nextSlide();
    } else if (event.key === 'ArrowLeft') {
      event.preventDefault();
      deferAutoSlide();
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
      deferAutoSlide();
      if (diff > 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
  }
}

/**
 * Program detail dialogs on The Next Chapter page.
 */
function setupChapterSupportDialogs() {
  const dialog = document.getElementById('chapter-support-dialog');
  if (!dialog) return;

  const openButtons = document.querySelectorAll('.chapter-support-panel__open');
  const closeButton = dialog.querySelector('.chapter-support-dialog__close');
  const title = dialog.querySelector('#chapter-support-dialog-title');
  const body = dialog.querySelector('.chapter-support-dialog__body');
  let activeTrigger = null;

  function openDialog(button) {
    const templateId = button.dataset.dialogTemplate;
    const template = document.getElementById(templateId);
    if (!template || !title || !body) return;

    activeTrigger = button;
    title.textContent = button.dataset.dialogTitle || '';
    body.replaceChildren(template.content.cloneNode(true));
    document.body.classList.add('has-open-dialog');

    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    } else {
      dialog.setAttribute('open', '');
    }

    requestAnimationFrame(() => closeButton?.focus());
  }

  function closeDialog() {
    if (typeof dialog.close === 'function' && dialog.open) {
      dialog.close();
    } else {
      dialog.removeAttribute('open');
      document.body.classList.remove('has-open-dialog');
      activeTrigger?.focus();
      activeTrigger = null;
    }
  }

  openButtons.forEach((button) => {
    button.addEventListener('click', () => openDialog(button));
  });

  closeButton?.addEventListener('click', closeDialog);

  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) closeDialog();
  });

  dialog.addEventListener('close', () => {
    document.body.classList.remove('has-open-dialog');
    activeTrigger?.focus();
    activeTrigger = null;
  });
}

/**
 * Bring the reasons for support into focus as they enter the reading area.
 */
function setupNextChapterReliefTiles() {
  const tiles = document.querySelectorAll('.next-chapter-relief__reasons > li');
  if (!tiles.length) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion || !('IntersectionObserver' in window)) {
    tiles.forEach((tile) => tile.classList.add('is-highlighted'));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-highlighted');
        observer.unobserve(entry.target);
      });
    },
    {
      threshold: 0.35,
      rootMargin: '0px 0px -10% 0px'
    }
  );

  tiles.forEach((tile) => observer.observe(tile));
}

/**
 * Expand the counseling outcomes as a connected set of possibilities.
 * The list remains visible by default if JavaScript is unavailable.
 */
function setupCounselingOutcomesExpansion() {
  const lists = document.querySelectorAll('.counseling-outcomes__list');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!lists.length || prefersReducedMotion || !('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      entry.target.classList.add('is-outcome-expanded');
      observer.unobserve(entry.target);
    });
  }, {
    threshold: 0.3,
    rootMargin: '0px 0px -8% 0px'
  });

  lists.forEach((list) => {
    list.classList.add('is-expansion-ready');
    list.querySelectorAll('li').forEach((item) => observer.observe(item));
  });
}

/**
 * Fade-in sections and staggered children on scroll
 */
function setupScrollReveal() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobileSessionDetails = window.matchMedia('(max-width: 760px)').matches;
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
    '.opportunity-list li',
    '.chapter-result',
    '.chapter-stage',
    '.chapter-support-panel',
    '.next-chapter-fit-item',
    '.chapter-faq'
  ].join(', ');

  const sections = main.querySelectorAll('section');
  const revealTargets = [];

  if (main.classList.contains('legal-content')) {
    main.classList.add('reveal');
    revealTargets.push(main);
  }

  sections.forEach((section) => {
    if (section.hasAttribute('data-reveal-disabled')) return;
    if (isMobileSessionDetails && section.classList.contains('counseling-sessions')) return;

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
