let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("mySlides");
    
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Скрываем все слайды
    }
    
    slideIndex++;
    
    if (slideIndex > slides.length) {
        slideIndex = 1; // Возвращаемся к первому слайду
    }
    
    slides[slideIndex - 1].style.display = "block"; // Показываем текущий слайд
    setTimeout(showSlides, 2000); // Меняем слайд каждые 5 секунд
}

document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector(".catalog-menu");
    const stopPoint = document.querySelector(".content"); // Блок "Каталог" или другой ограничитель

    const observer = new IntersectionObserver(
        ([entry]) => {
            if (entry.isIntersecting) {
                header.style.position = "absolute";
                header.style.top = stopPoint.offsetTop + "px";
            } else {
                header.style.position = "fixed";
                header.style.top = "0";
            }
        },
        { threshold: 0.1 }
    );

    observer.observe(stopPoint);
});

