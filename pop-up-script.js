const openPopup = document.getElementById('openPopupButton');
const closePopup = document.getElementById('closePopupButton');
const popup = document.getElementById('popup');

openPopup.addEventListener('click', () => {
    popup.style.display = 'flex';
});

closePopup.addEventListener('click', () => {
    popup.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === popup) {
        popup.style.display = 'none';
    }
});