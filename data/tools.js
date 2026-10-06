/**
 * DIGITALSAATHI — MASTER TOOLS REGISTRY (data/tools.js)
 * Central structured data registry powering directory, search, category filters, and related tools.
 */

(function () {
  'use strict';

  const TOOLS_DATA = [
    // =========================================================================
    // 1. PDF TOOLS
    // =========================================================================
    {
      id: 'merge-pdf',
      name: 'Merge PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Combine multiple PDF files into one single organized document in your chosen order.',
      icon: '📑',
      url: 'pdf/merge.html',
      tags: ['merge', 'combine', 'join', 'pdf', 'binder', 'pages', 'organize'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'split-pdf',
      name: 'Split PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Extract specific pages or separate a PDF into individual one-page documents.',
      icon: '✂️',
      url: 'pdf/split.html',
      tags: ['split', 'extract', 'separate', 'pages', 'cut', 'pdf'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'compress-pdf',
      name: 'Compress PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Reduce PDF file size to under 100KB, 200KB or 500KB while maintaining optimal quality.',
      icon: '🗜️',
      url: 'pdf/compress.html',
      tags: ['compress', 'reduce', 'size', 'kb', 'mb', 'shrink', 'optimize', 'pdf'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'jpg-to-pdf',
      name: 'JPG to PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Convert JPG, PNG, and WebP images into a single professional A4 PDF document.',
      icon: '📄',
      url: 'pdf/jpg-to-pdf.html',
      tags: ['jpg to pdf', 'images to pdf', 'png to pdf', 'convert', 'a4', 'photos to pdf'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'pdf-to-jpg',
      name: 'PDF to JPG',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Extract all pages from a PDF document as high-resolution JPG or PNG images in ZIP.',
      icon: '🖼️',
      url: 'pdf/pdf-to-jpg.html',
      tags: ['pdf to jpg', 'pdf to images', 'extract photos', 'png', 'zip', 'high dpi'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'rotate-pdf',
      name: 'Rotate PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Rotate PDF pages permanently to portrait or landscape (90°, 180°, 270°).',
      icon: '🔄',
      url: 'pdf/rotate.html',
      tags: ['rotate', 'orientation', 'upside down', 'landscape', 'portrait', 'fix', 'pdf'],
      browserBased: true,
      popular: false,
      badge: 'Browser'
    },
    {
      id: 'edit-pdf',
      name: 'Edit PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Add text, draw shapes, insert images, and annotate PDF documents easily.',
      icon: '✏️',
      url: 'pdf/edit.html',
      tags: ['edit', 'annotate', 'write', 'draw', 'text', 'pdf editor'],
      browserBased: true,
      popular: false,
      badge: 'Browser'
    },
    {
      id: 'sign-pdf',
      name: 'Sign PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Draw or upload your digital signature and place it onto any PDF contract or form.',
      icon: '✍️',
      url: 'pdf/sign.html',
      tags: ['sign', 'signature', 'contract', 'e-sign', 'fill', 'pdf'],
      browserBased: true,
      popular: false,
      badge: 'Browser'
    },
    {
      id: 'protect-pdf',
      name: 'Protect PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Encrypt PDF files with secure AES password protection and permission restrictions.',
      icon: '🔒',
      url: 'pdf/protect.html',
      tags: ['protect', 'password', 'encrypt', 'lock', 'secure', 'pdf'],
      browserBased: true,
      popular: false,
      badge: 'Secure'
    },
    {
      id: 'unlock-pdf',
      name: 'Unlock PDF',
      category: 'pdf',
      categoryName: 'PDF Tools',
      description: 'Remove password and decrypt protected PDF files if you have the permission.',
      icon: '🔓',
      url: 'pdf/unlock.html',
      tags: ['unlock', 'remove password', 'decrypt', 'open', 'pdf'],
      browserBased: true,
      popular: false,
      badge: 'Browser'
    },

    // =========================================================================
    // 2. IMAGE TOOLS
    // =========================================================================
    {
      id: 'image-compressor',
      name: 'Image Compressor',
      category: 'images',
      categoryName: 'Image Tools',
      description: 'Compress JPG, PNG, and WebP images to exact target KB size (under 20KB, 50KB, 100KB).',
      icon: '🗜️',
      url: 'image/compress.html',
      tags: ['image compressor', 'compress photo', 'reduce size', 'kb', 'shrink photo', 'jpg', 'png'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'image-resizer',
      name: 'Image Resizer',
      category: 'images',
      categoryName: 'Image Tools',
      description: 'Resize image dimensions by exact pixels, percentage, or presets with aspect ratio lock.',
      icon: '📐',
      url: 'image/resize.html',
      tags: ['image resizer', 'resize photo', 'dimensions', 'width', 'height', 'scale', 'pixels'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'image-cropper',
      name: 'Image Cropper',
      category: 'images',
      categoryName: 'Image Tools',
      description: 'Crop photos with standard aspect ratios (1:1, 4:3, 16:9, Passport 3.5x4.5cm) or freeform.',
      icon: '✂️',
      url: 'image/crop.html',
      tags: ['crop', 'cut image', 'square', 'avatar', 'trim', 'aspect ratio'],
      browserBased: true,
      popular: false,
      badge: 'Fast'
    },
    {
      id: 'image-converter',
      name: 'Image Converter',
      category: 'images',
      categoryName: 'Image Tools',
      description: 'Convert image formats between JPG, PNG, WebP, GIF, BMP, and SVG in batch.',
      icon: '🔄',
      url: 'image/convert.html',
      tags: ['convert image', 'format converter', 'jpg to png', 'png to jpg', 'webp', 'batch'],
      browserBased: true,
      popular: false,
      badge: 'Browser'
    },
    {
      id: 'remove-bg',
      name: 'Passport Photo BG Changer',
      category: 'images',
      categoryName: 'Image Tools',
      description: 'Replace photo backgrounds with clean white, blue, red, or transparent backdrop.',
      icon: '🎭',
      url: 'image/remove-bg.html',
      tags: ['remove background', 'white background', 'blue background', 'passport photo', 'cutout'],
      browserBased: true,
      popular: false,
      badge: 'AI'
    },
    {
      id: 'blur-face',
      name: 'Blur & Redact Image',
      category: 'images',
      categoryName: 'Image Tools',
      description: 'Pixelate or blackout sensitive info, numbers, IDs, and faces on images for privacy.',
      icon: '🔒',
      url: 'image/blur-face.html',
      tags: ['blur', 'redact', 'censor', 'pixelate', 'hide face', 'aadhaar', 'id'],
      browserBased: true,
      popular: false,
      badge: 'Privacy'
    },

    // =========================================================================
    // 3. DEVELOPER TOOLS
    // =========================================================================
    {
      id: 'json-formatter',
      name: 'JSON Formatter',
      category: 'developer',
      categoryName: 'Developer Tools',
      description: 'Beautify, validate, minify, and inspect JSON with collapsible interactive tree view.',
      icon: '💻',
      url: 'developer/json.html',
      tags: ['json formatter', 'json validator', 'beautify json', 'minify', 'tree view', 'parse'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'base64-encoder',
      name: 'Base64 Encoder / Decoder',
      category: 'developer',
      categoryName: 'Developer Tools',
      description: 'Encode text, images, and files to Base64 format and decode Base64 back with live preview.',
      icon: '🔤',
      url: 'developer/base64.html',
      tags: ['base64', 'encode', 'decode', 'data uri', 'binary', 'string', 'image to base64'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'sql-formatter',
      name: 'SQL Query Formatter',
      category: 'developer',
      categoryName: 'Developer Tools',
      description: 'Beautify and indent complex SQL queries with syntax highlighting and keyword casing.',
      icon: '💾',
      url: 'developer/sql.html',
      tags: ['sql formatter', 'beautify sql', 'database', 'mysql', 'postgres', 'query'],
      browserBased: true,
      popular: false,
      badge: 'Fast'
    },

    // =========================================================================
    // 4. CALCULATORS
    // =========================================================================
    {
      id: 'percentage-calculator',
      name: 'Percentage Calculator',
      category: 'calculators',
      categoryName: 'Calculators',
      description: 'Calculate percentages, % increase / decrease, discount rates, and marks conversion.',
      icon: '📊',
      url: 'calculators/percentage.html',
      tags: ['percentage calculator', 'percent', 'discount', 'increase', 'marks', 'math'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'age-calculator',
      name: 'Age Calculator',
      category: 'calculators',
      categoryName: 'Calculators',
      description: 'Calculate exact age in years, months, days, hours, and next birthday countdown timer.',
      icon: '🎂',
      url: 'calculators/age.html',
      tags: ['age calculator', 'date of birth', 'dob', 'birthday countdown', 'days lived', 'date difference'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'emi-calculator',
      name: 'EMI Calculator',
      category: 'calculators',
      categoryName: 'Calculators',
      description: 'Calculate monthly loan EMI, interest breakdown, and amortization schedule with charts.',
      icon: '💰',
      url: 'calculators/emi.html',
      tags: ['emi calculator', 'loan calculator', 'interest', 'home loan', 'car loan', 'amortization'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'cgpa-calculator',
      name: 'CGPA Calculator',
      category: 'calculators',
      categoryName: 'Calculators',
      description: 'Calculate semester CGPA, SGPA to percentage, and credit-weighted grade points.',
      icon: '🎓',
      url: 'calculators/cgpa.html',
      tags: ['cgpa calculator', 'sgpa', 'percentage', 'grade', 'university', 'college'],
      browserBased: true,
      popular: false,
      badge: 'Fast'
    },
    {
      id: 'attendance-calculator',
      name: 'Attendance Calculator',
      category: 'calculators',
      categoryName: 'Calculators',
      description: 'Track class attendance, calculate minimum classes needed to maintain 75% target.',
      icon: '📅',
      url: 'calculators/attendance.html',
      tags: ['attendance calculator', '75 percent', 'bunk tracker', 'classes', 'college attendance'],
      browserBased: true,
      popular: false,
      badge: 'Fast'
    },

    // =========================================================================
    // 5. TEXT TOOLS
    // =========================================================================
    {
      id: 'word-counter',
      name: 'Word Counter',
      category: 'text',
      categoryName: 'Text Tools',
      description: 'Count words, characters, sentences, paragraphs, reading time, and keyword density.',
      icon: '📝',
      url: 'text/word-counter.html',
      tags: ['word counter', 'character counter', 'reading time', 'paragraphs', 'keyword density', 'text analyzer'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },

    // =========================================================================
    // 6. UTILITY TOOLS
    // =========================================================================
    {
      id: 'qr-generator',
      name: 'QR Code Generator',
      category: 'utilities',
      categoryName: 'Utility Tools',
      description: 'Generate high-resolution custom QR codes for URLs, text, WiFi, vCard, and contacts.',
      icon: '📱',
      url: 'utilities/qr-generator.html',
      tags: ['qr code generator', 'create qr', 'wifi qr', 'custom qr code', 'barcode', 'download qr'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    },
    {
      id: 'password-generator',
      name: 'Password Generator',
      category: 'utilities',
      categoryName: 'Utility Tools',
      description: 'Create cryptographically secure, uncrackable passwords with custom rules and strength meter.',
      icon: '🔐',
      url: 'utilities/password-generator.html',
      tags: ['password generator', 'random password', 'secure password', 'generator', 'pin', 'passphrase'],
      browserBased: true,
      popular: true,
      badge: 'Popular'
    }
  ];

  // Path resolution utility for nested directories
  function resolveToolUrl(url) {
    if (!url) return '#';
    if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('#')) return url;
    
    // Check nesting level of current document
    const path = window.location.pathname.replace(/\\/g, '/');
    let prefix = '';
    
    if (path.includes('/tools/') || path.includes('/pdf/') || path.includes('/image/') || 
        path.includes('/developer/') || path.includes('/calculators/') || 
        path.includes('/text/') || path.includes('/utilities/')) {
      prefix = '../';
    }
    
    const cleanUrl = url.replace(/^\/+/, '');
    return prefix + cleanUrl;
  }

  // =========================================================================
  // Professional Vector SVG Icon Tile Generator (Like iLovePDF SaaS standard)
  // =========================================================================
  const SVG_ICONS = {
    'merge-pdf': {
      bg: '#ffefe8', color: '#ea580c',
      svg: '<svg viewBox="0 0 24 24"><path d="M4 4l6 6M4 10h6V4M20 20l-6-6M20 14h-6v6"/><line x1="12" y1="2" x2="12" y2="22" stroke-dasharray="3 3"/></svg>'
    },
    'split-pdf': {
      bg: '#ffefe8', color: '#ea580c',
      svg: '<svg viewBox="0 0 24 24"><path d="M10 4L4 10M4 4h6M4 4v6M14 20l6-6M20 20h-6M20 20v-6"/><line x1="12" y1="2" x2="12" y2="22" stroke-dasharray="3 3"/></svg>'
    },
    'compress-pdf': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><path d="M4 14h6v6M4 20l6-6M20 10h-6V4M20 4l-6 6M14 14h6v6M14 20l6-6M10 10H4V4M4 4l6 6"/></svg>'
    },
    'jpg-to-pdf': {
      bg: '#fef2f2', color: '#dc2626',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>'
    },
    'pdf-to-jpg': {
      bg: '#fffbeb', color: '#d97706',
      svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><circle cx="10" cy="13" r="1.5"/><path d="m18 18-3.5-3.5a1.4 1.4 0 0 0-2 0L8 19"/></svg>'
    },
    'edit-pdf': {
      bg: '#fdf4ff', color: '#9333ea',
      svg: '<svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>'
    },
    'sign-pdf': {
      bg: '#fff1f2', color: '#e11d48',
      svg: '<svg viewBox="0 0 24 24"><path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z"/><path d="M8 12c2 0 3-1 3-2s-1-2-2.5-2C7 8 7 10 8 12c1 2 3 3 5 3s4-1 4-2"/></svg>'
    },
    'protect-pdf': {
      bg: '#faf5ff', color: '#7c3aed',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
    },
    'rotate-pdf': {
      bg: '#eff6ff', color: '#3b82f6',
      svg: '<svg viewBox="0 0 24 24"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>'
    },
    'compress-image': {
      bg: '#f5f3ff', color: '#6366f1',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><polyline points="8 12 12 16 16 12"/><line x1="12" y1="8" x2="12" y2="16"/></svg>'
    },
    'resize-image': {
      bg: '#f5f3ff', color: '#6366f1',
      svg: '<svg viewBox="0 0 24 24"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>'
    },
    'crop-image': {
      bg: '#f5f3ff', color: '#6366f1',
      svg: '<svg viewBox="0 0 24 24"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>'
    },
    'convert-image': {
      bg: '#ecfeff', color: '#0891b2',
      svg: '<svg viewBox="0 0 24 24"><path d="M17 1l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 23l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>'
    },
    'passport-photo': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 19a5 5 0 0 1 10 0"/></svg>'
    },
    'signature-resizer': {
      bg: '#fff1f2', color: '#e11d48',
      svg: '<svg viewBox="0 0 24 24"><path d="M3 18c3-4 6 2 9-1s6-4 9-1"/><line x1="3" y1="21" x2="21" y2="21"/></svg>'
    },
    'json-formatter': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><polyline points="8 3 4 8 4 12 2 12 4 12 4 16 8 21"/><polyline points="16 3 20 8 20 12 22 12 20 12 20 16 16 21"/></svg>'
    },
    'base64-converter': {
      bg: '#eef2ff', color: '#4f46e5',
      svg: '<svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
    },
    'sql-formatter': {
      bg: '#eff6ff', color: '#0284c7',
      svg: '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>'
    },
    'emi-calculator': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>'
    },
    'percentage-calculator': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>'
    },
    'age-calculator': {
      bg: '#fffbeb', color: '#d97706',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><circle cx="12" cy="16" r="3"/><polyline points="12 15 12 16 13 16"/></svg>'
    },
    'cgpa-calculator': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
    },
    'attendance-calculator': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><polyline points="9 14 11 16 15 11"/></svg>'
    },
    'word-counter': {
      bg: '#fdf4ff', color: '#9333ea',
      svg: '<svg viewBox="0 0 24 24"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="14" y2="12"/><line x1="4" y1="18" x2="18" y2="18"/><polyline points="17 11 19 13 22 10"/></svg>'
    },
    'qr-generator': {
      bg: '#ecfeff', color: '#0891b2',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="3" height="3"/><rect x="18" y="14" width="3" height="3"/><rect x="14" y="18" width="3" height="3"/><rect x="18" y="18" width="3" height="3"/></svg>'
    },
    'password-generator': {
      bg: '#faf5ff', color: '#7c3aed',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><circle cx="12" cy="16" r="1"/></svg>'
    }
  };

  function getToolSvgIcon(toolId, category) {
    if (SVG_ICONS[toolId]) {
      const item = SVG_ICONS[toolId];
      return `<div class="tool-icon-tile" style="background:${item.bg};color:${item.color};">${item.svg}</div>`;
    }
    
    // Category Fallbacks with crisp vector SVGs
    const catFallbacks = {
      pdf: { bg: '#ffefe8', color: '#ea580c', svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>' },
      images: { bg: '#f5f3ff', color: '#6366f1', svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>' },
      image: { bg: '#f5f3ff', color: '#6366f1', svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>' },
      developer: { bg: '#eff6ff', color: '#2563eb', svg: '<svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>' },
      calculators: { bg: '#ecfdf5', color: '#059669', svg: '<svg viewBox="0 0 24 24"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>' },
      text: { bg: '#fdf4ff', color: '#9333ea', svg: '<svg viewBox="0 0 24 24"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="14" y2="12"/><line x1="4" y1="18" x2="18" y2="18"/></svg>' },
      utilities: { bg: '#ecfeff', color: '#0891b2', svg: '<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>' }
    };
    
    const c = (category || 'pdf').toLowerCase();
    const fallback = catFallbacks[c] || catFallbacks.pdf;
    return `<div class="tool-icon-tile" style="background:${fallback.bg};color:${fallback.color};">${fallback.svg}</div>`;
  }

  // Global object export
  window.DIGITALSAATHI_TOOLS = TOOLS_DATA;
  window.resolveToolUrl = resolveToolUrl;
  window.getToolSvgIcon = getToolSvgIcon;

})();
