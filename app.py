#inactive

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3
import random

app = Flask(__name__)

CORS(app)


#adds the labels to each row
def with_labels(rows, labels):
    return [dict((labels[i], value) for i, value in enumerate(row)) for row in rows]





#this groups the scenarios, their options and their options mechanics.It uses a get method so the json can be fetched by the javascript
@app.route('/scenarioDetails', methods=['GET'])
def output_scenario_details():
    db = sqlite3.connect('database.db')
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
                        "option_Mechanic": optionMechanic
                    })
                    break

        
    #https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
    #https://bobbyhadz.com/blog/python-get-random-key-value-from-dictionary
    random_scenario = random.choice(list(scenarios.values()))
    return jsonify(random_scenario)



#this uses a post method to update the stats to what the user entered
@app.route('/stats', methods=['POST'])
def input_stats():
    data = request.get_json()
    print(data)
    db = sqlite3.connect('database.db' , timeout=30)
    cursor = db.cursor()
    
    player_id = "Pl1" 
    print(cursor.fetchall())

    stat_name_to_id = {
        'economy': 1,
        'military': 2,
        'security': 3,
        'welfare': 4,
        'education': 5,
        'agriculture': 6
    }



    for stat_name, stat_value in data.items():
        stats_id = stat_name_to_id[stat_name]
        cursor.execute(
            'UPDATE playerStats SET statsValue = ? WHERE player_id = ? AND stats_id = ?',
            (stat_value, player_id, stats_id)
    )


    db.commit()
    db.close()
    print(cursor.rowcount, "rows affected")
    return jsonify(data)




@app.route('/statsChange', methods=['POST'])
def input_statChange():
    
    data = request.get_json()
    print("Received data:", data)  # Debug print


    data = request.get_json()
    print(data)
    db = sqlite3.connect('database.db' , timeout=30)
    cursor = db.cursor()
    
    player_id = "Pl1" 
    print(cursor.fetchall())

    cursor.execute(
                '''
                UPDATE playerStats
                SET statsValue = statsValue + ?
                WHERE player_id = ? AND stats_id = ?
                ''',
                (data['option_Mechanic'], player_id, data['stat_id'])
    )


    db.commit()
    db.close()
    print(cursor.rowcount, "rows affected")
    return jsonify(data)





















#this groups the players stats and uses a get method so it can be fetched by the javascript
@app.route('/playerStats', methods=['GET'])
def output_player_stats():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute(
    'SELECT playerStats.statsValue, '
    'stats.statName '
    'FROM playerStats '
    'LEFT JOIN stats ON stats.id = playerStats.stats_id'
)
    data = with_labels(cursor.fetchall(), ("statsValue", "statName"))
    return jsonify(data)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)