/* ============================================================
   Mobile nav toggle + small interactivity helpers
   ============================================================ */
(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        const toggle = document.querySelector('[data-nav-toggle]');
        const body = document.body;

        function setMenuOpen(open) {
            body.classList.toggle('menu-open', open);
            if (toggle) toggle.setAttribute('aria-expanded', String(open));
        }

        if (toggle) {
            toggle.addEventListener('click', function () {
                setMenuOpen(!body.classList.contains('menu-open'));
            });
        }

        // Close menu when a link inside it is activated
        document.querySelectorAll('.mobile-menu a, .mobile-menu button[type="submit"]').forEach(function (el) {
            el.addEventListener('click', function () { setMenuOpen(false); });
        });

        // Close menu on Esc
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && body.classList.contains('menu-open')) {
                setMenuOpen(false);
                if (toggle) toggle.focus();
            }
        });

        // Close menu if user resizes back to desktop
        let resizeT;
        window.addEventListener('resize', function () {
            clearTimeout(resizeT);
            resizeT = setTimeout(function () {
                if (window.innerWidth > 900 && body.classList.contains('menu-open')) {
                    setMenuOpen(false);
                }
            }, 100);
        });

        // Password show/hide toggles
        document.querySelectorAll('[data-toggle-password]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                const targetId = btn.getAttribute('data-toggle-password');
                const input = document.getElementById(targetId);
                if (!input) return;
                const isPwd = input.getAttribute('type') === 'password';
                input.setAttribute('type', isPwd ? 'text' : 'password');
                btn.setAttribute('aria-pressed', String(isPwd));
                btn.setAttribute('aria-label', isPwd ? 'Hide password' : 'Show password');
                const iconShow = btn.querySelector('.icon-show');
                const iconHide = btn.querySelector('.icon-hide');
                if (iconShow && iconHide) {
                    iconShow.style.display = isPwd ? 'none' : 'block';
                    iconHide.style.display = isPwd ? 'block' : 'none';
                }
            });
        });

        // Toast auto-dismiss
        document.querySelectorAll('.toast').forEach(function (toast) {
            const closeBtn = toast.querySelector('.toast-close');
            const dismiss = function () {
                toast.style.transition = 'opacity 200ms, transform 200ms';
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(8px)';
                setTimeout(function () { toast.remove(); }, 220);
            };
            if (closeBtn) closeBtn.addEventListener('click', dismiss);
            setTimeout(dismiss, 5000);
        });
    });
})();
