function getTweets() {
  console.log("Hii");
  return true;
}
function tweet(text) {
    let httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
      alert('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }
    //httpRequest.onreadystatechange = alertContents;
    httpRequest.open('GET', '/post_tweet/' + text);
    httpRequest.send();
}

document.addEventListener("DOMContentLoaded", function() {
    const tweetbtns = document.getElementsByClassName("tweetbtn");
    console.log(tweetbtns);

    for(let button of tweetbtns) {
      button.addEventListener("click", function(event) {
        console.log("button clicked");
        tweet(event.target.parentElement.getElementsByClassName("card-text")[0].innerText);
        //document.getElementById("demo").innerHTML = "Hello World";
    });
    }
});

