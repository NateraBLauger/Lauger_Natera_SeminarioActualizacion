const API_URL = "https://tp-final-pinguinos-api.onrender.com";

const formulario = document.getElementById("formulario");
const resultado = document.getElementById("resultado");

function mostrar(texto, tipo) {
  resultado.className = tipo;
  resultado.textContent = texto;
}

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const datos = {
    bill_length_mm: parseFloat(formulario.bill_length_mm.value),
    bill_depth_mm: parseFloat(formulario.bill_depth_mm.value),
    flipper_length_mm: parseFloat(formulario.flipper_length_mm.value),
    body_mass_g: parseFloat(formulario.body_mass_g.value),
  };

  mostrar("Consultando al modelo...", "info");

  try {
    const respuesta = await fetch(`${API_URL}/predecir`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });

    if (respuesta.status === 422) {
      mostrar("Datos inválidos: completá todos los campos con números mayores que 0.", "error");
      return;
    }
    if (!respuesta.ok) {
      mostrar(`Error del servidor (código ${respuesta.status}).`, "error");
      return;
    }

    const data = await respuesta.json();
    const lineas = Object.entries(data.probabilidades)
      .map(([clase, p]) => `${clase}: ${(p * 100).toFixed(1)}%`);
    mostrar(`Especie predicha: ${data.especie}\n${lineas.join("\n")}`, "ok");
  } catch (error) {
    mostrar("No se pudo conectar con la API. ¿Está encendida?", "error");
  }
});