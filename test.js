
/*
fetch('http://127.0.0.1:8000/scenario')
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('GET response text:');
        console.log(text);
    });
*/



fetch('http://127.0.0.1:8000/scenarioDetails')
  .then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    document.getElementById("getScenario").innerHTML = data.scenarioDescription;
    // this might work 
    //document.getElementById("getScenario").innerHTML = data.id, data.optionDescription, data.scenario_id;
  });


//https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
//this is an example of a post request that gets a username entered by the user
function sendInput() {
    //this gets the entered user name and posts it to the python terminal
    const usernameInput = document.getElementById('username').value;
    fetch("http://127.0.0.1:8000/post", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: usernameInput }),
    });
}





fetch('http://127.0.0.1:8000/playerStats')
  .then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    let html = "";
    data.forEach(item => {
      html += item.statName + ": " + item.statsValue + "<br>";
    });

    document.getElementById("getStats").innerHTML = html;
  });