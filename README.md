# CRUD Challenge with Flask

Este é um projeto de exemplo de um aplicativo CRUD (Create, Read, Update, Delete) desenvolvido com Flask, Peewee, MySQL e PhpMyAdmin. O objetivo é demonstrar como criar uma aplicação web simples que permite realizar operações CRUD em um banco de dados MySQL.

## Tecnologias utilizadas

    Flask
    Peewee ORM
    MySQL
    PhpMyAdmin
    Python-dotenv

## Configure as variáveis de ambiente:

Crie um arquivo .env na raiz do projeto com as seguintes informações:

    DB_NAME=nome_do_banco_de_dados
    DB_USER=usuario
    DB_PASSWORD=senha
    DB_HOST=localhost
    DB_PORT=3306
    KEY_LOGIN=chave_aleatoria

## Nota

Não se esqueça de ajustar o arquivo requirements.txt com as dependências utilizadas no projeto.

    Flask==3.0.3
    Flask-Login==0.6.3
    mysqlclient==2.2.4
    peewee==3.17.6
    python-dotenv==1.0.1