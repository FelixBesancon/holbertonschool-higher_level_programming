const listMovies = document.querySelector('ul#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      listMovies.appendChild(li);
    });
  });
