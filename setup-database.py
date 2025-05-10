import sqlite3

# create tables and insert some data. run it once to initialise the DB
# connect to the database
connect = sqlite3.connect('databaseTest.db')

connect.execute(
    'CREATE TABLE IF NOT EXISTS catagory (\
        id text PRIMARY KEY,\
        catagoryName text NOT NULL\
    )'
)

connect.execute(
    'CREATE TABLE IF NOT EXISTS phase (\
        id text PRIMARY KEY,\
        phaseName text NOT NULL\
    )'
)

connect.execute(
    'CREATE TABLE IF NOT EXISTS scenario (\
        id text PRIMARY KEY,\
        scenarioDescription text NOT NULL,\
        catagory_id TEXT,\
        phase_id TEXT,\
        FOREIGN KEY (catagory_id) REFERENCES catagory(id),\
        FOREIGN KEY (phase_id) REFERENCES phase(id)\
    )'
)


connect.execute(
    'CREATE TABLE IF NOT EXISTS options (\
       id text PRIMARY KEY,\
        optionDescription text NOT NULL, \
        scenario_id INTEGER, \
       FOREIGN KEY (scenario_id) REFERENCES scenario(id)\
    )'
)


cursor = connect.cursor()
cursor.execute('INSERT INTO catagory\
    (id, catagoryName) ' \
    'VALUES ("c1", "Weather")')

cursor.execute('INSERT INTO phase\
    (id, phaseName) ' \
    'VALUES ("p1", "Phase 1")')

cursor.execute('INSERT INTO scenario\
    (id, scenarioDescription, catagory_id, phase_id) ' \
    'VALUES ("s1", "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?", "c1","p1")')

cursor.execute('INSERT INTO options\
    (id, optionDescription, scenario_id) ' \
    'VALUES ("o11", "Divert magority water resources to crops to mitagate damage", "s1"), ' \
    '("o12", "Prioritise civiliens, divert recorces to maintain calm, amoung the people ", "s1"),' \
    '("o13", "Allocate recources to adress both heat damage to crops and civil unrest", "s1"),' \
    '("o14", "Blame someone and do nothing", "s1")')

connect.commit()
