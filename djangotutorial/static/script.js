// este código hace que el cursor personalizado siga al mouse de forma suave
const cursor = document.querySelector(".cursor-xray");

let mouseX = 0;
let mouseY = 0;
let cursorX = 0;
let cursorY = 0;

document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

function moverCursor() {
    cursorX += (mouseX - cursorX) * 0.12;
    cursorY += (mouseY - cursorY) * 0.12;

    cursor.style.left = cursorX + "px";
    cursor.style.top = cursorY + "px";

    requestAnimationFrame(moverCursor);
}

moverCursor();

// esta parte calcula cuánto bajé en la página y mueve la barra lateral
const progreso = document.querySelector(".progreso-scroll");

window.addEventListener("scroll", () => {
    const scrollActual = window.scrollY;
    const alturaTotal = document.documentElement.scrollHeight - window.innerHeight;
    const porcentaje = (scrollActual / alturaTotal) * 100;

    progreso.style.height = porcentaje + "%";
});


// esta parte hace que el personaje tenga un pequeño movimiento siguiendo al mouse
const personaje = document.querySelector(".personaje");

let personajeX = 0;
let personajeY = 0;
let objetivoX = 0;
let objetivoY = 0;

document.addEventListener("mousemove", (e) => {
    const centroX = window.innerWidth / 2;
    const centroY = window.innerHeight / 2;

    objetivoX = (e.clientX - centroX) / 25;
    objetivoY = (e.clientY - centroY) / 30;
});

function moverPersonaje() {
    personajeX += (objetivoX - personajeX) * 0.05;
    personajeY += (objetivoY - personajeY) * 0.05;

    personaje.style.transform = `translate(${personajeX}px, ${personajeY}px)`;

    requestAnimationFrame(moverPersonaje);
}

moverPersonaje();

// hace que algunos elementos aparezcan suavemente cuando entran en pantalla dando como un efecto de que desaparecen y aparecen
const elementos = document.querySelectorAll(
    ".section-header, .skill-card, .proyecto-card, .sobre-mi-texto"
);

const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
        if (entrada.isIntersecting) {
            entrada.target.classList.add("mostrar");
        }
    });
}, { threshold: 0.15 });

elementos.forEach((elemento) => {
    observador.observe(elemento);
});

const modoBtn = document.getElementById("modo-btn");

modoBtn.addEventListener("click", function () {

    document.body.classList.toggle("modo-oscuro");

    if (document.body.classList.contains("modo-oscuro")) {
        modoBtn.innerHTML = '<i class="bi bi-sun-fill"></i>';
    } else {
        modoBtn.innerHTML = '<i class="bi bi-moon-fill"></i>';
    }

});