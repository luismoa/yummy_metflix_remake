const INTERVAL_AJAX_WAIT_TO_REQUEST = 2000;
var IS_CREATED_MOVIE_COUNTER = false;
function updateMovieList(updated_movies)
{
  var items = [];
  for (var i in updated_movies) {
      var item = updated_movies[i];
      items.push('<li id="movie_' + item.id + '">' + item.title + '</li>');
  }
  $('#ul_movie').html(items.join(''));
}

 function createMovieCounterElements()
{
    var spanMovieCounting = document.createElement("span");
    $('.total-movies-wrapper').text("Total movies:");
    spanMovieCounting.setAttribute("class","movie-counting");
    document.querySelector(".movie-data-ajax").appendChild(spanMovieCounting)
    IS_CREATED_MOVIE_COUNTER = true
}

function updateMovieListCounter(updated_movies)
{
  var movies = updated_movies.length;
  console.log(movies)
  if (!IS_CREATED_MOVIE_COUNTER){
    createMovieCounterElements()
   }
  $(".movie-data-ajax span.movie-counting").text(movies);
}

/*AJAX request for updating our movie list asynchronous */
$(document).ready(function(){
    setInterval(function(){
    $.ajax({
        url:"/movies/api/",
        type:"get",
        dataType:"json",
        success: function(response){
            updateMovieList(response);
            updateMovieListCounter(response);
        }
});
}, INTERVAL_AJAX_WAIT_TO_REQUEST);
});
