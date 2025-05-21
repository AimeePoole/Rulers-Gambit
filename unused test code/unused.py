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
    db = sqlite3.connect('database.db')
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
def scenario_Post():
    db = sqlite3.connect('database.db' , timeout=30)
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
    db = sqlite3.connect('database.db' , timeout=30)
    cursor = db.cursor()

 
    cursor.execute('INSERT OR IGNORE INTO scenario\
    (id, scenarioDescription, catagory_id, phase_id) ' \
    'VALUES ("s3", "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?", "c1","p1")')


    db.commit()
    data = with_labels(cursor.fetchall(), ("id", "scenarioDescription","catagoryName","phaseName"))    
    return jsonify(data)
