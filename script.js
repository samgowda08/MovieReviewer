let api = 'https://www.omdbapi.com/?apikey=58d4f683&t=';

fetch(api).then((response)=>{
    return response.json()
}).then((movieData)=>{
    console.log(movieData)
})




let title = document.getElementById('title');
let date = document.getElementById('date');
let actors = document.getElementById('actors');
let director = document.getElementById('director');
let poster = document.getElementById('poster');
let desc = document.getElementById('desc');
let collection = document.getElementById('collection');
let ratings = document.getElementById('ratings');
let genre = document.getElementById('genre');
let awards = document.getElementById('awards');
let country = document.getElementById('country');
let runtime = document.getElementById('runtime');
let writer = document.getElementById('writer');
let imdbVotes = document.getElementById('imdbVotes');

function searchMovie(){
    let movieName = document.getElementById('movieName');
    let query = api + movieName.value;
    fetch(query).then((response)=>{
        return response.json()
    }).then((movieData)=>{
        console.log(movieData)
        title.innerText = movieData.Title;
        genre.innerText = movieData.Genre;
        date.innerText = movieData.Released;
        collection.innerText = movieData.BoxOffice;
        director.innerText = movieData.Director;
        ratings.innerText = movieData.imdbRating;
        actors.innerText = movieData.Actors;
        desc.innerText = movieData.Plot;
        awards.innerText = movieData.Awards;
        country.innerText = movieData.Country;
        runtime.innerText = movieData.Runtime;
        writer.innerText = movieData.Writer;
        imdbVotes.innerText = movieData.imdbVotes;
        poster.src = movieData.Poster;

    })
}
