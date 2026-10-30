/* SecureGuard PRD Interactive JavaScript */
document.addEventListener('DOMContentLoaded', function () {
  // 1. Sidebar Toggle Feature
  const toggleBtn = document.getElementById('toggleSidebarBtn');
  const sidebar = document.querySelector('.sidebar');

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', function () {
      sidebar.classList.toggle('open');
      if (window.innerWidth > 768) {
        if (sidebar.style.display === 'none') {
          sidebar.style.display = 'flex';
        } else {
          sidebar.style.display = 'none';
        }
      }
    });
  }

  // 2. Dark Mode Toggle
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const currentTheme = localStorage.getItem('sgcs_theme') || 'light';

  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    if (themeToggleBtn) {
      themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i> 浅色模式';
    }
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function () {
      let theme = document.documentElement.getAttribute('data-theme');
      if (theme === 'dark') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('sgcs_theme', 'light');
        themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i> 深色模式';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('sgcs_theme', 'dark');
        themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i> 浅色模式';
      }
    });
  }

  // 3. Smooth Scrolling for Anchor Links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });

  // 4. Accordions
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', function () {
      const item = this.parentElement;
      item.classList.toggle('active');
    });
  });

  // 5. Code Copy Button
  document.querySelectorAll('.code-block').forEach(block => {
    if (!block.querySelector('.copy-btn')) {
      const copyBtn = document.createElement('button');
      copyBtn.className = 'copy-btn';
      copyBtn.innerHTML = '<i class="far fa-copy"></i> 复制';
      copyBtn.addEventListener('click', function () {
        const codeText = block.querySelector('code') ? block.querySelector('code').innerText : block.innerText;
        navigator.clipboard.writeText(codeText.trim()).then(() => {
          copyBtn.innerHTML = '<i class="fas fa-check"></i> 已复制';
          setTimeout(() => {
            copyBtn.innerHTML = '<i class="far fa-copy"></i> 复制';
          }, 2000);
        });
      });
      block.appendChild(copyBtn);
    }
  });

  // 6. Global Quick Search Filter (if on index page or top navbar)
  const globalSearchInput = document.getElementById('globalSearchInput');
  if (globalSearchInput) {
    globalSearchInput.addEventListener('keyup', function (e) {
      const filter = e.target.value.toLowerCase();
      const searchItems = document.querySelectorAll('.searchable-item, .card, table tbody tr');

      searchItems.forEach(item => {
        const text = item.innerText.toLowerCase();
        if (text.includes(filter)) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  }
});
