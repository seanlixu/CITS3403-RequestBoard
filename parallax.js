const wave1 = document.querySelector('.wave1');
const wave2 = document.querySelector('.wave2');
const wave3 = document.querySelector('.wave3');
const wave4 = document.querySelector('.wave4');
const wave5 = document.querySelector('.wave5');
const wave6 = document.querySelector('.wave6');

document.addEventListener('scroll', function() {
        let value= window.scrollY;
        console.log(value);
        wave1.style.transform = 'translateX(' + (value * -0.5) + 'px)';
        wave2.style.transform = 'translateX(' + (value * -1) + 'px)';
        wave3.style.transform = 'translateX(' + (value * -1.5) + 'px)';
        wave4.style.transform = 'translateX(' + (value * -2) + 'px)';
        wave5.style.transform = 'translateX(' + (value * -2.5) + 'px)';
        wave6.style.transform = 'translateX(' + (value * -3) + 'px)';
    }

);
