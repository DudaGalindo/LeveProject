# LeveProject
In order to make this project work, you have to activate the virtual enviroment for the backend part and have installed mysql and flask in your machine.
When entering the main file from the command line do: cd ./myproject
After that, you will need to activate the virtual enviroment, typing in terminal: source venv/bin/activate
To run the backend just type: python3 project.py;
In order to run the frontend, you will have to open in another terminal, the folder called Brython and then write in terminal the following:
python3 -m http.server;
After that, open in your browser: localhost:8000/front.html;
This is the frontend page.
When a student is added, press the first button. If you want to add more students, return to localhost:8000/front.html
If you want to see all students in your database, you will need to press the last button in "Cadastrar Pessoas". This will redirect you to another url.
If you want to delete a student, give the person ID in the requested area, and press the button bellow it.
If you want to attribute a student to a course, write in the last section the student ID and their course.

For other cases, do the following (only backend part):
If you want to update a student information, type in your browser:
http://127.0.0.1:5000/alunos/update?id=TYPEID&Nome=TYPENAME&Telefone=TYPEPHONE&CPF=TYPECPF
for a id that exists in the database and corresponds to the student id from which your want to update the information.
