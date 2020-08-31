from browser import document, ajax, window, alert
from browser.html import INPUT, LABEL, BR, FORM, BUTTON,H1

def cadastro_pessoa():
    form = FORM(id="meu-form", action="#", method="get", target="_blank")
    form <= LABEL('Nome', id = 'nome')
    form <= INPUT(id ='Nome', name='Nome')
    form <= BR()
    form <= LABEL('CPF', id = 'cPF')
    form <= INPUT(id ='CPF', type='password', name='CPF')
    form <= BR()
    form <= LABEL('Telefone', id = 'telefone')
    form <= INPUT(id ='Telefone', type='password', name='Telefone')
    form <= BR()
    form <= LABEL('Adicionar', id='add')
    form <= BUTTON(id='submit',name='submit', type='button')
    form <= BR()
    form <= LABEL('Mostrar lista de pessoas:', id='stud_list')
    form <= BUTTON(id='all_students', name='students list', type='button')
    form <= BR()
    form <= H1('Deletar pessoa do banco de dados')
    form <= LABEL('ID da pessoa', id='delete_stud')
    form <= INPUT(id ='id', name='ID')
    form <= BR()
    form <= LABEL('Deletar: ', id='delete_stud')
    form <= BUTTON(id='delete', name='delete', type='button')
    form <= H1('Adicionar curso a pessoa')
    form <= LABEL('ID da pessoa', id='id_pessoa')
    form <= INPUT(id ='id_pcurso', name='ID')
    form <= BR()
    form <= LABEL('Curso', id='curso_type')
    form <= INPUT(id ='curso', name='Curso')
    form <= BR()
    form <= LABEL('Adicionar curso: ', id='add_pessoa_curso')
    form <= BUTTON(id='add_pc', name='add_pc', type='button')
    form <= BR()
    form <= LABEL('Mostrar cursos: ', id='cursos')
    form <= BUTTON(id='show_curso', name='show_cursos', type='button')
    #open('GET', 'http://127.0.0.1:5000/alunos/add', True)
    #get('http://127.0.0.1:5000/alunos/add')
    return form

def get():
    document['submit'].bind('click', submit)

def get_all_students():
    document['all_students'].bind('click', show_all)

def delete_student():
    document['delete'].bind('click', delete)

def get_courses():
    document['show_curso'].bind('click', show_cursos)

def add_pessoa_curso():
    document['add_pc'].bind('click', pessoa_curso)

def pessoa_curso(ev):
    exec(document['submit'].value)
    req = ajax.Ajax()
    curso = document['curso'].value
    ID_pessoa = document['id_pcurso'].value
    url = 'http://127.0.0.1:5000/pessoas/curso'
    window.location.href= (url+"?id=%s&Curso=%s"%(ID_pessoa, curso))

def show_all(ev):
    exec(document['all_students'].value)
    req = ajax.Ajax()
    url = 'http://127.0.0.1:5000/pessoas/all'
    window.location.href=url

def show_cursos(ev):
    exec(document['show_curso'].value)
    url = 'http://127.0.0.1:5000/cursos/all'
    window.location.href= url


def submit(ev):
    exec(document['submit'].value)
    req = ajax.Ajax()
    nome = document['Nome'].value
    telefone = document['Telefone'].value
    cpf = document['CPF'].value
    #req.bind('complete',on_complete(req))
    # pass the arguments in the query string
    url = 'http://127.0.0.1:5000/pessoas/add'
    window.location.href= (url+"?Nome=%s&Telefone=%s&CPF=%s"%(nome, telefone, cpf))

def delete(ev):
    exec(document['delete'].value)
    req = ajax.Ajax()
    id = document['id'].value
    url = ('http://127.0.0.1:5000/pessoas/delete?id=%s' %(id))
    window.location.href = url
