//inactive
//fetches the python get method getting a json file with the scenario description option decription and option mechanics

fetch('http://127.0.0.1:8000/scenarioDetails')
  .then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    //gets the correct html element
    document.getElementById("getScenario").innerHTML = data.scenarioDescription;

    document.getElementById("getOption1").innerHTML = data.options[0].optionDescription;
    document.getElementById("getOption2").innerHTML = data.options[1].optionDescription;
    document.getElementById("getOption3").innerHTML = data.options[2].optionDescription;
    document.getElementById("getOption4").innerHTML = data.options[3].optionDescription;


    // this might work 
    //document.getElementById("getScenario").innerHTML = data.id, data.optionDescription, data.scenario_id;
  });


//fetches the python get method returning a json filw with the players stats 
//put in a function so this can be refreshed every time a scenario is answered
fetch('http://127.0.0.1:8000/playerStats')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    console.log(data);
    let statsStyled = "";

    // let each stat be output like "Economy: 3"
    data.forEach(item => {
      statsStyled += item.statName + ": " + item.statsValue + "<br>";
    });

    // gets the correct html element
    document.getElementById("getStats").innerHTML = statsStyled;
  });



function displayRadioValue() {
  const selected = document.querySelector('input[name="Options"]:checked').value;
  document.getElementById("result").innerHTML = selected;
}
