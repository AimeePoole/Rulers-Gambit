from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3
import random

app = Flask(__name__)

CORS(app)


# given an array of rows, each of which is an array, add the given labels to each row
def with_labels(rows, labels):
    return [dict((labels[i], value) for i, value in enumerate(row)) for row in rows]



@app.route("/hello")
def scenario():
    return jsonify({"message": "Hello from Flask!"})


@app.route('/scenario', methods=['GET'])
def find_all():
    db = sqlite3.connect('databaseTest.db')
    #a cursor lets you Send SQL queries to the database (e.g., SELECT, INSERT, UPDATE, DELETE) and fetch results from those queries
    cursor = db.cursor()

    # get all scenario
    cursor.execute('SELECT scenario.id AS scenario_id,' \
    'scenario.scenarioDescription,' \
    'catagory.catagoryName,' \
    'phase.phaseName,' \
    'options.id AS option_id,' \
    'options.optionDescription FROM scenario ' \
    'LEFT JOIN catagory ON scenario.catagory_id = catagory.id ' \
    'LEFT JOIN phase ON scenario.phase_id = phase.id ' \
    'LEFT JOIN options ON options.scenario_id = scenario.id;')
    data = with_labels(cursor.fetchall(), ("id", "scenarioDescription","catagoryName","phaseName","option_id","optionDescription"))    
    return jsonify(data)




#this groups the options and scenarios and just shows that
@app.route('/scenarioDetails', methods=['GET'])
def find():
    db = sqlite3.connect('databaseTest.db')
    cursor = db.cursor()

    cursor.execute('''
        SELECT 
            scenario.id AS scenario_id,
            scenario.scenarioDescription,
            options.id,
            options.optionDescription,
            affects.optionMechanic,
            affects.stat_id
            FROM scenario
            LEFT JOIN options ON options.scenario_id = scenario.id
            LEFT JOIN affects ON affects.option_id = options.id

    ''')

    rows = cursor.fetchall()

    # Group the options by scenario so the scenario isnt printed every time
    scenarios = {}
    for scenario_id, scenario_desc, option_id, option_desc, optionMechanic, stat_id in rows:
        if scenario_id not in scenarios:
            #https://pythonguides.com/dictionaries/
            #https://docs.python.org/3/tutorial/datastructures.html#dictionaries
            #https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/  - Using square brackets []
            #https://jsonapi.org/format/#document-resource-objects
            scenarios[scenario_id] = {
                "id": scenario_id,
                "scenarioDescription": scenario_desc,
                "options": []
            }
        
        if option_desc:
            # Check if the option already exists
            #Retrieves the next item generator = (expression for item in iterable if condition) 
            #https://www.pythonmorsels.com/next
            generator = next((option for option in scenarios[scenario_id]["options"] if option["option_id"] == option_id), None)
            if not generator:
                # Add new option if it doesn't exist
                scenarios[scenario_id]["options"].append({
                    "option_id": option_id,
                    "optionDescription": option_desc,
                    "optionMechanic": []
                })
        #Checks whether for an optionMechanic
        if optionMechanic:
            # Find the specific option that the current mechanic affects by finding the one with the same option id
            for option in scenarios[scenario_id]["options"]:
                #chooses the correct id to add the mechanic to
                if option["option_id"] == option_id:
                    #appends the dictionary to have the mechanic
                    option["optionMechanic"].append({
                        "stat_id": stat_id,
                        "optionDescription": optionMechanic
                    })
                    break

        
    #https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
    #https://bobbyhadz.com/blog/python-get-random-key-value-from-dictionary
    random_scenario = random.choice(list(scenarios.values()))
    return jsonify(random_scenario)

# Access a value
#print(scenarios['scenario_id'])






#post test
@app.route('/scenarioPost', methods=['POST'])
def scenario_Post():
    db = sqlite3.connect('databaseTest.db' , timeout=30)
    cursor = db.cursor()

 
    cursor.execute('INSERT OR IGNORE INTO scenario\
    (id, scenarioDescription, catagory_id, phase_id) ' \
    'VALUES ("s3", "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?", "c1","p1")')


    db.commit()
    data = with_labels(cursor.fetchall(), ("id", "scenarioDescription","catagoryName","phaseName"))    
    return jsonify(data)






#post test
#What i need to do for this test is get the option-id and use that to find the option mechanics but they havent been created yet
@app.route('/optionPost', methods=['POST'])
def option_Post():
    db = sqlite3.connect('databaseTest.db' , timeout=30)
    cursor = db.cursor()

 
    cursor.execute('INSERT OR IGNORE INTO scenario\
    (id, scenarioDescription, catagory_id, phase_id) ' \
    'VALUES ("s3", "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?", "c1","p1")')


    db.commit()
    data = with_labels(cursor.fetchall(), ("id", "scenarioDescription","catagoryName","phaseName"))    
    return jsonify(data)






@app.route('/post', methods=['POST'])
def receive_input():
    data = request.get_json()
    username = data.get('username')
    
    # Example: Save to database or do something with it
    print("Received from user:", username)

    return jsonify({"message": "Received", "input": username})








if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
