from flask import Flask, render_template, redirect, request
from db import mydb, mycursor

app = Flask(__name__)
username = 'solomon'
password = '1811'

@app.route('/')
def index():
    return render_template('n.html')


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/Reg', methods = ["GET", "POST"])
def Reg():
    if request.method == "GET":
        mycursor.execute(f'SELECT * FROM Departments')
        Departments = mycursor.fetchall()
        return render_template("student_portal_student_reg.html", Departments = Departments)
    if request.method == "POST":
        _first_name = request.form['first_name']
        _middle_name = request.form['middle_name']
        _last_name = request.form['last_name']
        _DOB = request.form['DOB']
        _age = request.form['age']
        _phone_number = request.form['phone_number']
        _email = request.form['email']
        _username = request.form['username']
        _gender = request.form['gender']
        _Gaurdian_name = request.form['Gaurdian_name']
        _Gaurdian_phone_number = request.form['Gaurdian_phone_number']
        _password = request.form['password']
        _Department = request.form['Department_id']
        _Recovery_Question = request.form['Recovery_Question']
        _Recovery_Question_Ans = request.form['Recovery_Question_Ans']
        sql = 'INSERT INTO students (first_name, middle_name, last_name, DOB, age, phone_number, email, username, Gaurdian_name, Gaurdian_phone_number, password, GENDER, DEPARTMENT, Recovery_Question, Recovery_Question_Ans) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (_first_name, _middle_name, _last_name, _DOB, _age, _phone_number, _email, _username, _Gaurdian_name, _Gaurdian_phone_number, _password, _gender, _Department, _Recovery_Question, _Recovery_Question_Ans)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/login')


@app.route('/login', methods = ["GET", "POST"])
def login():
    message =''
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == "POST":
        _loginname = request.form["username"]
        _loginpassword = request.form["password"]
        mycursor.execute(f'SELECT * FROM students WHERE username = "{_loginname}" AND password = "{_loginpassword}" ')
        verify = mycursor.fetchone()
        print(verify)
        if verify:
            return redirect(f"/student-portal/{verify['STUDENT_ID']}")
        else :
            message = "failed to login with credentials"
            return render_template('login.html', msg = message)      

@app.route('/student-portal/<int:id>')
def student_portal(id):
    mycursor.execute(f'SELECT * FROM students WHERE STUDENT_ID="{id}"')
    student = mycursor.fetchone()
    mycursor.execute(f'SELECT * FROM COURSE_REG WHERE STUDENT_ID = "{id}"')
    course = mycursor.fetchall()
    print(course)
    return render_template('student_portal.html', student = student, course = course)


@app.route('/Lecturer-login', methods = ["GET", "POST"])
def Lecturer_login():
    message =''
    if request.method == 'GET':
        return render_template('Lecturer_login.html')
    if request.method == "POST":
        _loginemail = request.form["email"]
        _loginpassword = request.form["password"]
        mycursor.execute(f'SELECT * FROM LECTURERs WHERE email = "{_loginemail}" AND password = "{_loginpassword}" ')
        verify = mycursor.fetchone()
        print(verify)
        if verify:
            return redirect(f"/Lecturer-portal/{verify['LECTURERs_id']}")
        else :
            message = "failed to login with credentials"
            return render_template('Lecturer_login.html', msg =message)      

@app.route('/Lecturer-portal/<int:id>')
def Lecturer_portal(id):
    mycursor.execute(f'SELECT * FROM COURSEs WHERE LECTURER="{id}"')
    courses = mycursor.fetchall()
    mycursor.execute(f'SELECT * FROM LECTURERs WHERE LECTURERs_ID="{id}"')
    LECTURER = mycursor.fetchone()
    return render_template('Lecturer_portal.html', LECTURER = LECTURER, courses = courses)

@app.route('/reg_course/<int:id>', methods=(['GET', 'POST']))
def reg_course(id):
    # message = ''
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Courses')
        courses = mycursor.fetchall()
        return render_template('reg_course.html', courses = courses, id=id)
    if request.method == 'POST':
        user = mycursor.fetchone()
        # _StudentID = request.form ["number"]
        # _course = request.form ["course{{course.COURSE_ID}}"]
        for val in request.form:
            if val == 'submit':
                pass
            else:
                sql = 'INSERT INTO COURSE_REG (STUDENT_ID, COURSE_ID) VALUES (%s,%s)'
                val = (id, val)
                mycursor.execute(sql, val)
                mydb.commit()
        # mycursor.execute(f'INSERT INTO COURSE_REG (STUDENT_ID) VALUES({_StudentID})')
        # mydb.commit()
        mycursor.execute(f'SELECT * FROM students WHERE STUDENT_ID = "{id}"')
        user = mycursor.fetchone()
        print(user)
        return redirect(f"/student-portal/{user['STUDENT_ID']}")
        # return 'hi'
        # return redirect(f"/student-portal/{user['STUDENT_ID']}")
        # return render_template('reg_course.html', msg = message) 
    

@app.route('/course/<int:id>', methods=(['GET', 'POST']))
def course(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM COURSEs WHERE COURSE_ID = "{id}"')
        course = mycursor.fetchone()
        print(course)
        # mycursor.execute(f'SELECT * FROM LECTURERs WHERE LECTURERs_id = "{course.LECTURER}"')
        # Lecturer = mycursor.fetchone()
        # print(Lecturer)
        return render_template('course.html', course = course)


@app.route('/password_recovery', methods=(['GET', 'POST']))
def password_recovery():
    if request.method == 'GET':
        return render_template('password_recovery.html')
    if request.method == 'POST':
        _email = request.form['email']
        _Recovery_Question_ans = request.form['Recovery_Question_ans']
        _password = request.form['password']
        mycursor.execute(f'SELECT * FROM students WHERE email = "{_email}" AND Recovery_Question_ans = "{_Recovery_Question_ans}"')
        user = mycursor.fetchone()
        print(user)
        mycursor.execute(f"UPDATE students SET password = '{_password}' WHERE STUDENT_ID ='{user['STUDENT_ID']}'")
        mydb.commit()
        return redirect('/login')

if __name__ == '__main__':
    app.run()