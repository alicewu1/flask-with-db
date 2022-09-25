import sqlite3 # note, sqlite3 comes with python3

# Connecting to SQLITE
connect = sqlite3.connect(r"C:\Users\Lcw62\OneDrive\Documents\GitHub\flask-with-db\templates\patient.db")


# db object - creates cursor used throughout db programming
db = connect.cursor()

## EXECUTING A SQL STATEMENT  aka sending a SQL query ##
db.execute("DROP TABLE IF EXISTS patient_table") # delete table patient_table if it exists in patients.db 
connect.commit() # need to commit the current transction using commit()

# If you don't call this method, anything you did since the last call to commit() is not visible from other database connections.


## QUERY: CREATING TABLE/SCHEMA ##
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob DATE NOT NULL,
            address VARCHAR(255) NOT NULL,
            weight NUMBER NOT NULL, 
            haircolor CHAR(25) NOT NULL,
            contactnumber NUMBER NOT NULL
        ); """

# Use ; to end SQL statement

db.execute(table)
connect.commit() # commit the changes 


## INSERTING DUMMY DATA TO THE TABLE ##
## note:.db-journal file is temporary file that is created when you create a database.
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('12045', 'Patty', 'Doe', '01/02/1960', '49 Lexington', '143', 'brown', '8002013456')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('23456', 'George', 'Washington', '12/08/1995', '1903 Maple Ave', '185', 'black', '7001236543')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('37567', 'Dwayne', 'Feldman', '10/29/2002', '154 Henry St', '212', 'gray', '2127892100')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('45624', 'Annie', 'Smith', '08/02/2000', '38 Gate Blvd', '114', 'blonde', '8001230987')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('56739', 'Michelle', 'Lopez', '11/16/1972', '3243 Apple Ave', '138', 'red', '3006784567')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('56739', 'Ray', 'Falo', '03/13/1990', '3243 Eighth Ave', '121', 'black', '4006684537')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('56739', 'Cathy', 'Revere', '07/05/2004', '23 Yellow Ave', '109', 'blonde', '2193452345')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, address, weight, haircolor, contactnumber) values('56739', 'Rudy', 'Hall', '05/12/1984', '3289 Frank St', '147', 'brown', '5673451234')")



# push changes
connect.commit()


## Close the connection and remove .db-journal
connect.close()