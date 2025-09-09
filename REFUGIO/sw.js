const CACHE_NAME = "landing-cache-v1";
const archivos = [
  "/",
  "/index.html",
  "/styles.css",
  "/app.js",
  "/libros.json"
];

// Instalar Service Worker
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(archivos))
  );
});

// Interceptar solicitudes
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(resp => resp || fetch(event.request))
  );
});
