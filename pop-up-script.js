//inactive
//get elements by id once and save them as consts
const openPopup = document.getElementById('openPopupButton');
const closePopup = document.getElementById('closePopupButton');
const popup = document.getElementById('popup');

//opens popup when button is clicked
openPopup.addEventListener('click', () => {
    popup.style.display = 'flex';
});

//closes popup when button is clicked
closePopup.addEventListener('click', () => {
    popup.style.display = 'none';
});

//closes popup when outside the window is clicked
window.addEventListener('click', (event) => {
    if (event.target === popup) {
        popup.style.display = 'none';
    }
});

