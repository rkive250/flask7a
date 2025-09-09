const CACHE_NAME = "landing-cache-v1";
const archivos = [
  "/",
  "/index.html",
  "/styles.css",
  "/app.js"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(archivos))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(resp => resp || fetch(event.request))
  );
});
