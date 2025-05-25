//inactive
//this is to count how many thimes the submit button has been pressed and cap it at a sertain amount
// this code can/could be added to another js file is convinient/better

//https://www.tutorialspoint.com/how-to-count-the-number-of-times-a-button-is-clicked-using-javascript#:~:text=Tracking%20button%20clicks%20is%20a,keep%20track%20of%20button%20clicks.


      var count = 0;
      var button = document.getElementById("myButton");
      var result = document.getElementById("result");
      button.onclick = function() {
         count++;
         result.innerHTML = count;
      }
