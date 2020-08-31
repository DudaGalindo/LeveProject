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

@app.route('/pessoas/update', methods=['GET'])
def update_person():

    if 'id' in request.args:
        id = request.args['id']
    if 'Nome' in request.args:
        name = request.args['Nome']
    else: return "Error: Nome nao especificado. Por favor, especifique o nome."
    if 'Telefone' in request.args:
        phone = str(request.args['Telefone'])
    else: return "Error: Numero de telefone nao especificado. Por favor, especifique o numero de telefone."
    if 'CPF' in request.args:
        CPF = str(request.args['CPF'])

    sql = ("UPDATE pessoas SET name=%s, phone=%s, CPF=%s WHERE id=%s ")
    data = (name, phone, CPF, id)
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object
    mycursor.execute(sql, data)
    mysqldb.commit()
    resp = jsonify('Dados atualizados com sucesso!')
    resp.status_code = 200
    return resp

@app.route('/pessoas/all')
def users():
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object

    mycursor.execute("SELECT * FROM pessoas")
    rows = mycursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp

@app.route('/pessoas/add', methods=['GET'])
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
    else: return "Error: Nome nao foi dado. Por favor, digite o nome."
    if 'Telefone' in request.args:
        phone = str(request.args['Telefone'])
    else: return "Error: Numero de telefone nao foi dado. Por favor, digite o numero de telefone."
    if 'CPF' in request.args:
        CPF = str(request.args['CPF'])
    else: return "Error: CPF nao foi dado. Por favor, digite o CPF."

    try:
        #sql = "DROP TABLE students"
        #mycursor.execute(sql)
        mycursor.execute("CREATE TABLE pessoas (id INT AUTO_INCREMENT PRIMARY KEY, \
                            name VARCHAR(255), phone VARCHAR(255), CPF VARCHAR(255))")
    except:
        mycursor.execute("SELECT * FROM pessoas")
        rows = mycursor.fetchall()
        for row in rows:
            if CPF in row:
                return "Error: Pessoa ja cadastrada na nossa base de dados."

    sql = ("INSERT INTO pessoas (name, phone, CPF) VALUES (%s, %s, %s)")
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
    return jsonify("Pessoa cadastrada com sucesso.")

@app.route('/pessoas/curso', methods= ['GET'])
def add_student_course():
    if 'id' in request.args:
        student_identification = int(request.args['id'])
    else: return "Error: ID da pessoa nao foi dado. Por favor, especifique o ID da pessoa que quer deletar."
    if 'Curso' in request.args:
        course = request.args['Curso']
        course_id = course
    elif 'Matricula' in request.args:
        course = request.args['Matricula']
        course_id = course
    else: return "Error: Curso nao foi dado. Por favor, especifique o curso."

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

    mycursor.execute("SELECT * FROM pessoas")
    rows = mycursor.fetchall()
    verify = False
    for row in rows:
        if student_identification in row:
            verify = True
            id, name, phone, CPF = row
    if not verify: return "Error: Pessoa nao existe na nossa base de dados."

    verify = False
    aux = dict()
    aux['ID estudante'] = id
    aux['Nome'] = name
    aux['Telefone'] = phone
    aux['CPF'] = CPF
    results = []
    for curso in cursos:

        if curso['Numero de Matricula'] == course_id: #not working
            aux['curso'] = curso['Nome']
            verify = True

        if curso['Nome'] == course_id:
            aux['Curso'] = curso['Nome']
            verify = True

    if not verify:
        return "Error: Curso ou Numero de Matricula nao existem na nossa base de dados. Por favor, tente novamente."
    results.append(aux)

    sql_join = ("INSERT INTO conection (name, phone, CPF, curso) VALUES (%s, %s, %s, %s)")
    vals_join = (name,phone,CPF, course_id)
    mycursor.execute(sql_join,vals_join)
    mysqldb.commit()
    mysqldb.close()
    return jsonify(results)

@app.route('/pessoas/delete', methods= ['GET'])
def delete_student():
    if 'id' in request.args:
        id = int(request.args['id'])
    else: return "Error: ID da pessoa nao foi especificado. Por favor, especifique o ID."
    mysqldb = mysql.connect(host = "localhost",
                            user = "maria",
                            password = "hello12345",
                            database = "datacamp") #established connection between your database
    mycursor = mysqldb.cursor() #cursor() method create a cursor object
    mycursor.execute("SELECT * FROM pessoas")
    rows = mycursor.fetchall()
    verify = False
    for row in rows:
        if id in row:
            verify = True
            mycursor.execute("DELETE FROM pessoas WHERE id=%s", (id,))
            mycursor.execute("DELETE FROM conection WHERE id=%s", (id,))
            mysqldb.commit()
            resp = jsonify('User deleted successfully!')
            resp.status_code = 200
            mysqldb.close()
    if not verify: return "ID nao existe. Tente novamente."
    return resp
@app.route("/", methods=["GET"])
def home():
    if request.form:
        print(request.form)
    return render_template("front.html")
app.run()
