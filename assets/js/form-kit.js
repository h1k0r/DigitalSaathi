/* Vytra Form-Kit engine — shared client-side helpers for image/form tools.
   Everything runs in the browser. No file ever leaves the device. */
window.VytraImage = (function () {
  "use strict";

  function fmtSize(b) {
    if (b < 1024) return b + " B";
    if (b < 1048576) return (b / 1024).toFixed(1) + " KB";
    return (b / 1048576).toFixed(2) + " MB";
  }

  function loadFile(file) {
    return new Promise(function (res, rej) {
      var url = URL.createObjectURL(file);
      var img = new Image();
      img.onload = function () { res(img); URL.revokeObjectURL(url); };
      img.onerror = function () { rej(new Error("Could not read image")); URL.revokeObjectURL(url); };
      img.src = url;
    });
  }

  function drawScaled(img, w, h) {
    var c = document.createElement("canvas");
    c.width = Math.max(1, Math.round(w));
    c.height = Math.max(1, Math.round(h));
    var x = c.getContext("2d");
    x.imageSmoothingEnabled = true;
    x.imageSmoothingQuality = "high";
    x.drawImage(img, 0, 0, c.width, c.height);
    return c;
  }

  /* Fit inside maxW x maxH keeping aspect ratio (never upscales). */
  function fitInto(iw, ih, maxW, maxH) {
    var s = 1;
    if (maxW) s = Math.min(s, maxW / iw);
    if (maxH) s = Math.min(s, maxH / ih);
    if (s < 1) return [Math.max(1, Math.round(iw * s)), Math.max(1, Math.round(ih * s))];
    return [iw, ih];
  }

  function scaleCanvas(canvas, s) {
    var c = document.createElement("canvas");
    c.width = Math.max(1, Math.round(canvas.width * s));
    c.height = Math.max(1, Math.round(canvas.height * s));
    var x = c.getContext("2d");
    x.imageSmoothingEnabled = true;
    x.imageSmoothingQuality = "high";
    x.drawImage(canvas, 0, 0, c.width, c.height);
    return c;
  }

  function toBlob(canvas, type, q) {
    return new Promise(function (res) {
      canvas.toBlob(function (b) { res(b); }, type, q);
    });
  }

  /* Encode canvas to a blob at or under targetKB.
     Binary-searches quality; if even minQ overshoots, scales the canvas
     down and repeats. Returns { blob, width, height, quality, scale, ok }.
     For PNG (lossless) quality is ignored — scale loop only. */
  async function encodeToTarget(canvas, opts) {
    var target = Math.max(1, opts.targetKB) * 1024;
    var type = opts.type || "image/jpeg";
    var minQ = opts.minQ != null ? opts.minQ : 0.35;
    var maxQ = opts.maxQ != null ? opts.maxQ : 0.95;
    var lossless = type === "image/png";
    var scale = 1, cur = canvas;

    for (var round = 0; round < 7; round++) {
      cur = scale === 1 ? canvas : scaleCanvas(canvas, scale);
      if (lossless) {
        var b0 = await toBlob(cur, type, 1);
        if (b0 && b0.size <= target) {
          return { blob: b0, width: cur.width, height: cur.height, quality: 1, scale: scale, ok: true };
        }
      } else {
        var lo = minQ, hi = maxQ, best = null, bestQ = minQ;
        for (var i = 0; i < 8; i++) {
          var q = (lo + hi) / 2;
          var blob = await toBlob(cur, type, q);
          if (!blob) break;
          if (blob.size <= target) { best = blob; bestQ = q; lo = q; } else { hi = q; }
          if (best && (hi - lo) < 0.015) break;
        }
        if (best) {
          return { blob: best, width: cur.width, height: cur.height, quality: bestQ, scale: scale, ok: true };
        }
      }
      scale *= 0.85;
    }
    /* Last resort: report the smallest we got so the user sees a real number. */
    var last = await toBlob(cur, type, lossless ? 1 : minQ);
    return { blob: last, width: cur.width, height: cur.height, quality: minQ, scale: scale, ok: false };
  }

  /* Push near-white paper to pure white and deepen ink — signature cleanup. */
  function whiten(canvas, thresh) {
    thresh = thresh || 185;
    var x = canvas.getContext("2d");
    var d = x.getImageData(0, 0, canvas.width, canvas.height);
    var p = d.data;
    for (var i = 0; i < p.length; i += 4) {
      var lum = p[i] * 0.299 + p[i + 1] * 0.587 + p[i + 2] * 0.114;
      if (lum >= thresh) { p[i] = p[i + 1] = p[i + 2] = 255; }
      else if (lum < 80) { p[i] = p[i + 1] = p[i + 2] = 0; }
    }
    x.putImageData(d, 0, 0);
  }

  function grayscale(canvas) {
    var x = canvas.getContext("2d");
    var d = x.getImageData(0, 0, canvas.width, canvas.height);
    var p = d.data;
    for (var i = 0; i < p.length; i += 4) {
      var lum = p[i] * 0.299 + p[i + 1] * 0.587 + p[i + 2] * 0.114;
      p[i] = p[i + 1] = p[i + 2] = lum;
    }
    x.putImageData(d, 0, 0);
  }

  /* Fraction of edge pixels that look like plain white paper (0..1). */
  function edgeWhiteness(canvas) {
    var x = canvas.getContext("2d");
    var w = canvas.width, h = canvas.height;
    var d = x.getImageData(0, 0, w, h).data;
    var white = 0, total = 0, stepX = Math.max(1, Math.round(w / 120));
    function px(cx, cy) {
      var i = ((cy | 0) * w + (cx | 0)) * 4;
      return d[i] * 0.299 + d[i + 1] * 0.587 + d[i + 2] * 0.114;
    }
    for (var cx = 0; cx < w; cx += stepX) {
      for (var e = 0; e < 3; e++) {
        total++; if (px(cx, e) > 232) white++;
        total++; if (px(cx, h - 1 - e) > 232) white++;
      }
    }
    var stepY = Math.max(1, Math.round(h / 120));
    for (var cy = 0; cy < h; cy += stepY) {
      for (var e2 = 0; e2 < 3; e2++) {
        total++; if (px(e2, cy) > 232) white++;
        total++; if (px(w - 1 - e2, cy) > 232) white++;
      }
    }
    return total ? white / total : 0;
  }

  function download(blob, name) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
  }

  return {
    fmtSize: fmtSize, loadFile: loadFile, drawScaled: drawScaled, fitInto: fitInto,
    encodeToTarget: encodeToTarget, scaleCanvas: scaleCanvas, toBlob: toBlob,
    whiten: whiten, grayscale: grayscale, edgeWhiteness: edgeWhiteness, download: download
  };
})();

