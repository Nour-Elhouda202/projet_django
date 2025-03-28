    // Toggle Side Overlay des types de livres
    document.getElementById('toggleBookTypesButton').addEventListener('click', function() {
        document.getElementById('bookTypesOverlay').classList.toggle('active');
    });









  
const images = [
    "url('../image/8b6463f019bd3688b76d7dcc537001f0.jpg')",
    "url('../image/alger.jpg')",
    "url('../image/photo_2025-03-02_17-07-52.jpg')"
];

let currentIndex = 0;

function changeBackground() {
    const hero = document.getElementById('hero');
    if (hero) {
        
        hero.style.backgroundImage = `linear-gradient(to right, rgba(0, 0, 0, 0) 20%, rgba(0, 0, 0, 1) 100%), ${images[currentIndex]}`;
        
      
        currentIndex = (currentIndex + 1) % images.length;
    }
}


setInterval(changeBackground, 3000);
changeBackground();