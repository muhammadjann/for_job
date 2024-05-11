function getNews() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log(this.responseText)
    }
  xhttp.open("GET", "http://127.0.0.1:8000/api/v1/news/");
  xhttp.send();
}