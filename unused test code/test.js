

fetch('http://127.0.0.1:8000/scenario')
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('GET response text:');
        console.log(text);
    });


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


