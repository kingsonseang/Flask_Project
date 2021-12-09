
import mysql.connector
# from mysql.connector.errors import DatabaseError

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'SCHOOL_PORTAL',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS students(
        STUDENT_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
        first_name VARCHAR(100) NOT NULL,
        middle_name VARCHAR(100),
        last_name VARCHAR(100) NOT NULL,
        age INT CHECK(age>=18),
        GENDER VARCHAR(10),
        phone_number INT(25),
        Gaurdian_name VARCHAR(255),
        Gaurdian_phone_number INT,
        PRIMARY KEY(STUDENT_ID)
    )
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS COURSEs(
        COURSE_ID INT NOT NULL UNIQUE AUTO_INCREMENT,
        COURSE_NAME VARCHAR(255) NOT NULL,  
        PRIMARY KEY(COURSE_ID)
    )
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Departments(
        Department_id INT NOT NULL UNIQUE AUTO_INCREMENT,
        Department_name VARCHAR(255) NOT NULL,
        PRIMARY KEY(Department_id)
    )
    """
)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS COURSE_REG(
        COURSE_REG_ID INT AUTO_INCREMENT,
        PRIMARY KEY(COURSE_REG_ID)
    )
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS LECTURERs(
        LECTURERs_id INT NOT NULL UNIQUE AUTO_INCREMENT,
        first_name VARCHAR(100) NOT NULL,
        middle_name VARCHAR(100),
        last_name VARCHAR(100) NOT NULL,
        age INT CHECK(age>=18),
        phone_number INT(25),
        next_of_kin_name VARCHAR(255),
        next_of_kin_phone_number INT,
        PRIMARY KEY(LECTURERs_id)
    )
    """
)

mycursor.execute(
    """ALTER TABLE students ADD COLUMN IF NOT EXISTS(
        username VARCHAR(255),
        DOB INT,
        password VARCHAR(255),
        email VARCHAR(255),
        registered_courses INT,
        FOREIGN KEY(registered_courses) REFERENCES COURSE_REG(COURSE_REG_ID)
    )
    """
)

mycursor.execute(
    """ALTER TABLE students ADD COLUMN IF NOT EXISTS(
        Recovery_Question VARCHAR(255),
        Recovery_Question_Ans VARCHAR(255)
    )
    """
)

mycursor.execute(
    """ALTER TABLE students ADD COLUMN IF NOT EXISTS(
        DEPARTMENT INT,
        FOREIGN KEY(DEPARTMENT) REFERENCES Departments(Department_id)
    )
    """
)


mycursor.execute(
    """ALTER TABLE COURSEs ADD COLUMN IF NOT EXISTS(
        DEPARTMENT INT,
        FOREIGN KEY(DEPARTMENT) REFERENCES Departments(Department_id)
    )
    """
)

mycursor.execute(
    """ALTER TABLE LECTURERs ADD COLUMN IF NOT EXISTS(
        DEPARTMENT_ID INT,
        FOREIGN KEY(DEPARTMENT_ID) REFERENCES Departments(Department_id)
    )
    """
)

mycursor.execute(
    """ALTER TABLE COURSEs ADD COLUMN IF NOT EXISTS(
        LECTURER INT,
        FOREIGN KEY(LECTURER) REFERENCES LECTURERS(LECTURERS_ID)
    )
    """
)

mycursor.execute(
    """ALTER TABLE Departments ADD COLUMN IF NOT EXISTS(
        SUPERVISOR INT,
        FOREIGN KEY(SUPERVISOR) REFERENCES LECTURERS(LECTURERS_ID)
    )
    """
)

mycursor.execute(
    """ALTER TABLE COURSE_REG ADD COLUMN IF NOT EXISTS(
        STUDENT_ID INT NOT NULL,
        FOREIGN KEY(STUDENT_ID) REFERENCES students(STUDENT_ID)
    )
    """
)


mycursor.execute(
    """ALTER TABLE LECTURERs ADD COLUMN IF NOT EXISTS(
        password varchar(100),
        email varchar(100)
    )
    """
)

mycursor.execute(
    """ALTER TABLE COURSE_REG ADD COLUMN IF NOT EXISTS(
        COURSE_ID INT NOT NULL,
        FOREIGN KEY(COURSE_ID) REFERENCES COURSEs(COURSE_ID)
    )
    """
)

mycursor.execute(
    """ALTER TABLE COURSE_REG ADD COLUMN IF NOT EXISTS(
        COURSE_NAME VARCHAR(255)
    )
    """
)