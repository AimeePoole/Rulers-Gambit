#active
import sqlite3

# create tables and insert some data. run it once to initialise the DB
# connect to the database
connect = sqlite3.connect('database.db')

cursor = connect.cursor()

cursor.execute('INSERT INTO scenario \
    (id, scenarioDescription, catagory_id, phase_id) VALUES \
    ("s5", "A plage of incets threten to inialte your crops, jepoidsing your trade and agriculde", "c1", "p1"), \' \
    ("s10", "You hear rumors of an assasination attempt on your life, what do you do?", "c2", "p1"), \
               


cursor.execute('INSERT INTO options \
    (id, optionDescription, scenario_id) VALUES \
    ("o51", "call emergence coucile, agther your acedemtic and try and find a solution in time ", "s5"), \
    ("o52", "try and move the direction of the hourde (parhaps to sabitage a nabouring countrie) ", "s5"), \
    ("o53", "regardless if crops are ready to be harvested, harvest them and tey to save as much grain as possible ", "s5"), \
    ("o54", "dispatch troops to kill the hourd before they reach the crops ", "s5"), \
    ("o101", "Run an investigation and start arresting people who are suspect ", "s10"), \
    ("o102", "Fortify your castle, barricade the walls to protect yourself ", "s10"), \
    ("o103", "let them try, no one would dear try and assassinate you ", "s10"), \
    
               



cursor.execute('INSERT INTO affects \
    (stat_id, optionMechanic, option_id) VALUES \
    ("4","+1","o51"), \
    ("5","+2","o51"), \
    ("6","+1","o51"), \
    ("2","+1","o52"), \
    ("6","-1","o52"), \
    ("6","+3","o53"), \
    ("4","-1","o53"), \
    ("3","-2","o54"), \
    ("4","-1","o54"), \