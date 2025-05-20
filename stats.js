function checkSum() {
    const Economy = parseInt(document.getElementById('economy').value);
    const Military = parseInt(document.getElementById('military').value);
    const Security = parseInt(document.getElementById('security').value);
    const Welfare = parseInt(document.getElementById('welfare').value);
    const Education = parseInt(document.getElementById('education').value);
    const Agriculture = parseInt(document.getElementById('agriculture').value)
    
      const sum = Economy + Military + Security + Welfare + Education + Agriculture;
      const resultElement = document.getElementById('result');

      if (sum === 20) {
        alert("Success! The sum is exactly 20.");
        window.location.href = "senario_page.html";
      } else {
        alert("The sum is wrong. Try again!");
        resultElement.textContent = `The sum is ${sum}. Try again!`;
        resultElement.style.color = '#FF3333';
      }
      
}

function sendInputs() {
    //this gets the entered user name and posts it to the python terminal
    const Economy = document.getElementById('economy').value;
    const Military = document.getElementById('military').value;
    const Security = document.getElementById('security').value;
    const Welfare = document.getElementById('welfare').value;
    const Education = document.getElementById('education').value;
    const Agriculture = document.getElementById('agriculture').value;
 
    
    fetch("http://127.0.0.1:8000/stats", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({ economy : Economy , 
        military : Military ,
        security : Security ,
        welfare : Welfare ,
        education : Education ,
        agriculture : Agriculture
    }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response:", data);
        // You can update the UI or perform other actions with the received data here
    })
    
}