/* Privacy proof: count only file-bearing upload requests (FormData/File/Blob/
   ArrayBuffer bodies). Text beacons (analytics) are not counted. Rendered
   into any element carrying [data-vp]. */
window.VytraPrivacy = (function () {
  "use strict";
  var reqs = 0, bytes = 0;
  function isFileBody(b) {
    return (typeof FormData !== "undefined" && b instanceof FormData) ||
           (typeof File !== "undefined" && b instanceof File) ||
           (typeof Blob !== "undefined" && b instanceof Blob) ||
           (typeof ArrayBuffer !== "undefined" && b instanceof ArrayBuffer) ||
           (typeof ArrayBuffer !== "undefined" && ArrayBuffer.isView && ArrayBuffer.isView(b));
  }
  function sizeOf(b) {
    if (typeof b === "string") return b.length;
    if (b && typeof b.size === "number") return b.size;
    if (b && typeof b.byteLength === "number") return b.byteLength;
    return 0;
  }
  var origFetch = window.fetch;
  if (origFetch) {
    window.fetch = function (input, init) {
      try { if (init && isFileBody(init.body)) { reqs++; bytes += sizeOf(init.body); } } catch (e) {}
      return origFetch.apply(this, arguments);
    };
  }
  var origSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function (b) {
    try { if (isFileBody(b)) { reqs++; bytes += sizeOf(b); } } catch (e) {}
    return origSend.apply(this, arguments);
  };
  function render() {
    var html = "\uD83D\uDD12 File-upload requests since page load: <b>" + reqs +
      "</b> &middot; <b>" + bytes + " bytes</b> — processing is 100% in your browser";
    document.querySelectorAll("[data-vp]").forEach(function (el) { el.innerHTML = html; });
  }
  document.addEventListener("DOMContentLoaded", function () {
    render();
    setInterval(render, 2000);
  });
  return { get reqs() { return reqs; }, get bytes() { return bytes; } };
})();
