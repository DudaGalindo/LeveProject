# LeveProject
In order to make this project work, you have to activate the virtual enviroment for the backend part and have installed mysql and flask in your machine.
When entering the main file from the command line do: cd ./myproject
After that, you will need to activate the virtual enviroment, typing in terminal: source venv/bin/activate
To run the backend just type: python3 project.py
In order to add a Student to your database, from your local host server that the backend is running, type in your browser:
http://127.0.0.1:5000/alunos?Nome=TYPENAME&Telefone=TYPEPHONE&CPF=TYPECPF
where, TYPENAME, TYPEPHONE and TYPECPF should be replaced for the student name, phone and CPF, respectfully.
If you want to look at all students in your database type in your browser:
http://127.0.0.1:5000/alunos/all
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
