import sqlite3

def create_tables():
    conn = sqlite3.connect("HospitalDB.db")
    c = conn.cursor()

    # The following lines are commented out to prevent accidental table recreation.
    # To initialize the database, uncomment these lines and run this script directly.

    # conn.execute("DROP TABLE IF EXISTS PATIENT")
    # conn.execute("""CREATE TABLE PATIENT
    #           (PATIENT_ID INT(10) PRIMARY KEY,
    #            NAME VARCHAR(20) NOT NULL,
    #            SEX VARCHAR(10) NOT NULL,
    #            BLOOD_GROUP VARCHAR(5) NOT NULL,
    #            DOB DATE NOT NULL,
    #            ADDRESS VARCHAR(100) NOT NULL,
    #            CONSULT_TEAM VARCHAR(50) NOT NULL,
    #            EMAIL VARCHAR(20) NOT NULL
    #           )""")
    # print("PATIENT TABLE CREATED SUCCESSFULLY")
    #
    # conn.execute("DROP TABLE IF EXISTS CONTACT_NO")
    # conn.execute("""CREATE TABLE CONTACT_NO
    #           (PATIENT_ID INT(10) PRIMARY KEY,
    #            CONTACTNO INT(15) NOT NULL,
    #            ALT_CONTACT INT(15),
    #            FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID))
    #           """)
    # print("CONTACT_NO TABLE CREATED SUCCESSFULLY")
    #
    # conn.execute("DROP TABLE IF EXISTS employee")
    # conn.execute("""CREATE TABLE employee
    #           (EMP_ID VARCHAR(10) PRIMARY KEY,
    #            EMP_NAME VARCHAR(20) NOT NULL,
    #            SEX VARCHAR(10) NOT NULL,
    #            AGE INT(5) NOT NULL,
    #            DESIG VARCHAR(20) NOT NULL,
    #            SAL INT(10) NOT NULL,
    #            EXP VARCHAR(100) NOT NULL,
    #            EMAIL VARCHAR(20) NOT NULL,
    #            PHONE INT(12))""")
    # print("EMPLOYEE TABLE CREATED SUCCESSFULLY")
    #
    # conn.execute("DROP TABLE IF EXISTS TREATMENT")
    # conn.execute("""CREATE TABLE TREATMENT
    #           (PATIENT_ID INT(10) PRIMARY KEY,
    #            TREATMENT VARCHAR(100) NOT NULL,
    #            TREATMENT_CODE VARCHAR(30) NOT NULL,
    #            T_COST INT(20) NOT NULL,
    #            FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
    #           """)
    # print("TREATMENT TABLE CREATED SUCCESSFULLY")
    #
    # conn.execute("DROP TABLE IF EXISTS MEDICINE")
    # conn.execute("""CREATE TABLE MEDICINE
    #           (PATIENT_ID INT(10) PRIMARY KEY,
    #            MEDICINE_NAME VARCHAR(100) NOT NULL,
    #            M_COST INT(20) NOT NULL,
    #            M_QTY INT(10) NOT NULL,
    #            FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
    #           """)
    # print("MEDICINE TABLE CREATED SUCCESSFULLY")
    #
    # conn.execute("DROP TABLE IF EXISTS ROOM")
    # conn.execute("""CREATE TABLE ROOM
    #          (PATIENT_ID INT(10) NOT NULL ,
    #           ROOM_NO VARCHAR(20) PRIMARY KEY ,
    #           ROOM_TYPE VARCHAR(10) NOT NULL,
    #           RATE INT(10) NOT NULL,
    #           DATE_ADMITTED DATE,
    #           DATE_DISCHARGED DATE NULL,
    #           FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
    #           );
    #          """)
    # print("ROOM TABLE CREATED SUCCESSFULLY")
    #
    # conn.execute("DROP TABLE IF EXISTS APPOINTMENT")
    # c.execute("""CREATE TABLE appointment
    #             (
    #              PATIENT_ID INT(20) NOT NULL,
    #              EMP_ID VARCHAR(10) NOT NULL,
    #              AP_NO VARCHAR(10) PRIMARY KEY,
    #              AP_TIME TIME,
    #              AP_DATE DATE,
    #              description VARCHAR(100),
    #              FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID),
    #              FOREIGN KEY(EMP_ID) REFERENCES employee(EMP_ID));""")
    # print("APPOINTMENT TABLE CREATED SUCCESSFULLY")

    # conn.execute("DROP TABLE IF EXISTS USERS")
    # c.execute("""CREATE TABLE USERS
    #             (
    #              USERNAME TEXT NOT NULL PRIMARY KEY,
    #              PASSWORD TEXT NOT NULL
    #             );""")
    # c.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)", ('admin', '1234'))
    # c.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)", ('root', '4321'))
    # print("USERS TABLE CREATED SUCCESSFULLY")

    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect("HospitalDB.db")
    return conn

if __name__ == '__main__':
    create_tables()
    print("Database `HospitalDB.db` setup complete.")
    print("To re-initialize the database, uncomment the table creation queries in `create_tables` function.")
