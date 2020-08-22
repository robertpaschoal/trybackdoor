const $slider = document.querySelector('.slider');
const $body = document.querySelector('body');
let state = false;

$slider.addEventListener('click', () => {
    if (state) {
        $body.style.backgroundColor = '#f0f3bd';
        $slider.value = '0';
        state = false;

    } else {
        $body.style.backgroundColor = '#028090';
        $slider.value = '1';
        state = true;
    }
})