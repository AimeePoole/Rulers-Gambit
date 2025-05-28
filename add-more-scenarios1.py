#inactive
import sqlite3

# create tables and insert some data. run it once to initialise the DB
# connect to the database
connect = sqlite3.connect('database.db')



cursor = connect.cursor()

cursor.execute('INSERT INTO scenario \
    (id, scenarioDescription, catagory_id, phase_id) VALUES \
    ("s4", "A cold front is predicted; how will you prepare?", "c1", "p1"), \
    ("s6", "Tustland has attacked Kevian Rus, Refugees are heading towards our boarders, what do you do?", "c2", "p1"), \
    ("s7", "You are bombed by Tyskland. Over 150 civilians were killed, what do you do?", "c2", "p1"),\
    ("s8", "Tustland attacks you at shores, what do you do?", "c2", "p1"), \
    ("s9", "Tyskland has declared war against you, what do you do?", "c2", "p1")')


cursor.execute('INSERT INTO options \
    (id, optionDescription, scenario_id) VALUES \
    ("o41", "there is no cold front, no need to prepare anything, we will be fine", "s4"), \
    ("o42", "prepare stores, give out blankets to the people, ensure that all have a place to keep walm", "s4"), \
    ("o43", "Fuck the poor - do nothing ", "s4"), \
    ("o44", "ask for help from an ally", "s4"), \
    ("o61", "Place the military on the boarder", "s6"), \
    ("o62", "Allow all the refugees into your country", "s6"), \
    ("o63", "Negotiate with Gaul to take half the refugees each", "s6"), \
    ("o64", "Negotiate with other country Gaul for them to take all the refugees in exchange for some economic support", "s6"), \
    ("o71", "Use this to convince people to sign up for the war", "s7"), \
    ("o72", "Create planes to bomb them back ", "s7"), \
    ("o73", "Invest in air raid shelters and other preventative measures", "s7"), \
    ("o74", "Use a conscription/draft and force people to join the military", "s7"), \
    ("o81", "Fight back", "s8"), \
    ("o82", "Fortify", "s8"), \
    ("o83", "Ask for help from an ally", "s8"), \
    ("o84", "Negotiate with other country Gaul", "s8"), \
    ("o91", "Declare war back", "s9"), \
    ("o92", "Attempt to negotiate with other country", "s9"), \
    ("o93", "Attack", "s9"), \
    ("o94", "Ask for help from an ally", "s9")')


cursor.execute('INSERT INTO affects \
    (stat_id, optionMechanic, option_id) VALUES \
    ("4","-1","o41"), \
    ("1","-2","o41"), \
    ("4","1","o42"), \
    ("1","-1","o42"), \
    ("4","-2","o43"), \
    ("1","-2","o43"), \
    ("1","-1","o44"), \
    ("4","1","o44"), \
    ("2","-1","o61"), \
    ("4","-2","o62"), \
    ("6","2","o62"), \
    ("4","-1","o63"), \
    ("3","1","o63"), \
    ("1","-2","o64"), \
    ("4","1","o64"), \
    ("2","2","o71"), \
    ("6","-1","o71"), \
    ("3","-1","o71"), \
    ("5","1","o72"), \
    ("2","-2","o72"), \
    ("1","-2","o73"), \
    ("3","1","o73"), \
    ("2","2","o74"), \
    ("4","-2","o74"), \
    ("2","-1","o81"), \
    ("2","-1","o82"), \
    ("3","1","o82"), \
    ("2","1","o83"), \
    ("1","-1","o83"), \
    ("1","-1","o84"), \
    ("2","-1","o84"), \
    ("4","-1","o91"), \
    ("2","1","o91"), \
    ("1","-1","o92"), \
    ("4","-1","o92"), \
    ("2","-1","o93"), \
    ("4","-1","o93"), \
    ("1","-1","o94"), \
    ("2","1","o94")' \
    '')

connect.commit()
