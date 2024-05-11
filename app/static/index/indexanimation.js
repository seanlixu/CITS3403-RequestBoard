const f1 = document.getElementById('f1');
const f2 = document.getElementById('f2');
const f3 = document.getElementById('f3');
const f4 = document.getElementById('f4');
const f5 = document.getElementById('f5');
const f6 = document.getElementById('f6');
const f7 = document.getElementById('f7');
const f8 = document.getElementById('f8');

const button = document.getElementById('getstartedbutton');

document.addEventListener('mousemove', function(event){
    mousex = event.clientX;
    mousey = event.clientY;
    const buttonPos = button.getBoundingClientRect();
    const buttonCenterX = buttonPos.left + buttonPos.width / 2;
    const buttonCenterY = buttonPos.top + buttonPos.height / 2;

    const distX = Math.abs(mousex - buttonCenterX);
    
    const distY = Math.abs(mousey - buttonCenterY);
    console.log(distX);
    console.log(distY);
    // Use the distance to set the translateX value

    const translateY = 2*(distY / 10);



    // Apply the translation to the f1 element
    f1.style.transform = 'translateX(' + translateY + 'px)';
    f2.style.transform = 'translateX(' + (translateY*2.7) + 'px)';
    f3.style.transform = 'translateX(' + translateY + 'px)';
    f4.style.transform = 'translateX(' + (translateY*2.7) + 'px)';
    f5.style.transform = 'translateX(' + (-translateY) + 'px)';
    f6.style.transform = 'translateX(' + (-translateY*2.7) + 'px)';
    f7.style.transform = 'translateX(' + (-translateY) + 'px)';
    f8.style.transform = 'translateX(' + (-translateY*2.7) + 'px)';
})



const pfp1 = document.getElementById('pfp1');
const pfp2 = document.getElementById('pfp2');
const pfp3 = document.getElementById('pfp3');
const pfp4 = document.getElementById('pfp4');
const pfp5 = document.getElementById('pfp5');
const pfp6 = document.getElementById('pfp6');
const pfp7 = document.getElementById('pfp7');
const pfp8 = document.getElementById('pfp8');

const job1 = document.getElementById('job1');
const job2 = document.getElementById('job2');
const job3 = document.getElementById('job3');
const job4 = document.getElementById('job4');

document.addEventListener('scroll', function() {
        let value= window.scrollY;
        console.log(value);
        pfp1.style.transform = 'translateX(' + (value * 1) + 'px)';
        pfp3.style.transform = 'translateX(' + (value * 0.2) + 'px)';
        pfp5.style.transform = 'translateX(' + (value * 0.1) + 'px)';
        pfp6.style.transform = 'translateX(' + (value * 0.8) + 'px)';

        pfp2.style.transform = 'translateX(' + (value * -0.8) + 'px)';
        pfp4.style.transform = 'translateX(' + (value * -1.4) + 'px)';
        pfp7.style.transform = 'translateX(' + (value * -0.7) + 'px)';
        pfp8.style.transform = 'translateX(' + (value * -0.2) + 'px)';

        job1.style.transform = 'translateX(' + (value*-0.4) + 'px)';
        job2.style.transform = 'translateX(' + (value*0.9) + 'px)';
        job3.style.transform = 'translateX(' + (value*-1) + 'px)';
        job4.style.transform = 'translateX(' + (value*0.3) + 'px)';
    }
);

function calculateMax(value){
    if (value*1.1 >=560){
        return 560;
    }
    return value*1.1;
}
