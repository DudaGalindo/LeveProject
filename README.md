# LeveProject
Para fazer esse projeto funcionar, você deve ativar o ambiente virtual para o "backend" e ter instalado as bibliotecas do mysql e do flask.
Quando entrar no arquivo principal do projeto, na linha de comando do seu terminal escreva: cd ./myproject;
Após isso, você precisará ativar o ambiente virtual, escrevendo no terminal o seguinte: source venv/bin/activate.
Para rodar o backend escreva: python3 project.py;
Para rodar o frontend, você deverá abrir outro terminal e entrar na pasta Brython, seguindo: cd ./Brython. Após isso, digite: python3 -m http.server;
Depois, abra uma aba no navegador e escreva: localhost:8000/front.html;
Isso abrirá a página do frontend.
Quando uma pessoa for adicionada, após preencher todas as informações, pressione o primeiro botão. Esse botão vai lhe redirecionar pra uma página mostrando que o estudante foi adicionado. Essa operação de redirecionamento é meramente ilustrativa, pra mostrar que funcionou. Se quiser fazer outras operações, retorne para o localhost: localhost:8000/front.html;
Se você quiser ver todos os estudantes na sua base de dados, pressione o último botão em "Cadastrar Pessoas". Isto vai lhe redirecionar a outra url, lhe mostrando a lista de todos as pessoas existentes no banco de dados.
Se você quer deletar um estudante, digite  o ID da pessoa na área requisitada (esse ID é o que foi gerado durante o cadastro) e pressione o botão logo abaixo.
Se você quiser atribuir um curso a uma pessoa, escreva na última seção da página o ID do estudante e o curso. Isso irá lhe redirecionar à outra página, confirmando o funcionamento do processo.

Para outros casos, faça o seguinte (apenas para o backend):
Se você quer atualizar algum dado da pessoa, escreve no seu navegador:
http://127.0.0.1:5000/alunos/update?id=TYPEID&Nome=TYPENAME&Telefone=TYPEPHONE&CPF=TYPECPF
o ID deve existir na sua base de dados e corresponder ao estudante que você quer atualizar os dados. Para tanto, em TYPENAME, TYPEPHONE e TYPECPF, atualize com o nome, o telefone e o CPF do estudante.
