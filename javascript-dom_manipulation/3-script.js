const header = document.querySelector('#red_header');
header.addEventListener('click', function () {
  header.classList.toggle('red');
  header.classList.toggle('green');
});
