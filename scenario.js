//inactive
//fetches the python get method getting a json file with the scenario description option decription and option mechanics
let scenarioData = null;

fetch('http://127.0.0.1:8000/scenarioDetails')
  .then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    scenarioData = data;
    //gets the correct html elements and give them the correct text
    document.getElementById("getScenario").innerHTML = data.scenarioDescription;
    document.getElementById("getOption1").innerHTML = data.options[0].optionDescription;
    document.getElementById("getOption2").innerHTML = data.options[1].optionDescription;
    document.getElementById("getOption3").innerHTML = data.options[2].optionDescription;
    document.getElementById("getOption4").innerHTML = data.options[3].optionDescription;
      

    

});




//this uses the option picked to change the stats based on the affects 
function getOptionPickedId() {

  //note this could get the stat names through the json file but i refuse to fix that right now 
  const statNames = {
    "1": "Economy",
    "2": "Military",
    "3": "Security",
    "4": "Welfare",
    "5": "Education",
    "6": "Agriculture"
  }


  //this create the alert that will tell the use what the results would have been for all the options
  //this would be better a a pop up 
  let text = "These are the result of the options: \n\n";
          scenarioData.options.forEach(option => {
            text += `Option: ${option.optionDescription}\n`;
            option.optionMechanic.forEach(mechanic => { 
            const statName = statNames[mechanic.stat_id] || `Stat ID: ${mechanic.stat_id}`;
            text += `${statName} : ${mechanic.option_Mechanic}\n`;
            });
            text += '\n';
          });
  alert(text)


  //if there is no data error message
  if (!scenarioData) {
    document.getElementById("result").innerHTML = "Error: data not found";
    return;
  }

  //if no radio utton checked error message
  const checkSelected = document.querySelector('input[name="Options"]:checked');
  if (!checkSelected) {
    alert("Please select an option first.");
    return;
  }

  //get the option checked  index number (0,1,2,3) as i made that the name
  const selected = parseInt(document.querySelector('input[name="Options"]:checked').value)
  //gets all the mechanics per option
  const mechanics = scenarioData.options[selected].optionMechanic; 

  

  //if there is no mechanics stop (prevents crashing id databse isn't full)
  if (!mechanics || mechanics.length === 0) {
    console.error("No mechanics found for selected option.");
    return;
  }


//for each mechanic get its value and stat id
  for (let i = 0; i < mechanics.length; i++) {
    const mechanicValue = mechanics[i].option_Mechanic;
    const statId = mechanics[i].stat_id;

    //fetch the statsChange so tht this will effect the stats
    fetch("http://127.0.0.1:8000/statsChange", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      //add the values to a json file
      body: JSON.stringify({
        option_Mechanic: mechanicValue,
        stat_id: statId
      }),
    })
    //optput what hppend to the console to check it worked
    .then(response => response.json())
    .then(result => {
      console.log("Stat updated:", result);
      
    })
    .catch(error => {
      console.error("Error sending stat:", error);
    });
  }
  
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

  




