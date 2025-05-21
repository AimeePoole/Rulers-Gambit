
fetch('http://127.0.0.1:8000/scenarioDetails')
  .then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    document.getElementById("getScenario").innerHTML = data.scenarioDescription;
    // this might work 
    //document.getElementById("getScenario").innerHTML = data.id, data.optionDescription, data.scenario_id;
  });


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