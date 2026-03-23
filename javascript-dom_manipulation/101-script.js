document.addEventListener('DOMContentLoaded', () => {
  const hello = document.querySelector('#hello');
  const languageCode = document.querySelector('#language_code');
  const btnTranslate = document.querySelector('#btn_translate');
  btnTranslate.addEventListener('click', ()=>{
    const language = languageCode.value;
    fetch('https://hellosalut.stefanbohacek.com/?lang=' + language)
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello;
    });
  })
});
