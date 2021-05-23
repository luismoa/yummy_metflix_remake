 const interval_wait_ajax_to_request=2000;

    function updateMovieList(updated_movies)
    {
      var items = [];
      for (var i in updated_movies) {
          var item = updated_movies[i];
          items.push('<li id="' + item.id + '">' + item.title + '</li>');
      }
      $('#ul_movie').html(items.join(''));
    }

    function updateMovieListCunter(updated_movies)
    {
      var movies = updated_movies.length
      $('#movie-counter-ajax').innerHTML =movies
    }

   $(document).ready(function(){
    setInterval(function(){
     $.ajax({
    url:"/movies/api/",
    type:"get",
    dataType:"json",
    success: function(response){
        updateMovieList(response);
        updateMovieListCunter(response);
        console.log(response);
    }
   });
    }, interval_wait_ajax_to_request);
});








