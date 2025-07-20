document.getElementById("shortenBtn").addEventListener("click", async () => {
      const url = document.getElementById("urlInput").value;
      const resultDiv = document.getElementById("result");

      if (!url) {
        resultDiv.textContent = "Por favor ingresá un enlace válido.";
        return;
      }

      try {
        const response = await fetch("http://localhost:5000/api/shorten", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ Url: url })
        });

        const data = await response.json();

        if (response.ok) {
          resultDiv.innerHTML = `Enlace acortado: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
        } else {
          resultDiv.textContent = `Error: ${data.message || "No se pudo acortar el enlace."}`;
        }
      } catch (error) {
        resultDiv.textContent = "Hubo un error de conexión con el servidor.";
      }
    });