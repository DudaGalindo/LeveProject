import flask
from flask import request, jsonify
import mysql.connector as mysql
import sqlite3
from sqlite3 import OperationalError

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# GET couses name and ID's from database.
def api_cursos():
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM Cursos")
    datas = crsr.fetchall()
    cursos = []

    for id, curso in datas:
        aux = dict()
        aux['Numero de Matricula'] = id
        aux['Nome'] = curso
        cursos.append(aux)
    return cursos

cursos = api_cursos()

#def home():
#    return '''<h1>Distant Reading Archive</h1>
#<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/cursos/all', methods=['GET'])
def api_all():
    return jsonify(cursos)

@app.route('/alunos/update', methods=['GET'])
def update_person():

    if 'id' in request.args:
        id = request.args['id']
    if 'Nome' in request.args:
        name = request.args['Nome']
    else: return "Error: Alumn name not provided. Please specify alumn name."
    if 'Telefone' in request.args:
        phone = str(request.args['Telefone'])
    else: return "Error: Alumn phone number not provided. Please specify alumn phone number."
    if 'CPF' in request.args:
        CPF = str(request.args['CPF'])

    sql = ("UPDATE students SET name=%s, phone=%s, CPF=%s WHERE id=%s ")
    data = (name, phone, CPF, id)
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object
    mycursor.execute(sql, data)
    mysqldb.commit()
    resp = jsonify('User updated successfully!')
    resp.status_code = 200
    return resp

@app.route('/alunos/all')
def users():
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object

    mycursor.execute("SELECT * FROM students")
    rows = mycursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp

@app.route('/alunos/add', methods=['GET'])
def add_person():
    # Check if an ID or course name was provided as part of the URL.
    # If ID is provided, check if it exists as part of our database, if it does,
    # assign it to a variable, if it does'nt, display a Error message.
    # The same thing happens with the course name.
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object

    if 'Nome' in request.args:
        name = request.args['Nome']
    else: return "Error: Student name not provided. Please specify student name."
    if 'Telefone' in request.args:
        phone = str(request.args['Telefone'])
    else: return "Error: Student phone number not provided. Please specify student phone number."
    if 'CPF' in request.args:
        CPF = str(request.args['CPF'])
    else: return "Error: Student CPF not provided. Please specify student CPF."

    try:
        #sql = "DROP TABLE students"
        #mycursor.execute(sql)
        mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, \
                            name VARCHAR(255), phone VARCHAR(255), CPF VARCHAR(255))")
    except:
        mycursor.execute("SELECT * FROM students")
        rows = mycursor.fetchall()
        for row in rows:
            if CPF in row:
                return "Error: Student already in our database."

    sql = ("INSERT INTO students (name, phone, CPF) VALUES (%s, %s, %s)")
    val = (name, phone, CPF)
    mycursor.execute(sql, val)
    mysqldb.commit()
    mysqldb.close()
    # Create an empty list for our results
    aux = dict()
    aux['Nome'] = name
    aux['Telefone'] = phone
    aux['CPF'] = CPF
    #aux['ID aluno'] = row['id']
    results = [aux]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/alunos/curso', methods= ['GET'])
def add_student_course():
    if 'id' in request.args:
        student_identification = int(request.args['id'])
    elif 'CPF' in request.args:
        student_identification = request.args['CPF']
    else: return "Error: Student ID or CPF to add course not provided. Please specify at least one."
    if 'Curso' in request.args:
        course = request.args['Curso']
        course_id = course
    elif 'Matricula' in request.args:
        id = int(request.args['Matricula'])
        course_id = id
    else: return "Error: Course name or Matricula Number not provided. Please specify at least one."

    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object
    try:
        #sql = "DROP TABLE conection"
        #mycursor.execute(sql)
        mycursor.execute("CREATE TABLE conection (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), \
                        phone VARCHAR(255), CPF VARCHAR(255), curso VARCHAR(255))")
    except: pass

    mycursor.execute("SELECT * FROM students")
    rows = mycursor.fetchall()
    verify = False
    for row in rows:
        if student_identification in row:
            verify = True
            id, name, phone, CPF = row
    if not verify: return "Error: Student is not in our database."

    verify = False
    aux = dict()
    aux['ID estudante'] = id
    aux['Nome'] = name
    aux['Telefone'] = phone
    aux['CPF'] = CPF
    results = []
    for curso in cursos:
        try:
            if curso['Numero de Matricula'] == course_id:
                aux['curso'] = curso['Nome']
                verify = True

        except:
            if curso['Nome'] == course_id:
                aux['Numero de Matricula'] = curso['Numero de Matricula']
                verify = True

    if not verify:
        return "Error: Course name or Matricula Number provided is not ir our database. Please try again."
    results.append(aux)

    sql_join = ("INSERT INTO conection (name, phone, CPF, curso) VALUES (%s, %s, %s, %s)")
    vals_join = (name,phone,CPF, course_id)
    mycursor.execute(sql_join,vals_join)
    mysqldb.commit()
    mysqldb.close()
    return jsonify(results)

@app.route('/alunos/delete', methods= ['GET'])
def delete_student():
    if 'id' in request.args:
        id = int(request.args['id'])
    else: return "Error: Student ID not provided. Please give the student ID."
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object
    mycursor.execute("SELECT * FROM students")
    rows = mycursor.fetchall()
    verify = False
    for row in rows:
        if id in row:
            verify = True
            mycursor.execute("DELETE FROM students WHERE id=%s", (id,))
            mycursor.execute("DELETE FROM conection WHERE id=%s", (id,))
            mysqldb.commit()
            resp = jsonify('User deleted successfully!')
            resp.status_code = 200
            mysqldb.close()
    if not verify: return "Student ID does not exists"
    return resp
@app.route("/", methods=["GET"])
def home():
    if request.form:
        print(request.form)
    return render_template("front.html")
app.run()
