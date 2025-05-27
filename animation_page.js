//active
function animation_buttonid() {
  var spinner = document.getElementById('news_paper')
  //animation_page.html("#news_paper");
  //animation_page.html("#spin_button").
  document.getElementById('spin_button').onclick = function () {
    spinner.style.animationName = "example";
    setTimeout(function () {
      spinner.style.animationName = "";
    }, 4000);
  };
}

