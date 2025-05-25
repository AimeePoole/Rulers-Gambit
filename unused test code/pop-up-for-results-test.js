

  
  let text = "These are the result of the options: <br><br>";
  scenarioData.options.forEach(option => {
    text += `Option: ${option.optionDescription}<ul>`;
    option.optionMechanic.forEach(mechanic => {
      const statName = statNames[mechanic.stat_id] || `Stat ID: ${mechanic.stat_id}`;
      text += `<li>${statName} : ${mechanic.option_Mechanic}</li>`;
    });
    text += '</ul>';
  });
  document.getElementById("allMechanics").innerHTML = text;



  