document.addEventListener('DOMContentLoaded', () => {
  const hello = document.querySelector('#hello');
  const languageCode = document.querySelector('#language_code');
  const btnTranslate = document.querySelector('#btn_translate');
  btnTranslate.addEventListener('click', ()=>{})
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello;
    });
});
