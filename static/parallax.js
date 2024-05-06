// const wave1 = document.querySelector('.wave1');
const wave2 = document.querySelector('.wave2');
// const wave3 = document.querySelector('.wave3');
const wave4 = document.querySelector('.wave4');
// const wave5 = document.querySelector('.wave5');
const wave6 = document.querySelector('.wave6');
const card = document.querySelector('.card')    ;

const pfp1 = document.getElementById('pfp1');
const pfp2 = document.getElementById('pfp2');
const pfp3 = document.getElementById('pfp3');
const pfp4 = document.getElementById('pfp4');
const pfp5 = document.getElementById('pfp5');
const pfp6 = document.getElementById('pfp6');
const pfp7 = document.getElementById('pfp7');

const job1 = document.getElementById('job1');
const job2 = document.getElementById('job2');
const job3 = document.getElementById('job3');

document.addEventListener('scroll', function() {
        let value= window.scrollY;
        console.log(value);
        // wave1.style.transform = 'translateX(' + (value * -0.2) + 'px)';
        wave2.style.transform = 'translateX(' + (value * -0.5) + 'px)';
        // wave3.style.transform = 'translateX(' + (value * -1) + 'px)';
        wave4.style.transform = 'translateX(' + (value * -1) + 'px)';
        // wave5.style.transform = 'translateX(' + (value * -2) + 'px)';
        wave6.style.transform = 'translateX(' + (value * -1.5) + 'px)';

        pfp1.style.transform = 'translateX(' + (value * 0.6) + 'px)';
        pfp3.style.transform = 'translateX(' + (value * 1) + 'px)';
        pfp5.style.transform = 'translateX(' + (value * 1.4) + 'px)';
        pfp6.style.transform = 'translateX(' + (value * 0.5) + 'px)';

        pfp2.style.transform = 'translateX(' + (value * -1) + 'px)';
        pfp4.style.transform = 'translateX(' + (value * -1.4) + 'px)';
        pfp7.style.transform = 'translateX(' + (value * -0.7) + 'px)';

        job1.style.transform = 'translateX(' + (value*-0.4) + 'px)';
        job2.style.transform = 'translateX(' + (value*0.9) + 'px)';
        job3.style.transform = 'translateX(' + (value*-1) + 'px)';
    }
);

function calculateMax(value){
    if (value*1.1 >=560){
        return 560;
    }
    return value*1.1;
}

