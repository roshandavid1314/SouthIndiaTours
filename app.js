const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();

const photoDialog = document.querySelector('.photo-dialog');
if (photoDialog) {
  let opener;
  document.querySelectorAll('.photo-open').forEach(button => {
    button.addEventListener('click', () => {
      opener = button;
      const image = photoDialog.querySelector('img');
      image.src = button.dataset.photo;
      image.alt = button.dataset.caption;
      photoDialog.querySelector('p').textContent = button.dataset.caption;
      photoDialog.showModal();
    });
  });
  photoDialog.querySelector('.photo-close').addEventListener('click', () => photoDialog.close());
  photoDialog.addEventListener('click', event => {
    if (event.target !== photoDialog) return;
    const bounds = photoDialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) photoDialog.close();
  });
  photoDialog.addEventListener('close', () => {
    photoDialog.querySelector('img').removeAttribute('src');
    if (opener) opener.focus();
  });
}
