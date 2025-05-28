//fetches the python get method returning a json file with the players stats 
//this gets the final score through adding all the stats together
fetch('http://127.0.0.1:8000/playerStats')
  .then(function (response) {
    return response.json();
  })
  //this gets the data
  .then(function (data) {
    console.log(data);

    let total = 0;

    // let each stat be output like "Economy: 3"
    data.forEach(item => {
      total += parseInt(item.statsValue)
    });

    // gets the correct html element
    document.getElementById("endScore").innerHTML = total;
  });

//reset scenario counter so game can be replayed
localStorage.setItem('result', 0);