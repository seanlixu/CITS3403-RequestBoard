const $f1 = $('#f1');
const $f2 = $('#f2');
const $f3 = $('#f3');
const $f4 = $('#f4');
const $f5 = $('#f5');
const $f6 = $('#f6');
const $f7 = $('#f7');
const $f8 = $('#f8');

const $button = $('#getstartedbutton');

$(document).mousemove(function(event){
    const mousey = event.clientY;
    const buttonPos = $button.offset();
    const buttonCenterY = buttonPos.top + $button.height() / 2;

    const distY = Math.abs(mousey - buttonCenterY);

    const translateY = 2*(distY / 10);

    $f1.css('transform', 'translateX(' + translateY + 'px)');
    $f2.css('transform', 'translateX(' + (translateY * 2.7) + 'px)');
    $f3.css('transform', 'translateX(' + translateY + 'px)');
    $f4.css('transform', 'translateX(' + (translateY * 2.7) + 'px)');
    $f5.css('transform', 'translateX(' + (-translateY) + 'px)');
    $f6.css('transform', 'translateX(' + (-translateY * 2.7) + 'px)');
    $f7.css('transform', 'translateX(' + (-translateY) + 'px)');
    $f8.css('transform', 'translateX(' + (-translateY * 2.7) + 'px)');
});

const $pfp1 = $('#pfp1');
const $pfp2 = $('#pfp2');
const $pfp3 = $('#pfp3');
const $pfp4 = $('#pfp4');
const $pfp5 = $('#pfp5');
const $pfp6 = $('#pfp6');
const $pfp7 = $('#pfp7');
const $pfp8 = $('#pfp8');

const $job1 = $('#job1');
const $job2 = $('#job2');
const $job3 = $('#job3');
const $job4 = $('#job4');

$(document).scroll(function() {
    let value= $(this).scrollTop();
    $pfp1.css('transform', 'translateX(' + (value * -0.5) + 'px) rotate(' + (value * -0.1) + 'deg)');
    $pfp2.css('transform', 'translateX(' + (value * 0.5) + 'px) rotate(' + (value * 0.1) + 'deg)');
    $pfp3.css('transform', 'translateX(' + (value * -0.5) + 'px) rotate(' + (value * 0.1) + 'deg)');
    $pfp4.css('transform', 'translateX(' + (value * 0.5) + 'px) rotate(' + (value * -0.1) + 'deg)');

    $job1.css('transform', 'translateX(' + (value * -0.5) + 'px) rotate(' + (value * -0.1) + 'deg)');
    $job2.css('transform', 'translateX(' + (value * -0.5) + 'px) rotate(' + (value * 0.1) + 'deg)');
    $job3.css('transform', 'translateX(' + (value * 0.5) + 'px) rotate(' + (value * 0.1) + 'deg)');
    $job4.css('transform', 'translateX(' + (value * 0.5) + 'px) rotate(' + (value * -0.1) + 'deg)');
});
