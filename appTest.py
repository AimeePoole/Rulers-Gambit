from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3

appTest = Flask(__name__)
CORS(appTest)
jsOrigin = "http://127.0.0.1:5501"



# given an array of rows, each of which is an array, add the given labels to each row
def with_labels(rows, labels):
    return [dict((labels[i], value) for i, value in enumerate(row)) for row in rows]


app = Flask(__name__)

@app.route("/hello")
@cross_origin(origins = jsOrigin)
def scenario():
    return jsonify({"message": "Hello from Flask!"})


@app.route('/scenario', methods=['GET'])
@cross_origin(origins = jsOrigin)
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














#post test
@app.route('/scenarioPost', methods=['POST'])
@cross_origin(origins = jsOrigin)
def rate():
    db = sqlite3.connect('databaseTest.db' , timeout=30)
    cursor = db.cursor()

 
    cursor.execute('INSERT OR IGNORE INTO scenario\
    (id, scenarioDescription, catagory_id, phase_id) ' \
    'VALUES ("s3", "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?", "c1","p1")')


    db.commit()
    data = with_labels(cursor.fetchall(), ("id", "scenarioDescription","catagoryName","phaseName"))    
    return jsonify(data)






if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
