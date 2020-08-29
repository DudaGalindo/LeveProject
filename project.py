import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

Cursos = [
{'Numero Matricula': 0,
 'nome': 'Administração'},
{'Numero Matricula': 1,
 'title': 'Direito'},
{'Numero Matricula': 2,
 'nome': 'Design'},
{'Numero Matricula': 3,
 'nome': 'Letras'}
 ]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/Cursos/all', methods=['GET'])
def api_all():
    return jsonify(Cursos)


@app.route('/api/v1/resources/Cursos', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'Numero Matricula' in request.args:
        id = int(request.args['Numero Matricula'])
    elif 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No  or course name field provided. Please specify an id or course name."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for curso in Cursos:
        if curso['Numero Matricula'] == id:
            results.append(curso)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
