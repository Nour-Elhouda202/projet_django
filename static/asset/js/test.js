


const images = [
    'url("../image/331351-alexfas01.jpg")',
    'url("../image/8b6463f019bd3688b76d7dcc537001f0.jpg")',
];

let currentIndex = 0;

function changeBackground() {
    const div = document.getElementById('hero');
    div.style.opacity = 0;
    setTimeout(() => {
        div.style.backgroundImage = images[currentIndex];
        div.style.opacity = 1;
        currentIndex = (currentIndex + 1) % images.length;
    }, 1000); // Délai de 1 seconde pour l'effet de fondu
}

setInterval(changeBackground, 6000);

changeBackground();