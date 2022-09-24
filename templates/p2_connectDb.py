import sqlite3
import pandas as pd
import os.path

db_path = os.path.join("patient.db")

def get_db_connection():
    conn = sqlite3.connect(r"C:\Users\Alice\Documents\GitHub\flask-with-db\templates\patient.db")
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall() # Select * means get "all" columns
patientListSql

# gut check: save the data to a dataframe
df = pd.DataFrame(patientListSql)
df

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'address', 'weight', 'haircolor', 'contactnumber']
df

