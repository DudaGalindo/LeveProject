import sqlite3

connection = sqlite3.connect("myTable.db")
crsr = connection.cursor()
#crsr.execute("CREATE TABLE Cursos (ID INT(25), course_name VARCHAR(255))")

query = """INSERT INTO Cursos (id, course_name) VALUES (1, "Administração"),(2, "Ciências Contábeis"),(3, "Engenharia"),(4, "Direito"),(5, "Letras"),(6, "Medicina"),(7, "Odontologia"),(8, "Ciências da Computação")"""

crsr.execute(query)
connection.commit()

# close the connection
connection.close()
