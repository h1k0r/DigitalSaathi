/**
 * VYTRA — GOOGLE ADSENSE CENTRAL CONFIGURATION & LOADER
 * File: config/ads-config.js
 * Production Domain: https://digitalsaathi.vytra.in
 *
 * INSTRUCTIONS FOR ACTIVATION:
 * 1. Register your site on Google AdSense (https://www.google.com/adsense/).
 * 2. When approved, obtain your Google AdSense Publisher ID (e.g. ca-pub-1234567890123456).
 * 3. Replace 'ca-pub-XXXXXXXXXXXXXXXX' below with your actual Publisher ID.
 * 4. Toggle 'enabled: true'.
 * 5. Update /ads.txt with your corresponding pub-XXXXXXXXXXXXXXXX.
 */

(function () {
  'use strict';

  const ADSENSE_CONFIG = {
    // Set to true once approved by Google AdSense
    enabled: false,

    // Replace ca-pub-XXXXXXXXXXXXXXXX with the publisher ID supplied by Google AdSense
    publisherId: "ca-pub-XXXXXXXXXXXXXXXX",

    // Automatically load Google Auto Ads script in <head> when enabled
    autoAds: true,

    // Show clean, non-intrusive preview placeholders during local development/testing only
    // Set to false in production until AdSense is activated
    devPlaceholder: false,

    // Defined slot dimensions to protect Core Web Vitals (Zero Layout Shift - CLS < 0.1)
    slots: {
      toolSeparator: {
        format: 'auto',
        minHeight: '100px',
        maxWidth: '728px'
      },
      footerBanner: {
        format: 'auto',
        minHeight: '90px',
        maxWidth: '728px'
      }
    }
  };

  /**
   * Initializes Google AdSense safely without layout shifts or policy violations
   */
  function initAdSense() {
    // Check if consent has been revoked
    try {
      const consentStatus = localStorage.getItem('ds_consent_status');
      if (consentStatus === 'rejected') {
        // User explicitly rejected advertising cookies
        collapseAdSlots();
        return;
      }
    } catch (e) {
      // Local storage unavailable
    }

    // Check if enabled with a genuine publisher ID (not placeholder)
    const isPlaceholder = !ADSENSE_CONFIG.publisherId || 
                          ADSENSE_CONFIG.publisherId.includes('XXXXXXXXXXXXXXXX');

    if (ADSENSE_CONFIG.enabled && !isPlaceholder) {
      // Load Official Google AdSense Client Script Asynchronously
      if (!document.querySelector('script[src*="pagead2.googlesyndication.com"]')) {
        const adScript = document.createElement('script');
        adScript.async = true;
        adScript.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_CONFIG.publisherId}`;
        adScript.crossOrigin = 'anonymous';
        document.head.appendChild(adScript);
        console.info('[Vytra] Google AdSense initialized.');
      }
    } else {
      // AdSense disabled or placeholder active
      const isDevQuery = window.location.search.includes('ads_dev=1');
      const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

      if ((ADSENSE_CONFIG.devPlaceholder || isDevQuery) && isLocalhost) {
        renderDevelopmentPlaceholders();
      } else {
        collapseAdSlots();
      }
    }
  }

  /**
   * Renders neutral, clean development placeholders for layout verification (Dev mode only)
   */
  function renderDevelopmentPlaceholders() {
    const slots = document.querySelectorAll('.ad-container, .adsense-slot');
    slots.forEach(slot => {
      if (!slot.querySelector('.ad-placeholder-badge')) {
        slot.style.display = 'flex';
        slot.style.alignItems = 'center';
        slot.style.justifyContent = 'center';
        slot.style.background = '#f8fafc';
        slot.style.border = '1px dashed #cbd5e1';
        slot.style.borderRadius = '8px';
        slot.style.margin = '2rem auto';
        slot.style.padding = '12px';
        slot.style.minHeight = '100px';
        slot.style.maxWidth = '728px';
        slot.innerHTML = '<span class="ad-placeholder-badge" style="font-size:0.75rem;font-weight:700;letter-spacing:0.05em;color:#94a3b8;text-transform:uppercase;">Advertisement Space (ca-pub-XXXXXXXXXXXXXXXX)</span>';
      }
    });
  }

  /**
   * Collapses ad containers when AdSense is not active to prevent blank white gaps
   */
  function collapseAdSlots() {
    const slots = document.querySelectorAll('.ad-container, .adsense-slot');
    slots.forEach(slot => {
      slot.style.display = 'none';
    });
  }

  // Global object export (Vytra primary + backward compatible alias)
  const adsController = {
    config: ADSENSE_CONFIG,
    init: initAdSense,
    collapse: collapseAdSlots
  };
  window.VYTRA_ADS = adsController;
  window.DIGITALSAATHI_ADS = adsController;

  // Run initialization on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAdSense);
  } else {
    initAdSense();
  }

})();
