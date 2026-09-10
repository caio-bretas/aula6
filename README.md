Sistema Web de Gestão de Tarefas

Projeto desenvolvido na Semana 6 — Introdução ao Django, com o objetivo de transformar o Sistema de Gestão de Tarefas, anteriormente executado no terminal, em uma aplicação web utilizando Django.

Participantes
Diego Santos
Caio Bretas
Tecnologias utilizadas
Python
Django
HTML
Git
Funcionalidades

Nesta etapa do projeto, foram implementadas:

Página inicial do sistema;
Listagem de tarefas;
Navegação entre páginas;
Views utilizando Django;
Templates HTML;
Rotas utilizando urls.py;
Dados temporários armazenados em uma lista Python.

Nesta versão, as tarefas ainda não são armazenadas em banco de dados.

Estrutura do projeto
gestao_tarefas/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── tarefas/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── tarefas/
            ├── inicio.html
            └── lista.html

Como executar o projeto
1. Criar o ambiente virtual

No Windows:

python -m venv venv

2. Ativar o ambiente virtual
venv\Scripts\activate

3. Instalar o Django
pip install django

4. Executar o servidor
python manage.py runserver

5. Acessar no navegador

Página inicial:

http://127.0.0.1:8000/


Lista de tarefas:

http://127.0.0.1:8000/tarefas/

Fluxo da aplicação
URL
 ↓
View
 ↓
Template
 ↓
Página HTML

Objetivo da Semana 6

Compreender o funcionamento básico do Django e a integração entre URLs, Views e Templates, preparando o projeto para as próximas etapas, nas quais serão estudados modelos, banco de dados e persistência das tarefas.
