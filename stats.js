function checkSum() {
  //this gets all the stat values entered as consts 
  const Economy = parseInt(document.getElementById('economy').value);
  const Military = parseInt(document.getElementById('military').value);
  const Security = parseInt(document.getElementById('security').value);
  const Welfare = parseInt(document.getElementById('welfare').value);
  const Education = parseInt(document.getElementById('education').value);
  const Agriculture = parseInt(document.getElementById('agriculture').value)

  //this adds all the stats
  const total = Economy + Military + Security + Welfare + Education + Agriculture;
  const result = document.getElementById('result');

  //checks the stats are equal to 20
  if (total === 20) {
    alert("Success! The total is exactly 20.");

    //fetches the python post method returning the new stats in a json file
    fetch("http://127.0.0.1:8000/stats", {
      method: "POST",
      //using json
      headers: {
        "Content-Type": "application/json",
      },
      //this insertes the stats
      body: JSON.stringify({
        economy: Economy,
        military: Military,
        security: Security,
        welfare: Welfare,
        education: Education,
        agriculture: Agriculture
      }),
    })
      .then(response => response.json())
      .then(data => {
        console.log("Server response:", data);
        // You can update the UI or perform other actions with the received data here
      })
    //opens the scenarion page is the stats equal 20
    window.location.href = "senario_page.html";

  }
  //error message for if the su doesnt equal 20
  else {
    result.textContent = `The sum is ${total}. Try again!`;
    result.style.color = '#FF3333';
  }

}
