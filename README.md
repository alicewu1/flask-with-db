# flask-with-db
**HHA504 / Cloud Computing / Assignment 4 / Flask and DBs / Part 1**

**This repo aims to: explores database management systems (DBMS) (storage, databases, querying)**
- Connect Flask application to the local database created using SQLITE

**GCP IP:** http://35.194.3.120/ 

**Tasks:**
1. Connect Flask to SQLITE
2. Setup a local DBs on your machine(s) using SQLITE
3. Create an SQLite DB that contains a patient table and a minimum of 4 additional columns for patient details beyond (MRN, first and last name, DOB)
4. Create new fake patients/table using SQLalchemy
5. Create a file called createDB.py in your repo that contains the source code for how these patients were created
6. Inside your flask app, create a new route called ‘/patients’
7. Within the patient-patients route, display the list of patients retrieve from the SQLITE DB
8. Deploy to Azure or GCP and insert IP of machines in readme.md file in repo



**Error encountered:**
1. [SOLVED] "sqlite3.OperationalError: no such table: patient_table"
- Attempted to change .db path to absolute path, but did not resolve the issue
- Encountered issue both on local machine and GCP
- To resolve the issue, I moved the patient.db from templates folder to main directory and including a / in patient.db in the app.py script
