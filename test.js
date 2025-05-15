fetch('http://127.0.0.1:8000/scenario')
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('GET response text:');
        console.log(text);
    });


fetch('http://127.0.0.1:8000/scenarioDetails')
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('GET response text:');
        console.log(text); 
    });

