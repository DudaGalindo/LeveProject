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


mysqldb = mysql.connect(host = "localhost",
                        user = "maria",
                        password = "hello12345",
                        database = "datacamp")#established connection between your database
mycursor = mysqldb.cursor() #cursor() method create a cursor object

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/pessoas/all', methods=['GET'])
def api_all():
    return jsonify(pessoas)

@app.route('/info', methods=['GET'])
def api_course():
    # Check if an ID or course name was provided as part of the URL.
    # If ID is provided, check if it exists as part of our database, if it does,
    # assign it to a variable, if it does'nt, display a Error message.
    # The same thing happens with the course name.
    if 'Nome' in request.args:
        name = request.args['Nome']
    else: return "Error: Alumn name not provided. Please specify alumn name."
    if 'Telefone' in request.args:
        phone = str(request.args['Telefone'])
    else: return "Error: Alumn phone number not provided. Please specify alumn phone number."
    if 'CPF' in request.args:
        CPF = str(request.args['CPF'])
    else: return "Error: Alumn CPF not provided. Please specify alumn CPF."
    if 'Curso' in request.args:
        course = request.args['Curso']
    elif 'Matricula' in request.args:
        id = int(request.args['Matricula'])
    else: return "Error: Course name or Matricula Number not provided. Please specify at least one."
    try:
        sql = "DROP TABLE students"
        mycursor.execute(sql)
        mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(255), CPF VARCHAR(255))")
    except: pass

    sql = ("INSERT INTO students (name, phone, CPF) VALUES (%s, %s, %s)")
    val = (name, phone, CPF)
    mycursor.execute(sql, val)

    # Create an empty list for our results
    results = [{'Name':name, 'Phone':phone, 'CPF':CPF}]

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    verify = False
    for curso in cursos:
        aux = dict()
        try:
            if curso['Numero de Matricula'] == id:
                aux['Curso'] = 'Curso'
                verify = True
                results.append(curso)
        except:
            if curso['Nome'] == name:
                verify = True
                results.append(curso)
    if not verify:
        return "Error: Course name or Matricula Number provided is not ir our database. Please try again."
    #return "Error: Course name or ID does not exist. Please specify a valid course name or ID."
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
app.run()
