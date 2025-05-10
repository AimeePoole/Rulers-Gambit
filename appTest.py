from flask import Flask, jsonify, request
import sqlite3

# given an array of rows, each of which is an array, add the given labels to each row
def with_labels(rows, labels):
    return [dict((labels[i], value) for i, value in enumerate(row)) for row in rows]


app = Flask(__name__)

# lets you test the app is ronnung
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "Hello, world!", 200

# retrieve all books
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

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
