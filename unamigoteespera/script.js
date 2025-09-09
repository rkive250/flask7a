// Cargar datos de la "DB" (JSON)
fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const lista = document.getElementById('lista-padrinos');
    data.padrinos.forEach(padrino => {
      const li = document.createElement('li');
      li.innerHTML = `
        <strong>${padrino.nombre}</strong> - Apadrina a: ${padrino.animal_apadrinado}<br>
        Monto: ${padrino.monto} | Desde: ${padrino.fecha_inicio}
      `;
      lista.appendChild(li);
    });
  })
  .catch(error => console.error('Error al cargar datos:', error));

// Registrar Service Worker para offline
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(reg => console.log('SW registrado:', reg))
      .catch(err => console.error('Error en SW:', err));
  });
}