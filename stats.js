

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
