//inactive
//fetches the python get method getting a json file with the scenario description option decription and option mechanics
let scenarioData = null;

fetch('http://127.0.0.1:8000/scenarioDetails')
  .then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    scenarioData = data;
    //gets the correct html element
    document.getElementById("getScenario").innerHTML = data.scenarioDescription;

    document.getElementById("getOption1").innerHTML = data.options[0].optionDescription;
    document.getElementById("getOption2").innerHTML = data.options[1].optionDescription;
    document.getElementById("getOption3").innerHTML = data.options[2].optionDescription;
    document.getElementById("getOption4").innerHTML = data.options[3].optionDescription;
  });



  function getOptionPickedId(data)
  {
    if (!scenarioData) {
      document.getElementById("result").innerHTML = "Scenario data not loaded yet.";
      return;
    }

    const selected = parseInt(document.querySelector('input[name="Options"]:checked').value);
    document.getElementById("result").innerHTML = scenarioData.options[selected].option_id
;
  }
  

  

  
  
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




