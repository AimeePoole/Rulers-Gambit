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


cursor.execute('INSERT INTO scenario \
    (id, scenarioDescription, catagory_id, phase_id) VALUES \
    ("s1", "A heatwave has swept the nation, resulting in civil unrest and exstresive damage to crops. You must find a way to rectifi the sitchuation will you?", "c1", "p1"), \
    ("s2", "A storm has hit your southern frount, disrupting trade, uprooting citizens and damaging infulstructure. How will you respond?", "c1", "p1"), \
    ("s3", "The rains have been barren for servil days, people are running out of water, and drying on the streets, the crops wither in reflection, what will you do?", "c1", "p1")')


cursor.execute('INSERT INTO options \
    (id, optionDescription, scenario_id) VALUES \
    ("o11", "Divert majority water resources to crops to mitigate damage", "s1"), \
    ("o12", "Prioritise civilians, divert resources to maintain calm among the people", "s1"), \
    ("o13", "Allocate resources to address both heat damage to crops and civil unrest", "s1"), \
    ("o14", "Blame someone and do nothing", "s1"), \
    ("o21", "Allocate aid to citizens, relocating all who have been disrupted by the storm", "s2"), \
    ("o22", "Aid lost infrastructure and trade to try and prevent more economic losses", "s2"), \
    ("o23", "Cry", "s2"), \
    ("o24", "Do nothing", "s2"), \
    ("o31", "Beg the gods, conserve what you can", "s3"), \
    ("o32", "Fund a mass research project", "s3"), \
    ("o33", "Cull the few to protect the many, kill a small population to conserve resources", "s3"), \
    ("o34", "Cry", "s3")')



connect.commit()
