/* ============================================================
   Theme toggle — light / dark with localStorage persistence.
   The "no-FOUC" inline init lives in base.html <head>.
   ============================================================ */
(function () {
    'use strict';

    const STORAGE_KEY = 'gam3aty-theme';

    function getStoredTheme() {
        try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
    }

    function setStoredTheme(value) {
        try { localStorage.setItem(STORAGE_KEY, value); } catch (e) { /* ignore */ }
    }

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        const buttons = document.querySelectorAll('[data-theme-toggle]');
        buttons.forEach((btn) => {
            btn.setAttribute('aria-pressed', String(theme === 'dark'));
            btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
        });
    }

    function currentTheme() {
        return document.documentElement.getAttribute('data-theme') || 'light';
    }

    function toggle() {
        const next = currentTheme() === 'dark' ? 'light' : 'dark';
        setStoredTheme(next);
        applyTheme(next);
    }

    document.addEventListener('DOMContentLoaded', function () {
        const buttons = document.querySelectorAll('[data-theme-toggle]');
        buttons.forEach((btn) => btn.addEventListener('click', toggle));
        applyTheme(currentTheme());
    });

    // Respond to OS theme changes if user hasn't chosen one
    if (window.matchMedia) {
        const mq = window.matchMedia('(prefers-color-scheme: dark)');
        mq.addEventListener && mq.addEventListener('change', function (e) {
            if (!getStoredTheme()) applyTheme(e.matches ? 'dark' : 'light');
        });
    }
})();
