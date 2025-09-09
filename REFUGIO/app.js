// -------------------------------
// Función para mostrar datos en la página
// -------------------------------
function mostrarDatos(datos) {
  const contenedor = document.getElementById("tabla");
  contenedor.innerHTML = ""; // limpiar antes de volver a cargar

  datos.forEach(item => {
    contenedor.innerHTML += `
      <div class="item">
        <p><b>ID:</b> ${item.id}</p>
        <p><b>Título:</b> ${item.titulo}</p>
        <p><b>Autor:</b> ${item.autor}</p>
        <hr>
      </div>
    `;
  });
}

// -------------------------------
// Cargar datos desde JSON o LocalStorage
// -------------------------------
async function cargarDatos() {
  try {
    if (navigator.onLine) {
      // Si hay internet → traer datos del JSON
      const respuesta = await fetch("libros.json");
      const datos = await respuesta.json();

      // Mostrar en pantalla
      mostrarDatos(datos);

      // Guardar en localStorage
      localStorage.setItem("libros", JSON.stringify(datos));
    } else {
      // Si no hay internet → usar localStorage
      const guardados = JSON.parse(localStorage.getItem("libros"));
      if (guardados) {
        mostrarDatos(guardados);
      } else {
        document.getElementById("tabla").innerHTML = 
          "<p>No hay datos disponibles offline todavía.</p>";
      }
    }
  } catch (error) {
    console.error("Error cargando datos:", error);
  }
}

// -------------------------------
// Registrar Service Worker
// -------------------------------
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js")
    .then(() => console.log("✅ Service Worker registrado"))
    .catch(err => console.error("❌ Error registrando SW:", err));
}

// -------------------------------
// Ejecutar carga de datos al iniciar
// -------------------------------
window.addEventListener("DOMContentLoaded", cargarDatos);
