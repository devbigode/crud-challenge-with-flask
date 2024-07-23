# CRUD Challenge with Flask

Este é um projeto de exemplo de um aplicativo CRUD (Create, Read, Update, Delete) desenvolvido com Flask, Peewee, MySQL e PhpMyAdmin. O objetivo deste projeto é demonstrar como criar uma aplicação web simples que permite realizar operações CRUD em um banco de dados MySQL.

## Tecnologias Utilizadas

Flask
Peewee ORM
MySQL
PhpMyAdmin
Python-dotenv

## Configure as variáveis de ambiente:

    DB_NAME=nome_do_banco_de_dados
    DB_USER=usuario
    DB_PASSWORD=senha
    DB_HOST=localhost
    DB_PORT=3306

Crie um arquivo .env na raiz do projeto com as seguintes informações:

## Nota

Não se esqueça de ajustar o arquivo requirements.txt com as dependências utilizadas no projeto.

    Flask==2.1.1
    peewee==3.14.4
    mysqlclient==2.0.3
    python-dotenv==0.19.2