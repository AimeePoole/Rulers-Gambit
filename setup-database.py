import sqlite3

# create tables and insert some data. run it once to initialise the DB
# connect to the database
connect = sqlite3.connect('databaseTest.db')

# authors table
connect.execute(
    'CREATE TABLE IF NOT EXISTS scenario (\
        id integer PRIMARY KEY,\
        scenarioDescription text NOT NULL\
    )'
)



# genres table
connect.execute(
    'CREATE TABLE IF NOT EXISTS options (\
       id integer PRIMARY KEY,\
        optionDescription text NOT NULL, \
        scenario_id INTEGER, \
       FOREIGN KEY (scenario_id) REFERENCES scenario(id)\
    )'
)

cursor = connect.cursor()
cursor.execute('INSERT INTO scenario\
    (id, scenarioDescription) ' \
    'VALUES (1, "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?"), '
    '(2, "A storm has hit your southern frount, disrupting trade, uprooting citizens and damaging infulstructure. How will you respond?")')
connect.commit()

