#inactive
import sqlite3

# create tables and insert some data. run it once to initialise the DB
# connect to the database
connect = sqlite3.connect('database.db')

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
    'CREATE TABLE IF NOT EXISTS stats (\
        id INTEGER PRIMARY KEY,\
        statName text NOT NULL\
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

connect.execute(
    'CREATE TABLE IF NOT EXISTS affects (\
        stat_id TEXT,\
        optionMechanic INT NOT NULL,\
        option_id TEXT, \
        PRIMARY KEY (stat_id, option_id),\
        FOREIGN KEY (stat_id) REFERENCES stat(id),\
        FOREIGN KEY (option_id) REFERENCES option(id)\
    )'
)

connect.execute(
    'CREATE TABLE IF NOT EXISTS player (\
       id text PRIMARY KEY\
    )'
)

connect.execute(
    'CREATE TABLE IF NOT EXISTS playerStats (\
        player_id text, \
        stats_id INTEGER, \
        statsValue INTEGER, \
        PRIMARY KEY (player_id, stats_id), \
        FOREIGN KEY (player_id) REFERENCES player(id), \
        FOREIGN KEY (stats_id) REFERENCES stats(id)\
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


cursor.execute('INSERT INTO stats \
    (id, statName) VALUES \
    ("1", "Economy"), \
    ("2", "Military"), \
    ("3", "Security"),\
    ("4", "Welfare"), \
    ("5", "Education"), \
    ("6", "Agriculture")' )

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


cursor.execute('INSERT INTO affects \
    (stat_id, optionMechanic, option_id) VALUES \
    ("6","2","o11"), \
    ("4","-2","o11"), \
    ("6","-2","o12"), \
    ("4","+1","o12"), \
    ("3","-2","o12"), \
    ("6","1","o13"), \
    ("4","1","o13"), \
    ("6","-4","o14"), \
    ("4","1","o21"), \
    ("1","-1","o21"), \
    ("1", "2","o22"), \
    ("4", "-2","o22"), \
    ("4", "-2","o23"), \
    ("1", "-2","o23"), \
    ("4", "-2","o24"), \
    ("1", "-2","o24"), \
    ("4", "-2","o31"), \
    ("3", "-1","o31"), \
    ("1", "-2","o32"), \
    ("5", "2","o32"), \
    ("4", "-1","o32"), \
    ("4", "1","o33"), \
    ("3", "-2","o33"), \
    ("6", "-1","o34"), \
    ("4", "-1","o34"), \
    ("3", "-2","o34")')


connect.execute('INSERT INTO player \
        (id) VALUES ("Pl1")'\
)



cursor.execute('INSERT INTO playerStats \
    (player_id, stats_id, statsValue) VALUES \
    ("Pl1", 1, 0), \
    ("Pl1", 2, 0), \
    ("Pl1", 3, 0),\
    ("Pl1", 4, 0), \
    ("Pl1", 5, 0), \
    ("Pl1", 6, 0)' )



        

connect.commit()
