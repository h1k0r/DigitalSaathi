/* VYTRA IDE v1.0 — VS Code-style shell (Monaco + explorer + panel + runner + problems).
   Config comes from window.VYTRA_IDE set inline in the page. Vanilla JS, no build. */
(function () {
'use strict';

/* ---------------- config ---------------- */
var CFG = window.VYTRA_IDE || {};
var LANGS = {
  c:          { monaco: 'c',          ext: 'c',   main: 'main.c',   label: 'C (gcc)',         runner: 'gcc',    wb: 'gcc-13.2.0-c' },
  cpp:        { monaco: 'cpp',        ext: 'cpp', main: 'main.cpp', label: 'C++ (g++)',       runner: 'g++',    wb: 'gcc-13.2.0' },
  java:       { monaco: 'java',       ext: 'java', main: 'Main.java', label: 'Java (OpenJDK)', runner: 'OpenJDK', wb: 'openjdk-jdk-21+35' },
  php:        { monaco: 'php',        ext: 'php', main: 'main.php', label: 'PHP (CLI)',       runner: 'php',    wb: 'php-8.3.12' },
  python:     { monaco: 'python',     ext: 'py',  main: 'main.py',  label: 'Python 3',        runner: 'python', wb: 'cpython-3.10.0' },
  javascript: { monaco: 'javascript', ext: 'js',  main: 'main.js',  label: 'JavaScript (node)', runner: 'node', wb: 'nodejs-18.15.0' }
};
function urlLang() {
  try {
    var m = /[?&]lang=([a-z+]+)/i.exec(location.search || '');
    if (m && LANGS[m[1].toLowerCase()]) return m[1].toLowerCase();
  } catch (e) {}
  return null;
}
function applyLangVars(key) {
  var L = LANGS[key]; LANG = key;
  MONACO_LANG = L.monaco; EXT = L.ext; MAIN = L.main; LABEL = L.label;
  LS_PROJ = 'vytra-ide-proj-' + key; OLD_KEY = 'vytra-proj-' + key;
}
var LANG = urlLang() || CFG.pistonLang || 'c';
if (!LANGS[LANG]) LANG = 'c';
var MONACO_LANG = LANGS[LANG].monaco;
var EXT = LANGS[LANG].ext;
var MAIN = LANGS[LANG].main;
var LABEL = LANGS[LANG].label;
var LS_PROJ = 'vytra-ide-proj-' + LANG;
var LS_SET = 'vytra-ide-settings';
var OLD_KEY = 'vytra-proj-' + LANG;
var API_RUN = 'https://emkc.org/api/v2/piston/execute';
var API_RT = 'https://emkc.org/api/v2/piston/runtimes';
var MONACO_BASE = 'https://cdn.jsdelivr.net/npm/monaco-editor@0.52.2/min/vs';

var SAMPLES = {
  c: '#include <stdio.h>\n\nint main() {\n    char name[100];\n    if (scanf("%99s", name) != 1) return 0;\n    printf("Hello, %s!\\n", name);\n    return 0;\n}\n',
  'c++': '#include <iostream>\n#include <string>\nint main() {\n    std::string name;\n    if (!(std::cin >> name)) return 0;\n    std::cout << "Hello, " << name << "!" << std::endl;\n    return 0;\n}\n',
  java: 'import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String name = sc.hasNext() ? sc.next() : "Programmer";\n        System.out.println("Hello, " + name + "!");\n        sc.close();\n    }\n}\n',
  php: "<?php\n$name = trim(fgets(STDIN) ?: '');\nif ($name === '') { $name = 'Programmer'; }\necho \"Hello, $name!\\n\";\n",
  python: 'name = input().strip() or "Programmer"\nprint(f"Hello, {name}!")\n',
  javascript: "const fs = require('fs');\nconst name = fs.readFileSync(0, 'utf8').trim() || 'Programmer';\nconsole.log(`Hello, ${name}!`);\n"
};
var EXAMPLES = {
  c: [
    { name: 'Hello World', files: { 'main.c': '#include <stdio.h>\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}\n' } },
    { name: 'Fibonacci', files: { 'main.c': '#include <stdio.h>\nint fib(int n) { return n < 2 ? n : fib(n-1) + fib(n-2); }\nint main() {\n    for (int i = 0; i < 10; i++) printf("%d ", fib(i));\n    printf("\\n");\n    return 0;\n}\n' } },
    { name: 'Sorting', files: { 'main.c': '#include <stdio.h>\nint main() {\n    int a[] = {5, 2, 9, 1, 7}, n = 5;\n    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++)\n        if (a[i] > a[j]) { int t = a[i]; a[i] = a[j]; a[j] = t; }\n    for (int i = 0; i < n; i++) printf("%d ", a[i]);\n    printf("\\n");\n    return 0;\n}\n' } }
  ]
};
EXAMPLES['c++'] = [
  { name: 'Hello World', files: { 'main.cpp': '#include <iostream>\nint main() {\n    std::cout << "Hello, World!" << std::endl;\n    return 0;\n}\n' } },
  { name: 'Vector sort', files: { 'main.cpp': '#include <iostream>\n#include <vector>\n#include <algorithm>\nint main() {\n    std::vector<int> v = {5, 2, 9, 1, 7};\n    std::sort(v.begin(), v.end());\n    for (int x : v) std::cout << x << " ";\n    std::cout << std::endl;\n    return 0;\n}\n' } }
];
EXAMPLES.java = [
  { name: 'Hello World', files: { 'Main.java': 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}\n' } }
];
EXAMPLES.php = [
  { name: 'Hello World', files: { 'main.php': "<?php\necho \"Hello, World!\\n\";\n" } }
];
EXAMPLES.python = [
  { name: 'Hello World', files: { 'main.py': 'print("Hello, World!")\n' } },
  { name: 'Fibonacci', files: { 'main.py': 'a, b = 0, 1\nfor _ in range(10):\n    print(a, end=" ")\n    a, b = b, a + b\nprint()\n' } }
];
EXAMPLES.javascript = [
  { name: 'Hello World', files: { 'main.js': 'console.log("Hello, World!");\n' } }
];

/* ---------------- utils ---------------- */
function $(id) { return document.getElementById(id); }
function escH(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function on(el, ev, fn) { if (el) el.addEventListener(ev, fn); }

/* ---------------- settings ---------------- */
var settings = { theme: 'vs-dark', fontSize: 14, tabSize: 4, wrap: 'off', minimap: true };
try {
  var ss = JSON.parse(localStorage.getItem(LS_SET) || '{}');
  for (var k in settings) if (ss[k] !== undefined) settings[k] = ss[k];
} catch (e) {}
function saveSettings() { try { localStorage.setItem(LS_SET, JSON.stringify(settings)); } catch (e) {} }

/* ---------------- project store ---------------- */
var state = { files: {}, open: [], active: null, dirty: {} };
function persist() {
  try { localStorage.setItem(LS_PROJ, JSON.stringify({ files: state.files, open: state.open, active: state.active })); } catch (e) {}
}
function starterFiles() {
  var o = {}; o[MAIN] = SAMPLES[LANG] || SAMPLES.c; return o;
}
function loadProject() {
  var fromHash = null;
  try {
    if (location.hash.indexOf('#s=') === 0) {
      var raw = atob(location.hash.slice(3).replace(/-/g, '+').replace(/_/g, '/'));
      var data = JSON.parse(decodeURIComponent(escape(raw)));
      if (data && data.f) fromHash = data;
    }
  } catch (e) {}
  if (fromHash) {
    if (fromHash.l && LANGS[fromHash.l]) applyLangVars(fromHash.l);
    state.files = fromHash.f; state.open = Object.keys(fromHash.f); state.active = state.open[0] || null;
    if (fromHash.s !== undefined) { var si = $('vscStdin'); if (si) si.value = fromHash.s; }
    persist(); return;
  }
  try {
    var s = JSON.parse(localStorage.getItem(LS_PROJ) || 'null');
    if (s && s.files && Object.keys(s.files).length) {
      state.files = s.files;
      state.open = (s.open || []).filter(function (p) { return state.files[p] !== undefined; });
      if (!state.open.length) state.open = Object.keys(state.files);
      state.active = (s.active && state.files[s.active] !== undefined) ? s.active : state.open[0];
      return;
    }
  } catch (e) {}
  try { // migrate previous single/multi-file format
    var old = JSON.parse(localStorage.getItem(OLD_KEY) || 'null');
    if (old && old.length) {
      state.files = {}; old.forEach(function (f) { state.files[f.name] = f.content || ''; });
      state.open = Object.keys(state.files); state.active = state.open[0];
      persist(); return;
    }
  } catch (e) {}
  state.files = starterFiles(); state.open = [MAIN]; state.active = MAIN;
  persist();
}

/* ---------------- editor (Monaco + fallback) ---------------- */
var editor = null, monacoOK = false, fallbackTa = null;
var viewStates = {};
function edGet() {
  if (monacoOK && editor) return editor.getValue();
  return fallbackTa ? fallbackTa.value : '';
}
function edSet(v) {
  if (monacoOK && editor) editor.setValue(v);
  else if (fallbackTa) fallbackTa.value = v;
  syncActiveToModel();
}
function currentContent() {
  return state.active && state.files[state.active] !== undefined ? state.files[state.active] : '';
}
function syncActiveToModel() {
  if (state.active) {
    state.files[state.active] = edGet();
    state.dirty[state.active] = false;
  }
}
function applySettings() {
  if (monacoOK && editor) {
    editor.updateOptions({
      fontSize: settings.fontSize, tabSize: settings.tabSize,
      wordWrap: settings.wrap, minimap: { enabled: !!settings.minimap }
    });
    monaco.editor.setTheme(settings.theme);
  }
  document.querySelector('.vsc-shell').classList.toggle('vsc-light', settings.theme === 'vs');
}
function setStatusPos(line, col) {
  var el = $('vscPos');
  if (el) el.textContent = 'Ln ' + line + ', Col ' + col;
}
function refreshStatus() {
  var n = Object.keys(state.files).length;
  var el = $('vscFiles');
  if (el) el.textContent = n + (n === 1 ? ' file' : ' files');
}
function bootMonaco() {
  return new Promise(function (resolve) {
    if (typeof require === 'undefined') return resolve(false);
    var done = false, to = setTimeout(function () { if (!done) { done = true; resolve(false); } }, 15000);
    try {
      require.config({ paths: { vs: MONACO_BASE } });
      require(['vs/editor/editor.main'], function () {
        if (done) return; done = true; clearTimeout(to); resolve(true);
      }, function () { if (!done) { done = true; clearTimeout(to); resolve(false); } });
    } catch (e) { if (!done) { done = true; clearTimeout(to); resolve(false); } }
  });
}
function initMonaco() {
  monacoOK = true;
  editor = monaco.editor.create($('vscEditor'), {
    value: currentContent(), language: MONACO_LANG, theme: settings.theme,
    fontSize: settings.fontSize, tabSize: settings.tabSize, wordWrap: settings.wrap,
    minimap: { enabled: !!settings.minimap }, automaticLayout: true,
    folding: true, bracketPairColorization: { enabled: true },
    guides: { bracketPairs: true }, scrollBeyondLastLine: false, padding: { top: 10 },
    renderLineHighlight: 'all', smoothScrolling: true
  });
  editor.onDidChangeModelContent(function () {
    if (state.active) { state.dirty[state.active] = (editor.getValue() !== state.files[state.active]); paintTabs(); }
  });
  editor.onDidChangeCursorPosition(function (e) { setStatusPos(e.position.lineNumber, e.position.column); });
  applySettings();
}
function initFallback() {
  monacoOK = false;
  var host = $('vscEditor');
  host.innerHTML = '';
  fallbackTa = document.createElement('textarea');
  fallbackTa.className = 'vsc-fallback';
  fallbackTa.spellcheck = false;
  fallbackTa.value = currentContent();
  host.appendChild(fallbackTa);
  fallbackTa.addEventListener('input', function () {
    if (state.active) { state.dirty[state.active] = (fallbackTa.value !== state.files[state.active]); paintTabs(); }
  });
}

/* ---------------- explorer ---------------- */
function folderTree() {
  var root = {};
  Object.keys(state.files).forEach(function (p) {
    var parts = p.split('/'), node = root;
    for (var i = 0; i < parts.length - 1; i++) {
      node[parts[i]] = node[parts[i]] || {};
      node = node[parts[i]];
    }
    node[parts[parts.length - 1]] = null;
  });
  return root;
}
function sanitizeProject() {
  if (!state.files || typeof state.files !== 'object' || Array.isArray(state.files)) state.files = {};
  Object.keys(state.files).forEach(function (k) {
    if (typeof k !== 'string' || !k.trim() || typeof state.files[k] !== 'string') delete state.files[k];
  });
  var names = Object.keys(state.files);
  if (!names.length) { state.files[MAIN] = SAMPLES[LANG] || ''; names = [MAIN]; }
  state.open = (state.open || []).filter(function (p) { return state.files[p] !== undefined; });
  if (!state.open.length) state.open = names.slice();
  if (!state.active || state.files[state.active] === undefined) state.active = state.open[0];
  if (state.dirty == null || typeof state.dirty !== 'object') state.dirty = {};
}
function paintTree() {
  var host = $('vscTree');
  if (!host) return;
  try {
    host.innerHTML = '';
    var names = Object.keys(state.files).filter(function (k) { return !/\/\.keep$/.test(k); });
    if (!names.length) {
      host.innerHTML = '<div style="padding:14px;font-size:.78rem;color:#858585;">No files yet<br><br>Click <b>+ F</b> above to add one.</div>';
      return;
    }
    walk(folderTree(), '', 0);
    if (!host.children.length) throw new Error('empty render');
  } catch (e) {
    try {
      host.innerHTML = '';
      Object.keys(state.files).forEach(function (p) {
        if (/\/\.keep$/.test(p)) return;
        var row = document.createElement('div');
        row.className = 'vsc-titem' + (p === state.active ? ' active' : '');
        var nm = document.createElement('span');
        nm.className = 'fname'; nm.textContent = p;
        row.appendChild(nm);
        row.addEventListener('click', function () { openFile(p); });
        host.appendChild(row);
      });
    } catch (e2) {}
  }
}
  function walk(node, prefix, depth) {
    Object.keys(node).sort().forEach(function (name) {
      var full = prefix + name;
      if (node[name] === null) {
        var row = document.createElement('div');
        row.className = 'vsc-titem' + (full === state.active ? ' active' : '');
        row.style.paddingLeft = (8 + depth * 14) + 'px';
        var dot = document.createElement('span');
        dot.style.cssText = 'width:7px;height:7px;border-radius:50%;flex-shrink:0;background:' + (state.dirty[full] ? '#E5322D' : '#3a9bdc');
        var nm = document.createElement('span');
        nm.className = 'fname'; nm.textContent = name;
        row.appendChild(dot); row.appendChild(nm);
    
row.addEventListener('click', function () { openFile(full); });
      host.appendChild(row);
      }
    });
  Object.keys(node).sort().forEach(function (name) {
    if (node[name] === null) return;
    var full = prefix + name;
    var row = document.createElement('div');
    row.className = 'vsc-titem';
    row.style.paddingLeft = (8 + depth * 14) + 'px';
    var g = document.createElement('span');
    g.className = 'glyph'; g.textContent = '\u25b8';
    var nm = document.createElement('span');
    nm.textContent = name;
    row.appendChild(g); row.appendChild(nm);
    if (LS_COL_get()[full]) row.classList.add('closed');
    row.addEventListener('click', function () {
      var c = LS_COL_get();
      if (c[full]) delete c[full]; else c[full] = 1;
      LS_COL_set(c);
      paintTree();
    });
    host.appendChild(row);
    if (!LS_COL_get()[full]) walk(node[name], full + '/', depth + 1);
  });
}

/* ---------------- explorer ops (cont.) ---------------- */
function syncEditorToState() { syncEditorToModel(); }
function edSet(v) {
  if (monacoOK && editor) { editor.setValue(v == null ? '' : v); return; }
  if (fallbackTa) fallbackTa.value = v == null ? '' : v;
}
function resetDirty(p) { state.dirty[p] = false; paintTabs(); }
var LS_COL = LS_PROJ + '-collapsed';
function LS_COL_get() { try { return JSON.parse(localStorage.getItem(LS_COL)) || {}; } catch (e) { return {}; } }
function LS_COL_set(c) { try { localStorage.setItem(LS_COL, JSON.stringify(c)); } catch (e) {} }
function closeDrawer() {
  var s = $('vscSide');
  if (s && window.innerWidth <= 900) s.classList.remove('drawer');
}
var pendingKind = 'file';
function askName(kind) {
  pendingKind = kind;
  var row = $('vscNewRow'), inp = $('vscNewName');
  if (!row || !inp) { var n = prompt(kind === 'dir' ? 'Folder path (e.g. src/utils):' : 'File name (e.g. helper.' + EXT + '):'); if (n != null) confirmName(n); return; }
  row.classList.add('on'); inp.value = '';
  inp.placeholder = kind === 'dir' ? 'dir/name (folder)' : 'name.' + EXT;
  inp.focus();
  inp.onkeydown = function (e) {
    if (e.key === 'Enter') confirmName();
    if (e.key === 'Escape') row.classList.remove('on');
  };
  $('vscAddBtn').onclick = function () { confirmName(); };
}
function cleanName(s) { return (s || '').trim().replace(/[\\:*?"<>|]/g, '').replace(/^\.?\//, ''); }
function confirmName(given) {
  var inp = $('vscNewName');
  var nm = cleanName(given !== undefined ? given : (inp ? inp.value : ''));
  var row = $('vscNewRow');
  if (row) row.classList.remove('on');
  if (!nm) return;
  if (pendingKind === 'dir') {
    if (!/\/$/.test(nm)) nm += '/';
    var key = nm + '.keep';
    if (state.files[key] !== undefined) { alert('Already exists.'); return; }
    state.files[key] = '';
    if (state.open.indexOf(key) < 0) state.open.push(key);
    openFile(key);
  } else {
    if (nm.indexOf('.') < 0) nm += '.' + EXT;
    if (state.files[nm] !== undefined) { alert('Already exists.'); return; }
    state.files[nm] = '';
    openFile(nm);
  }
  persist();
}
function renameFile(p) {
  var nn = prompt('Rename to:', p);
  if (nn == null) return;
  nn = cleanName(nn);
  if (!nn || nn === p) return;
  if (state.files[nn] !== undefined) { alert('A file with that name exists.'); return; }
  state.files[nn] = state.files[p];
  delete state.files[p];
  var i = state.open.indexOf(p);
  if (i > -1) state.open[i] = nn;
  if (state.active === p) state.active = nn;
  if (state.dirty[p]) { state.dirty[nn] = true; delete state.dirty[p]; }
  persist(); paintTree(); paintTabs();
}
function deleteFile(p) {
  var real = Object.keys(state.files).filter(function (k) { return !/\/\.keep$/.test(k); });
  if (real.length <= 1 && !/\/\.keep$/.test(p)) { alert('Keep at least one file.'); return; }
  if (!confirm('Delete ' + p + '?')) return;
  delete state.files[p];
  var i = state.open.indexOf(p);
  if (i > -1) state.open.splice(i, 1);
  if (state.active === p) {
    state.active = state.open[Math.min(i, state.open.length - 1)] || Object.keys(state.files)[0] || null;
    if (state.active) edSet(state.files[state.active]);
  }
  delete state.dirty[p];
  persist(); paintTree(); paintTabs();
}
var ctxEl = null;
function closeCtx() { if (ctxEl) { ctxEl.remove(); ctxEl = null; } }
function showCtx(x, y, items) {
  closeCtx();
  ctxEl = document.createElement('div');
  ctxEl.style.cssText = 'position:fixed;z-index:600;background:#252526;border:1px solid #454545;border-radius:8px;padding:5px;min-width:190px;box-shadow:0 12px 32px rgba(0,0,0,.5);left:' + x + 'px;top:' + y + 'px;';
  items.forEach(function (it) {
    var b = document.createElement('button');
    b.textContent = it[0];
    b.style.cssText = 'display:block;width:100%;background:none;border:0;color:#ccc;font-size:.8rem;padding:7px 10px;border-radius:5px;cursor:pointer;text-align:left;font-family:inherit;';
    b.addEventListener('mouseenter', function () { b.style.background = '#094771'; b.style.color = '#fff'; });
    b.addEventListener('mouseleave', function () { b.style.background = 'none'; b.style.color = '#ccc'; });
    b.addEventListener('click', function () { closeCtx(); it[1](); });
    ctxEl.appendChild(b);
  });
  document.body.appendChild(ctxEl);
  setTimeout(function () { document.addEventListener('click', closeCtx, { once: true }); }, 0);
}


/* ---------------- tabs ---------------- */
function paintTabs() {
  var host = $('vscTabs');
  if (!host) return;
  host.innerHTML = '';
  state.open.forEach(function (p) {
    var t = document.createElement('button');
    t.type = 'button';
    t.className = 'vsc-tab' + (p === state.active ? ' active' : '') + (state.dirty[p] ? ' dirty' : '');
    t.title = p;
    var nm = document.createElement('span'); nm.textContent = p.split('/').pop();
    var dot = document.createElement('span'); dot.className = 'dot';
    var x = document.createElement('button'); x.className = 'x'; x.textContent = '\u00d7'; x.title = 'Close';
    x.addEventListener('click', function (e) { e.stopPropagation(); closeFile(p); });
    t.appendChild(nm); t.appendChild(dot); t.appendChild(x);
    t.addEventListener('click', function () { openFile(p); });
    t.addEventListener('auxclick', function (e) { if (e.button === 1) closeFile(p); });
    t.addEventListener('dragstart', function (e) { e.dataTransfer.setData('text/plain', p); });
    t.addEventListener('dragover', function (e) { e.preventDefault(); });
    t.addEventListener('drop', function (e) {
      e.preventDefault();
      var from = e.dataTransfer.getData('text/plain');
      var a = state.open.indexOf(from), b = state.open.indexOf(p);
      if (a > -1 && b > -1 && a !== b) {
        state.open.splice(b, 0, state.open.splice(a, 1)[0]);
        persist(); paintTabs();
      }
    });
    t.draggable = true;
    host.appendChild(t);
  });
  var b = $('vscBread');
  if (b) b.innerHTML = state.active ? escH(state.active).replace(/\//g, ' <span style="opacity:.5">\u203a</span> ') + ' — <b>' + escH(LABEL) + '</b>' : '';
}
function openFile(p) {
  if (state.files[p] === undefined) return;
  syncEditorToState();
  state.active = p;
  if (state.open.indexOf(p) < 0) state.open.push(p);
  edSet(state.files[p] == null ? '' : state.files[p]);
  resetDirty(p);
  paintTabs(); paintTree(); persist();
  closeDrawer();
}
function closeFile(p) {
  var i = state.open.indexOf(p);
  if (i < 0) return;
  if (state.dirty[p] && !confirm('Close without saving? (auto-save is on, your work is kept)')) return;
  state.open.splice(i, 1);
  if (state.active === p) {
    state.active = state.open[Math.min(i, state.open.length - 1)] || null;
    if (state.active) edSet(state.files[state.active]);
  }
  paintTabs(); persist();
}
function resetDirty(p) { state.dirty[p] = false; paintTabs(); }

/* ---------------- panel ---------------- */
function ptab(name) {
  var btns = document.querySelectorAll('.vsc-ptabs button');
  for (var i = 0; i < btns.length; i++) btns[i].classList.toggle('active', btns[i].getAttribute('data-ptab') === name);
  var bodies = { out: 'vscPOut', in: 'vscPIn', prob: 'vscPProb', preview: 'vscPPreview' };
  for (var k in bodies) {
    var el = $(bodies[k]);
    if (el) el.classList.toggle('active', k === name);
  }
}
(function panelTabs() {
  var btns = document.querySelectorAll('.vsc-ptabs button');
  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function () { ptab(this.getAttribute('data-ptab')); });
  }
})();
(function resizer() {
  var bar = $('vscResize'), panel = $('vscPanel');
  if (!bar || !panel) return;
  var startY = 0, startH = 0, on = false;
  bar.addEventListener('mousedown', function (e) { on = true; startY = e.clientY; startH = panel.offsetHeight; e.preventDefault(); });
  document.addEventListener('mousemove', function (e) {
    if (!on) return;
    var h = Math.max(120, Math.min(window.innerHeight * 0.7, startH + (startY - e.clientY)));
    panel.style.height = h + 'px';
  });
  document.addEventListener('mouseup', function () { on = false; });
})();

/* ---------------- runner (wandbox sandbox) ---------------- */
var ABORT = null;
var WB_COMPILERS = { c: 'gcc-13.2.0-c', cpp: 'gcc-13.2.0', java: 'openjdk-jdk-21+35', php: 'php-8.3.12', python: 'cpython-3.10.0', javascript: 'nodejs-18.15.0' };
var WB_LABELS = { c: 'gcc 13.2', cpp: 'g++ 13.2', java: 'OpenJDK 21', php: 'PHP 8.3', python: 'Python 3.10', javascript: 'node 18.15' };
function mainFile() {
  if (state.active && state.files[state.active] !== undefined) {
    var nm = String(state.active).split('/').pop();
    if (/^main\./i.test(nm) || state.open.length <= 1) return state.active;
  }
  for (var i = 0; i < state.open.length; i++) {
    if (/^main\./i.test(String(state.open[i]).split('/').pop())) return state.open[i];
  }
  return state.active;
}
function extraCodeFiles(except) {
  return state.open.filter(function (p) { return p !== except && /\.(c|cpp|cc|h|hpp|java|php)$/i.test(p); });
}
function setRunning(on) {
  $('vscShell').classList.toggle('running', !!on);
  $('vscRunBtn').disabled = !!on;
}
function runCode() {
  syncEditorToModel();
  var mf = mainFile();
  if (!mf) { vscOut('<span class="dim">No files to run.</span>', true); return; }
  var code = state.files[mf] || '';
  if (!code.trim()) { vscOut('<span class="dim">Main file is empty.</span>', true); return; }
  var compiler = WB_COMPILERS[LANG] || 'gcc-13.2.0-c';
  var notes = [];
  if (LANG === 'java') {
    var nc = code.replace(/public\s+class\s+Main\b/, 'class Main');
    if (nc !== code) { code = nc; notes.push('Note: \u2018public\u2019 removed from Main for the sandbox'); }
  }
  var extras = extraCodeFiles(mf);
  if (extras.length && LANG !== 'php') notes.push('Only ' + mf.split('/').pop() + ' ran \u2014 extra files stay in the project/ZIP');
  setRunning(true);
  ABORT = (typeof AbortController !== 'undefined') ? new AbortController() : null;
  var __timedOut = false;
  var __to = setTimeout(function () { if (ABORT) { __timedOut = true; try { ABORT.abort(); } catch (e) {} } }, 90000);
  vscOut('<span class="dim">Compiling &amp; running\u2026</span>', true);
  ptab('out');
  $('vscRunMeta').textContent = '';
  var t0 = performance.now();
  (async function () {
    try {
      setRunnerLabel(WB_LABELS[LANG] || compiler);
      var body = { code: code, compiler: compiler, stdin: $('vscStdin').value, options: (LANG === 'c' || LANG === 'cpp') ? 'warning' : '' };
      if (extras.length) body.codes = extras.map(function (p) { return { file: p.split('/').pop(), code: state.files[p] }; });
      var res = await fetch('https://wandbox.org/api/compile.json', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        signal: ABORT ? ABORT.signal : undefined
      });
      if (!res.ok) throw new Error('runner HTTP ' + res.status);
      var j = await res.json();
      var out = j.program_output || '';
      var err = [j.compiler_error, j.program_error].filter(function (x) { return x; }).join('\n');
      window.__lastErr = err;
      var html = '';
      if (out) html += escH(out);
      if (err) html += '<span class="err">' + escH(err) + '</span>';
      if (!out && !err) html += '<span class="dim">(no output)</span>';
      vscOut(html, true);
      var ok = (j.status === '0' || j.status === 0);
      var ms = Math.round(performance.now() - t0);
      var meta = (ok ? 'Exit 0' : 'Failed') + ' \u2022 ' + ms + ' ms';
      if (notes.length) meta += ' \u2022 ' + notes.join(' \u2022 ');
      $('vscRunMeta').textContent = meta;
      if (!ok) diagnose(true);
    } catch (err) {
      if (err && err.name === 'AbortError') vscOut(__timedOut ? '<span class="err">Timed out after 90s — try smaller input.</span>' : '<span class="dim">Stopped.</span>', true);
      else vscOut('<span class="err">Runner unreachable. Check connection and retry. (' + escH(err.message || err) + ')</span>', true);
    } finally {
      try { clearTimeout(__to); } catch (e) {}
      setRunning(false); ABORT = null;
    }
  })();
}
function stopRun() {
  if (ABORT) { try { ABORT.abort(); } catch (e) {} }
  setRunning(false);
}
function setRunnerLabel(s) {
  var el = $('vscRunner');
  if (el) el.textContent = s;
}
function collectFiles() {
  syncEditorToModel();
  return state.open.filter(function (p) { return state.files[p] !== undefined; })
    .map(function (p) { return { name: p.split('/').pop(), content: state.files[p] }; });
}

/* ---------------- problems (static analyzer, local) ---------------- */
function sStripStr(line) {
  return line.replace(/"(?:[^"\\]|\\.)*"/g, '""').replace(/'(?:[^'\\]|\\.)*'/g, "''");
}
function sStripCom(line) {
  var i = line.indexOf('//');
  if (i >= 0) line = line.slice(0, i);
  if (/^(c|c\+\+|java|php)$/.test(LANG)) { var h = line.indexOf('#'); if (h >= 0 && /^\s*#/.test(line)) line = ''; }
  return line;
}
function staticChecks(code, out) {
  var lines = code.split('\n'), stack = [], pairs = { '}': '{', ')': '(', ']': '[' }, bad = null;
  lines.forEach(function (raw, i) {
    if (bad) return;
    var line = sStripCom(sStripStr(raw));
    for (var k = 0; k < line.length; k++) {
      var ch = line[k];
      if (ch === '{' || ch === '(' || ch === '[') stack.push({ ch: ch, line: i + 1 });
      else if (pairs[ch]) {
        if (!stack.length || stack[stack.length - 1].ch !== pairs[ch]) { bad = { ch: ch, line: i + 1 }; break; }
        stack.pop();
      }
    }
  });
  if (bad) out.push({ sev: 'err', t: 'Unbalanced bracket near line ' + bad.line, b: 'Found <b>' + escH(bad.ch) + '</b> with no matching opener. Check that line and the 2\u20133 above.' });
  else if (stack.length) { var t0 = stack[stack.length - 1]; out.push({ sev: 'err', t: 'Unclosed ' + escH(t0.ch) + ' from line ' + t0.line, b: 'Add the missing closer at the end of its block.' }); }
  lines.forEach(function (raw, i) {
    var line = sStripCom(raw);
    var dq = (line.match(/(?<!\\)"/g) || []).length;
    if (dq % 2 === 1) out.push({ sev: 'err', t: 'Unclosed quote on line ' + (i + 1), b: 'Odd number of <b>"</b> \u2014 close the string.' });
  });
  var ctl = /^\s*(if|else|for|while|switch|catch|try|finally|do|class|struct|enum|public|private|protected|case|default)\b/;
  if (LANG === 'c' || LANG === 'cpp' || LANG === 'java' || LANG === 'php') {
  lines.forEach(function (raw, i) {
    var line = sStripCom(raw).trim();
    if (!line || line[0] === '#' || line.slice(0, 2) === '//') return;
    if (/[;{}:]$/.test(line) || /,$/.test(line) || ctl.test(line)) return;
    if (/^\s*(import|package|#include|using)\b/.test(line) || /\)\s*$/.test(line)) return;
    if (line === '<?php' || line === '?>') return;
    out.push({ sev: 'warn', t: 'Possible missing semicolon, line ' + (i + 1), b: '<b>' + escH(line.slice(0, 70)) + '</b>' });
  });
  }
  if (LANG === 'python') {
    if (/\n\t/.test(code) && /\n    /.test(code)) out.push({ sev: 'err', t: 'Mixed tabs and spaces', b: 'Use <b>spaces only</b> (4 per level) \u2014 mixing causes TabError.' });
    lines.forEach(function (raw, i) {
      if (/^\s*(def\s+\w+.*|if\s+.*|elif\s+.*|else\s*|for\s+.*|while\s+.*|class\s+\w+.*|try\s*|except.*|finally\s*|with\s+.*)\)?\s*$/.test(raw) && !/:\s*(#.*)?$/.test(raw) && raw.trim() !== '')
        out.push({ sev: 'err', t: 'Missing colon on line ' + (i + 1), b: 'Add a trailing <b>:</b>.' });
    });
  }
  if (LANG === 'php' && !/^\s*<\?php/i.test(code)) out.push({ sev: 'warn', t: 'Missing <?php tag', b: 'Without it the code prints as text instead of running.' });
  if (LANG === 'java') {
    if (!/public\s+static\s+void\s+main/.test(code)) out.push({ sev: 'warn', t: 'No main method', b: 'Needs <b>public static void main(String[] args)</b> in class <b>Main</b>.' });
    if (!/class\s+Main\b/.test(code)) out.push({ sev: 'warn', t: 'Class is not Main', b: 'The runner launches class <b>Main</b>.' });
  }
}
var TS_RULES = [
  [/expected ['\u2018\u2019;]+ ?before/i, 'Missing semicolon/bracket above', 'Check the <b>previous</b> line for a missing <b>;</b>, <b>}</b> or <b>)</b>.'],
  [/was not declared in this scope/i, 'Undeclared identifier', 'Typo, wrong scope, or missing <b>#include</b>.'],
  [/cannot find symbol/i, 'Cannot find symbol (Java)', 'Check spelling and imports.'],
  [/NullPointerException/i, 'Null object used', 'Print the object before use or add a null check.'],
  [/ArrayIndexOutOfBoundsException|IndexOutOfBounds/i, 'Index past the end', 'Valid indexes for length n: <b>0..n-1</b>.'],
  [/Segmentation fault|segfault/i, 'Bad memory access', 'NULL/wild pointer or buffer overflow. Test tiny input.'],
  [/could not find or load main class|ClassNotFoundException/i, 'Wrong class name', 'Must match <b>public class Main</b>.'],
  [/Parse error:\s*syntax error,\s*unexpected\s*(\S+)/i, 'PHP parse error', 'Check the line <b>before</b> the reported one.'],
  [/Call to undefined function\s*(\S+)/i, 'Unknown PHP function', 'Typo or missing extension.'],
  [/division by zero|ArithmeticException/i, 'Division by zero', 'Guard the divisor.'],
  [/FileNotFoundException|No such file/i, 'File not found', 'Wrong path or working directory.']
];
function explainError(err, out) {
  var done = false;
  err.split('\n').slice(0, 6).forEach(function (line) {
    if (done) return;
    for (var k = 0; k < TS_RULES.length; k++) {
      if (TS_RULES[k][0].test(line)) {
        var title = TS_RULES[k][1].replace('{1}', '');
        out.push({ sev: 'err', t: title, b: TS_RULES[k][2] });
        done = true; break;
      }
    }
  });
  if (!done) out.push({ sev: 'warn', t: 'No known pattern', b: 'Fix only the <b>first</b> error \u2014 later ones are knock-on effects.' });
}
function renderProblems(list) {
  var host = $('vscProblems');
  host.innerHTML = '';
  if (!list.length) { host.innerHTML = '<span class="dim">No problems found. Shrink to a 10-line repro if it still fails.</span>'; }
  list.forEach(function (f) {
    var d = document.createElement('div');
    d.className = 'prob' + (f.sev === 'warn' ? ' warn' : (f.sev === 'good' ? ' good' : ''));
    var b = document.createElement('b'); b.textContent = f.t;
    var x = document.createElement('div'); x.innerHTML = f.b;
    d.appendChild(b); d.appendChild(x); host.appendChild(d);
  });
  var c = $('vscProbCount');
  if (c) c.textContent = list.length ? '(' + list.length + ')' : '';
}
function diagnose(auto) {
  syncEditorToModel();
  var code = state.active ? (state.files[state.active] || '') : '';
  var out = [];
  if (code.trim()) staticChecks(code, out);
  if (window.__lastErr) explainError(window.__lastErr, out);
  if (!out.length) out.push({ sev: 'good', t: 'Clean', b: 'No obvious issues. Read the first error line if it still fails.' });
  renderProblems(out);
  ptab('prob');
  if (!auto) $('vscPanel').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
window.__diagnose = diagnose;

/* ---------------- output helpers ---------------- */
function vscOut(html, clear) {
  var el = $('vscOut');
  if (clear) el.innerHTML = '';
  var d = document.createElement('div');
  d.innerHTML = html;
  while (d.firstChild) el.appendChild(d.firstChild);
  el.scrollTop = el.scrollHeight;
}

/* ----------------explorer ops ---------------- */
var pendingKind = 'file';
function askName(kind, done) {
  pendingKind = kind;
  var row = $('vscNewRow'), inp = $('vscNewName');
  row.classList.add('on'); inp.value = ''; inp.placeholder = kind === 'dir' ? 'dir/name (folder)' : 'name.' + EXT;
  inp.focus();
  inp.onkeydown = function (e) {
    if (e.key === 'Enter') confirmName(done);
    if (e.key === 'Escape') row.classList.remove('on');
  };
  $('vscAddBtn').onclick = function () { confirmName(done); };
}
function cleanName(s) { return (s || '').trim().replace(/[\\:*?"<>|]/g, '').replace(/^\.?\//, ''); }
function confirmName(done) {
  var inp = $('vscNewName'), nm = cleanName(inp.value);
  $('vscNewRow').classList.remove('on');
  if (!nm) return;
  if (pendingKind === 'dir') {
    if (!/\/$/.test(nm)) nm += '/';
    var key = nm + '.keep';
    if (state.files[key] !== undefined) { alert('Already exists.'); return; }
    state.files[key] = '';
    if (state.open.indexOf(key) < 0) state.open.push(key);
    openFile(key);
  } else {
    if (nm.indexOf('.') < 0) nm += '.' + EXT;
    if (state.files[nm] !== undefined) { alert('Already exists.'); return; }
    state.files[nm] = '';
    openFile(nm);
  }
  persist();
  if (done) done();
}
function renameFile(p) {
  var nn = prompt('Rename to:', p);
  if (nn == null) return;
  nn = cleanName(nn);
  if (!nn || nn === p) return;
  if (state.files[nn] !== undefined) { alert('A file with that name exists.'); return; }
  state.files[nn] = state.files[p];
  delete state.files[p];
  var i = state.open.indexOf(p);
  if (i > -1) state.open[i] = nn;
  if (state.active === p) state.active = nn;
  if (state.dirty[p]) { state.dirty[nn] = true; delete state.dirty[p]; }
  persist(); paintTree(); paintTabs();
}
function deleteFile(p) {
  var sibs = Object.keys(state.files).filter(function (k) { return !/\/\.keep$/.test(k); });
  if (sibs.length <= 1 && !/\/\.keep$/.test(p)) { alert('Keep at least one file.'); return; }
  if (!confirm('Delete ' + p + '?')) return;
  delete state.files[p];
  // remove orphaned folder placeholders is unnecessary; drop empty .keep of same dir
  var i = state.open.indexOf(p);
  if (i > -1) state.open.splice(i, 1);
  if (state.active === p) {
    state.active = state.open[state.open.length - 1] || Object.keys(state.files)[0] || null;
    if (state.active) edSet(state.files[state.active]);
  }
  delete state.dirty[p];
  persist(); paintTree(); paintTabs();
}
var ctxEl = null;
function closeCtx() { if (ctxEl) { ctxEl.remove(); ctxEl = null; } }
function showCtx(x, y, items) {
  closeCtx();
  ctxEl = document.createElement('div');
  ctxEl.style.cssText = 'position:fixed;z-index:600;background:#252526;border:1px solid #454545;border-radius:8px;padding:5px;min-width:190px;box-shadow:0 12px 32px rgba(0,0,0,.5);left:' + x + 'px;top:' + y + 'px;';
  items.forEach(function (it) {
    var b = document.createElement('button');
    b.textContent = it[0];
    b.style.cssText = 'display:block;width:100%;background:none;border:0;color:#ccc;font-size:.8rem;padding:7px 10px;border-radius:5px;cursor:pointer;text-align:left;font-family:inherit;';
    b.addEventListener('mouseenter', function () { b.style.background = '#094771'; b.style.color = '#fff'; });
    b.addEventListener('mouseleave', function () { b.style.background = 'none'; b.style.color = '#ccc'; });
    b.addEventListener('click', function () { closeCtx(); it[1](); });
    ctxEl.appendChild(b);
  });
  document.body.appendChild(ctxEl);
  setTimeout(function () { document.addEventListener('click', closeCtx, { once: true }); }, 0);
}

/* ---------------- files <-> editor sync ---------------- */
function syncEditorToModel() {
  if (!state.active) return;
  state.files[state.active] = edGet();
}
function syncEditorToState() { syncEditorToModel(); }

/* ---------------- palette ---------------- */
var PAL_CMDS = [
  ['Run code', 'Ctrl+Enter', function () { runCode(); }],
  ['Stop', '', function () { stopRun(); }],
  ['Diagnose problems', '', function () { diagnose(false); }],
  ['Download project ZIP', '', function () { zipProject(); }],
  ['Import ZIP', '', function () { $('vscZipIn').click(); }],
  ['Share link (copy)', '', function () { shareLink(); }],
  ['Toggle sidebar', 'Ctrl+B', function () { toggleSide(); }],
  ['Toggle theme', '', function () { cycleTheme(); }],
  ['Fullscreen', '', function () { toggleFull(); }],
  ['Go to line', 'Ctrl+G', function () { gotoLine(); }],
  ['Find', 'Ctrl+F', function () { findAct(); }],
  ['Format document', 'Shift+Alt+F', function () { formatDoc(); }],
  ['Increase font', 'Ctrl+=', function () { zoomFont(1); }],
  ['Decrease font', 'Ctrl+-', function () { zoomFont(-1); }]
];
var palMode = 'cmd', palSel = 0, palItems = [];
function openPalette(mode) {
  palMode = mode || 'cmd'; palSel = 0;
  $('vscOverlay').classList.add('on');
  var inp = $('vscPalInput');
  inp.value = mode === 'files' ? '' : '>';
  inp.placeholder = mode === 'files' ? 'Open file by name\u2026' : 'Type a command\u2026';
  renderPal('');
  setTimeout(function () { inp.focus(); }, 30);
}
function closePalette() { $('vscOverlay').classList.remove('on'); }
function palCandidates(q) {
  q = (q || '').toLowerCase();
  var out = [];
  if (palMode === 'files' || (palMode === 'cmd' && q.charAt(0) !== '>')) {
    Object.keys(state.files).forEach(function (p) {
      if (!q || p.toLowerCase().indexOf(q) > -1) out.push({ t: p, s: 'file', fn: function () { openFile(p); } });
    });
    if (palMode === 'files') return out;
    q = q.replace(/^>/, '');
  } else q = q.replace(/^>/, '');
  PAL_CMDS.forEach(function (c) {
    if (!q || c[0].toLowerCase().indexOf(q) > -1) out.push({ t: c[0], s: c[1], fn: c[2] });
  });
  return out.slice(0, 12);
}
function renderPal(q) {
  palItems = palCandidates(q);
  if (palSel >= palItems.length) palSel = 0;
  var host = $('vscPalItems');
  host.innerHTML = '';
  palItems.forEach(function (it, i) {
    var d = document.createElement('div');
    d.className = 'item' + (i === palSel ? ' sel' : '');
    var a = document.createElement('span'); a.textContent = it.t;
    var b = document.createElement('small'); b.textContent = it.s;
    d.appendChild(a); d.appendChild(b);
    d.addEventListener('click', function () { closePalette(); it.fn(); });
    d.addEventListener('mousemove', function () { palSel = i; renderPal($('vscPalInput').value); });
    host.appendChild(d);
  });
  var sel = host.children[palSel];
  if (sel) sel.scrollIntoView({ block: 'nearest' });
}

/* ---------------- menus ---------------- */
function closeMenus() {
  var ms = document.querySelectorAll('.vsc-menu.open');
  for (var i = 0; i < ms.length; i++) ms[i].classList.remove('open');
}
function menuItems(id, defs) {
  var host = $(id);
  if (!host) return;
  host.innerHTML = '';
  defs.forEach(function (d) {
    if (d === '-') { var hr = document.createElement('hr'); host.appendChild(hr); return; }
    var b = document.createElement('button');
    var t = document.createElement('span'); t.textContent = d[0];
    var k = document.createElement('kbd'); k.textContent = d[1] || '';
    b.appendChild(t); b.appendChild(k);
    b.addEventListener('click', function () { closeMenus(); d[2](); });
    host.appendChild(b);
  });
}
function buildMenus() {
  menuItems('menuFile', [
    ['Back to Vytra home', '', function () { location.href = '../'; }],
    ['New file', '', function () { askName('file'); }],
    ['New folder', '', function () { askName('dir'); }],
    ['-', ''],
    ['Download project ZIP', '', function () { zipProject(); }],
    ['Import ZIP', '', function () { $('vscZipIn').click(); }],
    ['Share link (copy)', '', function () { shareLink(); }],
    ['-', ''],
    ['Load example\u2026', '', function () { exampleMenu(); }]
  ]);
  menuItems('menuEdit', [
    ['Find', 'Ctrl+F', function () { findAct(); }],
    ['Replace', 'Ctrl+H', function () { replaceAct(); }],
    ['Go to line', 'Ctrl+G', function () { gotoLine(); }],
    ['Format document', 'Shift+Alt+F', function () { formatDoc(); }]
  ]);
  menuItems('menuView', [
    ['Toggle sidebar', 'Ctrl+B', function () { toggleSide(); }],
    ['Toggle theme', '', function () { cycleTheme(); }],
    ['Increase font', 'Ctrl+=', function () { zoomFont(1); }],
    ['Decrease font', 'Ctrl+-', function () { zoomFont(-1); }],
    ['Fullscreen', '', function () { toggleFull(); }]
  ]);
  menuItems('menuRun', [
    ['Run code', 'Ctrl+Enter', function () { runCode(); }],
    ['Stop', '', function () { stopRun(); }],
    ['Diagnose problems', '', function () { diagnose(false); }]
  ]);
  var ms = document.querySelectorAll('.vsc-menu > button');
  for (var i = 0; i < ms.length; i++) {
    (function (btn) {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var w = btn.parentElement, was = w.classList.contains('open');
        closeMenus();
        if (!was) w.classList.add('open');
      });
    })(ms[i]);
  }
  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('.vsc-menu')) closeMenus();
  });
}

/* ---------------- actions ---------------- */
function toggleSide() {
  var s = $('vscSide');
  if (window.innerWidth <= 900) s.classList.toggle('drawer');
  else s.classList.toggle('hidden');
}
function closeDrawer() {
  var s = $('vscSide');
  if (s && window.innerWidth <= 900) s.classList.remove('drawer');
}
function cycleTheme() {
  settings.theme = (settings.theme === 'vs-dark') ? 'vs' : 'vs-dark';
  saveSettings(); applySettings();
}
function zoomFont(d) {
  settings.fontSize = Math.max(10, Math.min(28, settings.fontSize + d));
  saveSettings(); applySettings();
}
function toggleFull() {
  var sh = $('vscShell');
  if (!document.fullscreenElement) { if (sh.requestFullscreen) sh.requestFullscreen(); }
  else if (document.exitFullscreen) document.exitFullscreen();
}
function gotoLine() {
  if (monacoOK && editor) { try { editor.getAction('editor.action.gotoLine').run(); return; } catch (e) {} }
  var v = prompt('Go to line:');
  var n = parseInt(v, 10);
  if (!isNaN(n) && fallbackTa) {
    var lines = fallbackTa.value.split('\n'), pos = 0;
    for (var i = 0; i < Math.min(n - 1, lines.length); i++) pos += lines[i].length + 1;
    fallbackTa.focus(); fallbackTa.setSelectionRange(pos, pos);
  }
}
function findAct() {
  if (monacoOK && editor) { try { editor.getAction('editor.actions.findWithArgs').run({ searchString: '' }); return; } catch (e) {} }
  openPalette('cmd');
  $('vscPalInput').value = '>Find';
  renderPal('>Find');
}
function replaceAct() {
  if (monacoOK && editor) { try { editor.getAction('editor.action.startFindReplaceAction').run(); return; } catch (e) {} }
}
function formatDoc() {
  if (monacoOK && editor) { try { editor.getAction('editor.action.formatDocument').run(); return; } catch (e) {} }
}
function exampleMenu() {
  var list = EXAMPLES[LANG] || [];
  if (!list.length) { alert('No examples for this language yet.'); return; }
  showCtxList(list.map(function (e) { return e.name; }), function (name) {
    var ex = null;
    list.forEach(function (e) { if (e.name === name) ex = e; });
    if (!ex) return;
    if (!confirm('Replace project with example "' + name + '"?')) return;
    state.files = {}; for (var k in ex.files) state.files[k] = ex.files[k];
    state.open = Object.keys(state.files); state.active = state.open[0];
    edSet(state.files[state.active] || '');
    paintTree(); paintTabs(); persist();
  });
}
function showCtxList(names, done) {
  showCtx(window.innerWidth / 2 - 120, 120, names.map(function (n) { return [n, function () { done(n); }]; }));
}
function zipProject() {
  if (typeof JSZip === 'undefined') { alert('ZIP library still loading \u2014 try again in a moment.'); return; }
  syncEditorToModel();
  var zip = new JSZip(), names = Object.keys(state.files);
  if (!names.length) { alert('Project is empty.'); return; }
  names.forEach(function (n) { zip.file(n, state.files[n] == null ? '' : state.files[n]); });
  zip.generateAsync({ type: 'blob' }).then(function (blob) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'vytra-' + LANG + '-project.zip';
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 800);
  }).catch(function (e) { alert('ZIP failed: ' + e.message); });
}
function importZip(file) {
  if (typeof JSZip === 'undefined') { alert('ZIP library still loading \u2014 try again in a moment.'); return; }
  JSZip.loadAsync(file).then(function (zip) {
    var jobs = [];
    zip.forEach(function (rel, entry) {
      if (!entry.dir) jobs.push(entry.async('string').then(function (txt) { return { n: rel, t: txt }; }));
    });
    return Promise.all(jobs);
  }).then(function (items) {
    var ok = 0;
    items.forEach(function (it) {
      if (/\.(c|h|cpp|hpp|cc|java|php|txt|md|json|sql)$/i.test(it.n) && it.t.length < 200000) {
        state.files[it.n] = it.t; ok++;
      }
    });
    if (!ok) { alert('No code files found in that ZIP.'); return; }
    state.open = Object.keys(state.files); state.active = state.open[0];
    edSet(state.files[state.active] || '');
    paintTree(); paintTabs(); persist();
  }).catch(function (e) { alert('Import failed: ' + e.message); });
}
function shareLink() {
  syncEditorToModel();
  try {
    var data = { f: state.files, s: $('vscStdin').value, l: LANG };
    var raw = unescape(encodeURIComponent(JSON.stringify(data)));
    var h = '#s=' + btoa(raw).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    var url = location.href.split('#')[0] + h;
    var done = function () { alert('Share link copied. Anyone opening it loads this project.'); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(done, function () { prompt('Copy link:', url); });
    else prompt('Copy link:', url);
  } catch (e) { alert('Share failed: ' + e.message); }
}

/* ---------------- shortcuts ---------------- */
document.addEventListener('keydown', function (e) {
  var inShell = e.target && e.target.closest && e.target.closest('.vsc-shell');
  var palOpen = $('vscOverlay').classList.contains('on');
  if (palOpen) {
    if (e.key === 'Escape') closePalette();
    else if (e.key === 'ArrowDown') { e.preventDefault(); palSel = Math.min(palSel + 1, palItems.length - 1); renderPal($('vscPalInput').value); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); palSel = Math.max(palSel - 1, 0); renderPal($('vscPalInput').value); }
    else if (e.key === 'Enter') { e.preventDefault(); if (palItems[palSel]) { var fn = palItems[palSel].fn; closePalette(); fn(); } }
    return;
  }
  if (!inShell) return;
  var mod = e.ctrlKey || e.metaKey;
  if (mod && e.shiftKey && (e.key === 'P' || e.key === 'p')) { e.preventDefault(); openPalette('cmd'); }
  else if (mod && (e.key === 'p' || e.key === 'P')) { e.preventDefault(); openPalette('files'); }
  else if (mod && e.shiftKey && (e.key === 'V' || e.key === 'v')) { e.preventDefault(); buildPreview(); }
  else if (mod && (e.key === 'b' || e.key === 'B')) { e.preventDefault(); toggleSide(); }
  else if (mod && (e.key === 's' || e.key === 'S')) { e.preventDefault(); syncEditorToModel(); persist(); flashStatus('Saved locally'); }
  else if (mod && e.key === 'Enter') { e.preventDefault(); runCode(); }
  else if (mod && (e.key === 'g' || e.key === 'G')) { e.preventDefault(); gotoLine(); }
  else if (mod && (e.key === '=' || e.key === '+')) { e.preventDefault(); zoomFont(1); }
  else if (mod && (e.key === '-' || e.key === '_')) { e.preventDefault(); zoomFont(-1); }
});
function flashStatus(msg) {
  var el = $('vscFiles');
  if (!el) return;
  var old = el.textContent;
  el.textContent = msg;
  setTimeout(function () { refreshStatus(); }, 1200);
}

/* ---------------- settings ---------------- */
function openSettings() {
  $('setTheme').value = settings.theme;
  $('setFont').value = settings.fontSize;
  $('setTab').value = settings.tabSize;
  $('setWrap').checked = (settings.wrap === 'on');
  $('setMini').checked = !!settings.minimap;
  $('vscSettingsOv').classList.add('on');
}
function closeSettings() { $('vscSettingsOv').classList.remove('on'); }

function syncLangUI() {
  var short = { c: 'C', cpp: 'C++', java: 'Java', php: 'PHP', python: 'Python', javascript: 'JS' }[LANG] || LANG;
  var sel = $('vscLangSel');
  if (sel) sel.value = LANG;
  var ls = $('vscLangSt');
  if (ls) ls.textContent = short;
}
function switchLanguage(key) {
  if (!LANGS[key] || key === LANG) return;
  syncEditorToModel(); persist();
  applyLangVars(key);
  state = { files: {}, open: [], active: null, dirty: {} };
  viewStates = {};
  loadProject();
  if (monacoOK && editor) { try { monaco.editor.setModelLanguage(editor.getModel(), MONACO_LANG); } catch (e) {} }
  edSet(state.active ? state.files[state.active] : '');
  paintTree(); paintTabs(); refreshStatus();
  syncLangUI();
  setRunnerLabel((WB_LABELS[LANG] || LANG) + ' (sandbox)');
  try { history.replaceState(null, '', key === 'c' ? location.pathname : '?lang=' + key); } catch (e) {}
}
window.__switchLanguage = switchLanguage;
['c', 'cpp', 'java', 'php', 'python', 'javascript'].forEach(function (k) {
  PAL_CMDS.push(['Language: ' + LANGS[k].label, '', (function (kk) { return function () { switchLanguage(kk); }; })(k)]);
});

/* ---------------- activity bar + misc wiring ---------------- */
function wireChrome() {
  var acts = document.querySelectorAll('.vsc-activity button');
  for (var i = 0; i < acts.length; i++) {
    (function (b) {
      b.addEventListener('click', function () {
        var a = b.getAttribute('data-act');
        for (var j = 0; j < acts.length; j++) acts[j].classList.remove('active');
        b.classList.add('active');
        if (a === 'files') toggleSide();
        else if (a === 'run') runCode();
        else if (a === 'zip') zipProject();
        else if (a === 'settings') openSettings();
      });
    })(acts[i]);
  }
  on($('vscMenuBtn'), 'click', toggleSide);
  on($('vscLangSel'), 'change', function () { switchLanguage($('vscLangSel').value); });
  on($('vscNewFile'), 'click', function () { askName('file'); });
  on($('vscNewFolder'), 'click', function () { askName('dir'); });
  on($('vscAddBtn'), 'click', function () { confirmName(); });
  on($('vscRunBtn'), 'click', runCode);
  on($('vscStopBtn'), 'click', stopRun);
  on($('vscFab'), 'click', runCode);
  on($('vscFullBtn'), 'click', toggleFull);
  on($('setClose'), 'click', closeSettings);
  on($('setSave'), 'click', function () {
    settings.theme = $('setTheme').value;
    settings.fontSize = Math.max(10, Math.min(28, parseInt($('setFont').value, 10) || 14));
    settings.tabSize = Math.max(2, Math.min(8, parseInt($('setTab').value, 10) || 4));
    settings.wrap = $('setWrap').checked ? 'on' : 'off';
    settings.minimap = $('setMini').checked;
    saveSettings(); applySettings(); closeSettings();
    var el = $('vscTabSize'); if (el) el.textContent = settings.tabSize;
  });
  on($('vscOverlay'), 'click', function (e) { if (e.target === $('vscOverlay')) closePalette(); });
  var inp = $('vscPalInput');
  on(inp, 'input', function () { palSel = 0; renderPal(inp.value); });
  var zipIn = document.createElement('input');
  zipIn.type = 'file'; zipIn.accept = '.zip'; zipIn.id = 'vscZipIn'; zipIn.style.display = 'none';
  zipIn.addEventListener('change', function () { if (zipIn.files[0]) importZip(zipIn.files[0]); zipIn.value = ''; });
  document.body.appendChild(zipIn);
  if (window.innerWidth <= 900) { var mb = $('vscMenuBtn'); if (mb) mb.style.display = ''; }
}

/* ---------------- website preview (static HTML/CSS/JS) ---------------- */
var SITE_STARTER = {
'index.html': '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>My Site</title>\n<link rel="stylesheet" href="styles.css">\n</head>\n<body>\n  <main class="card">\n    <h1 id="title">Hello, web!</h1>\n    <p>Built in Vytra IDE. Edit me.</p>\n    <button id="btn">Clicks: 0</button>\n  </main>\n<script src="app.js"><\/script>\n</body>\n</html>\n',
'styles.css': 'body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;display:flex;min-height:100vh;margin:0;align-items:center;justify-content:center;}\n.card{background:#1e293b;padding:40px;border-radius:16px;text-align:center;}\nbutton{background:#E5322D;color:#fff;border:0;padding:10px 22px;border-radius:8px;font-size:1rem;cursor:pointer;}\n',
'app.js': 'var n = 0;\nvar b = document.getElementById("btn");\nif(b){ b.addEventListener("click", function(){ n++; b.textContent = "Clicks: " + n; }); }\n'
};
function previewFiles() {
  var htmls = Object.keys(state.files).filter(function (p) { return /\.html?$/i.test(p) && !/\/\.keep$/.test(p); });
  htmls.sort(function (a, b) {
    var ai = /index\.html?$/i.test(a) ? 0 : 1, bi = /index\.html?$/i.test(b) ? 0 : 1;
    return (ai - bi) || (a.length - b.length);
  });
  return htmls;
}
function findAsset(ref, extRe) {
  var base = String(ref).split('?')[0].split('#')[0];
  if (/^(https?:|data:|blob:|\/\/)/i.test(base)) return null;
  var name = base.split('/').pop().toLowerCase();
  if (!name) return null;
  var keys = Object.keys(state.files);
  for (var i = 0; i < keys.length; i++) {
    if (keys[i].split('/').pop().toLowerCase() === name && extRe.test(keys[i])) return keys[i];
  }
  return null;
}
function buildPreview() {
  syncEditorToModel();
  var list = previewFiles();
  var frame = $('vscPreviewFrame'), empty = $('vscPreviewEmpty');
  if (!list.length) {
    if (frame) frame.style.display = 'none';
    if (empty) { empty.style.display = ''; empty.innerHTML = 'No website yet \u2014 create an <b>index.html</b> file, or File menu \u2192 New website project.'; }
    ptab('preview');
    return;
  }
  var doc = state.files[list[0]];
  doc = doc.replace(/<link\b[^>]*href="([^"]+)"[^>]*>/gi, function (m, href) {
    var k = findAsset(href, /\.css$/i);
    if (k) return '<style>\n' + state.files[k] + '\n</style>';
    return m;
  });
  doc = doc.replace(/<script\b[^>]*src="([^"]+)"[^>]*>\s*<\/script>/gi, function (m, src) {
    var k = findAsset(src, /\.js$/i);
    if (k) return '<script>\n' + state.files[k].replace(/<\/script/gi, '<\\/script') + '\n<' + '/script>';
    return m;
  });
  var hook = '<script>(function(){function s(a){try{parent.postMessage({vytraConsole:a},\'*\');}catch(e){}}window.addEventListener(\'error\',function(e){s(\'error: \'+(e.message||\'unknown\'));});var fns=[\'log\',\'warn\',\'error\'];fns.forEach(function(k){var f=console[k].bind(console);console[k]=function(){try{var t=Array.prototype.map.call(arguments,function(a){try{return typeof a===\'object\'?JSON.stringify(a):String(a);}catch(x){return String(a);}}).join(\' \');s(k+\': \'+t);}catch(x){} return f.apply(null,arguments);};});})();<' + '/script>';
  if (/<head\b[^>]*>/i.test(doc)) doc = doc.replace(/<head\b[^>]*>/i, function (m) { return m + hook; });
  else doc = hook + doc;
  if (window.__prevUrl) { try { URL.revokeObjectURL(window.__prevUrl); } catch (e) {} }
  window.__prevUrl = URL.createObjectURL(new Blob([doc], { type: 'text/html' }));
  if (frame) { frame.style.display = ''; frame.src = window.__prevUrl; }
  if (empty) empty.style.display = 'none';
  ptab('preview');
}
function newWebsiteProject() {
  if (!confirm('Replace project with a website starter (index.html + styles.css + app.js)?')) return;
  state.files = {}; for (var k in SITE_STARTER) state.files[k] = SITE_STARTER[k];
  state.open = Object.keys(state.files); state.active = 'index.html';
  edSet(state.files[state.active] || '');
  paintTree(); paintTabs(); persist();
  buildPreview();
}
(function initPreview(){
  var fb = $('vscFullBtn');
  if (fb && !$('vscPrevBtn')) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'vsc-iconbtn'; b.id = 'vscPrevBtn'; b.title = 'Preview website';
    b.innerHTML = '&#127760;';
    fb.parentElement.insertBefore(b, fb);
    b.addEventListener('click', buildPreview);
  }
  var mr = $('menuRun');
  if (mr && !$('vscPrevMenu')) {
    var mb = document.createElement('button');
    mb.id = 'vscPrevMenu';
    mb.innerHTML = '<span>Preview website</span><span><kbd>Ctrl+Shift+V</kbd></span>';
    mb.addEventListener('click', function () { closeMenus(); buildPreview(); });
    mr.appendChild(mb);
  }
  var mf = $('menuFile');
  if (mf && !$('vscWebItem')) {
    var w = document.createElement('button');
    w.id = 'vscWebItem';
    w.innerHTML = '<span>New website project</span><span></span>';
    w.addEventListener('click', function () { closeMenus(); newWebsiteProject(); });
    mf.appendChild(w);
  }
  PAL_CMDS.push(['Preview website', 'Ctrl+Shift+V', function () { buildPreview(); }]);
  PAL_CMDS.push(['New website project', '', function () { newWebsiteProject(); }]);
  window.addEventListener('message', function (e) {
    if (e && e.data && typeof e.data.vytraConsole === 'string') {
      var el = $('vscOut');
      if (!el) return;
      var d = document.createElement('div');
      d.innerHTML = '<span class="dim">[preview]</span> ' + escH(String(e.data.vytraConsole)).slice(0, 500);
      el.appendChild(d); el.scrollTop = el.scrollHeight;
    }
  });
})();

/* ---------------- boot ---------------- */
window.addEventListener('error', function (e) {
  try {
    var el = document.getElementById('vscOut');
    if (el && window.__ideBooted) {
      var d = document.createElement('div');
      d.style.cssText = 'color:#fca5a5;font-size:.8rem;margin-top:8px;';
      d.textContent = 'JS error: ' + (e.message || 'unknown');
      el.appendChild(d);
    }
  } catch (x) {}
});
window.__ideBooted = false;
try {
  loadProject();
  buildMenus();
  wireChrome();
  paintTree();
} catch (e) {
  try {
    var el0 = document.getElementById('vscOut');
    if (el0) el0.innerHTML = '<span class="err">Startup failed: ' + escH(e.message || e) + ' — try hard refresh (Ctrl+Shift+R).</span>';
  } catch (x) {}
  if (window.console && console.error) console.error(e);
}
window.__ideBooted = true;
bootMonaco().then(function (ok) {
  if (ok) initMonaco();
  else initFallback();
  paintTabs();
  refreshStatus();
  var el = $('vscTabSize'); if (el) el.textContent = settings.tabSize;
  syncLangUI();
  setRunnerLabel((WB_LABELS[LANG] || LANG) + ' (sandbox)');
});

})();
