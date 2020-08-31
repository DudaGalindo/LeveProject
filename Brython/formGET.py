from browser import document, ajax, window, alert
from browser.html import INPUT, LABEL, BR, FORM, BUTTON

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
    form <= LABEL('Add', id='add')
    form <= BUTTON(id='submit',name='submit', type='button')
    form <= BR()
    form <= LABEL('NEXT', id='add')
    form <= INPUT(id='next', name='next', type='submit')
    form <= BR()
    form <= LABEL('Students List', id='stud_list')
    form <= BUTTON(id='all_students', name='students list', type='button')
    #open('GET', 'http://127.0.0.1:5000/alunos/add', True)
    #get('http://127.0.0.1:5000/alunos/add')
    return form

def get():
    document['submit'].bind('click', exec_python)

def exec_python(ev):
    exec(document['submit'].value)
    req = ajax.Ajax()
    nome = document['Nome'].value
    telefone = document['Telefone'].value
    cpf = document['CPF'].value
    #req.bind('complete',on_complete(req))
    # pass the arguments in the query string
    url = 'http://127.0.0.1:5000/alunos/add'
    req.open('GET',url+"?Nome=%s&Telefone=%s&CPF=%s" %(nome, telefone, cpf),True)
    req.set_header('content-type','application/x-www-form-urlencoded', 'Access-Control-Allow-Origin')
    req.send()
    window.location.href=url

def get_all_students():
    document['all_students'].bind('click', show_all)

def show_all(ev):
    exec(document['all_students'].value)
    req = ajax.Ajax()
    url = 'http://127.0.0.1:5000/alunos/all'
    req.open('GET',url,True)
    req.set_header('content-type','application/x-www-form-urlencoded', 'Access-Control-Allow-Origin')
    req.send()
    window.location.href=url
