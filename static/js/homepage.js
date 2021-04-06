function showPopularMovies(){
    var x = document.getElementById("popularMovies");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

// $(function() {
//     $("#searchMovie").autocomplete({
//         source : function(request, response) {
//             $.ajax({
//                 type: "POST",
//                 url : "http://127.0.0.1:5000/autosearch",
//                 dataType : "json",
//                 crossDomain: true,
//                 contentType: 'application/json; charset=utf-8',            
//                 cache: false,
//                 data : {
//                     searchMovie : request.search_query
//                 },
//                 success : function(data) {
//                     //alert(data);
//                     console.log(data);
//                     response(data);
//                 },
//                 error: function(jqXHR, textStatus, errorThrown) {
//                     console.log(textStatus + " " + errorThrown);
//                 }
//             });
//         },
//         minLength : 2
//     });
// });
