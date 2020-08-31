# LeveProject
In order to make this project work, you have to activate the virtual enviroment for the backend part and have installed mysql and flask in your machine.
When entering the main file from the command line do: cd ./myproject
After that, you will need to activate the virtual enviroment, typing in terminal: source venv/bin/activate
To run the backend just type: python3 project.py
In order to run the frontend, you will have to open in another terminal, the folder called Brython and then write in terminal the following:
python3 -m http.server
When a student is added, press the first button. If you want to add more students, press Submit Button next, or reload page.
If you want to see all students in your database, you will need to press the last button, bellow the submit button. This will redirect you to another url.

For other cases, do the following (only backend part):
If you want to delete any student from your database, type in your browser:
http://127.0.0.1:5000/alunos/delete?id=TYPEID or http://127.0.0.1:5000/alunos/delete?CPF=TYPECPF
The first one is used if you know the student id in the database, and the seccond one, is used otherwise (assuming you know the student CPF).
If you want to update a student informatio, type in your browser:
http://127.0.0.1:5000/alunos/update?id=TYPEID&Nome=TYPENAME&Telefone=TYPEPHONE&CPF=TYPECPF
for a id that exists in the database and corresponds to the student id from which your want to update the information.
If you want connect a student into a course, that is provided from our database, you can do:
http://127.0.0.1:5000/alunos/curso?id=TYPEID&Matricula=TYPEMATRICULA
where, in place of id you can also specify the CPF and in place of Matricula you can specify the course name. To see all courses that exists in our database, please type in your browser:
http://127.0.0.1:5000/cursos/all
