document.addEventListener("DOMContentLoaded", function () {
    const noticias = document.querySelectorAll(".noticia");
    const navegacion = document.querySelector(".navegacion");
    const botonAnterior = document.getElementById("anterior");
    const botonSiguiente = document.getElementById("siguiente");
    let indiceNoticiaActual = 0;

    function mostrarNoticia(indice) {
        noticias.forEach((noticia, i) => {
            if (i === indice) {
                noticia.style.display = "block";
            } else {
                noticia.style.display = "none";
            }
        });
    }

    function avanzarNoticia() {
        indiceNoticiaActual = (indiceNoticiaActual + 1) % noticias.length;
        mostrarNoticia(indiceNoticiaActual);
    }

    function retrocederNoticia() {
        indiceNoticiaActual = (indiceNoticiaActual - 1 + noticias.length) % noticias.length;
        mostrarNoticia(indiceNoticiaActual);
    }

    mostrarNoticia(indiceNoticiaActual);

    botonSiguiente.addEventListener("click", avanzarNoticia);
    botonAnterior.addEventListener("click", retrocederNoticia);
});
