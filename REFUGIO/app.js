if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(() => console.log("✅ Service Worker registrado"))
    .catch(err => console.error("❌ Error registrando SW:", err));
}
