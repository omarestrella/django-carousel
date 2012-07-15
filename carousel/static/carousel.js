function enableIndicators(swipeCarousel) {
    var carousel = swipeCarousel.element,
        indicators = document.getElementById('indicators');

    var slides = carousel.getElementsByTagName('li');

    for(var i = 0; i < slides.length; i++) {
        var li = document.createElement('li');
        li.innerHTML = '&bull;';
        indicators.appendChild(li);
    }
}
