var spinner = document.querySelector("#news_paper");
document.querySelector("button").onclick = function() {
  spinner.style.animationName = "example";
  setTimeout(function() {
    spinner.style.animationName = "";
  }, 4000);
};