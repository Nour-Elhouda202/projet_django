

document.addEventListener('DOMContentLoaded', () => {
    const seeMoreBtn = document.getElementById('see-more-btn');
    const moreContent = document.getElementById('more-content');

    if (seeMoreBtn && moreContent) {
        seeMoreBtn.addEventListener('click', () => {
            if (moreContent.classList.contains('collapsed')) {
                // Afficher le contenu supplémentaire
                moreContent.classList.remove('collapsed');
                moreContent.classList.add('expanded');
                seeMoreBtn.innerHTML = "رؤية أقل<span class='arrow-up'>▲</span>";
            } else {
                // Masquer le contenu supplémentaire
                moreContent.classList.remove('expanded');
                moreContent.classList.add('collapsed');
                seeMoreBtn.innerHTML = "  رؤية المزيد<span class='arrow-down'>▼</span>";
            }
        });
    } else {
        console.error("Bouton ou contenu supplémentaire non trouvé.");
    }
});

let slideIndex = 1;
showSlides(slideIndex);

// Fonction pour passer à la diapositive suivante ou précédente
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Fonction pour afficher une diapositive spécifique
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Fonction principale pour gérer l'affichage des diapositives
function showSlides(n) {
    let i;
    const slides = document.getElementsByClassName("mySlides");
    const dots = document.getElementsByClassName("dot");

    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    // Masquer toutes les diapositives
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    // Désactiver tous les points
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    // Afficher la diapositive actuelle et activer le point correspondant
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

