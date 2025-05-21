function checkSum() {
    const Economy = parseInt(document.getElementById('economy').value);
    const Military = parseInt(document.getElementById('military').value);
    const Security = parseInt(document.getElementById('security').value);
    const Welfare = parseInt(document.getElementById('welfare').value);
    const Education = parseInt(document.getElementById('education').value);
    const Agriculture = parseInt(document.getElementById('agriculture').value)
    
      const total = Economy + Military + Security + Welfare + Education + Agriculture;
      const result = document.getElementById('result');

      if (total === 20) {
        alert("Success! The total is exactly 20.");

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

        window.location.href = "senario_page.html";

      } else {
        result.textContent = `The sum is ${total}. Try again!`;
        result.style.color = '#FF3333';
      }
      
}
