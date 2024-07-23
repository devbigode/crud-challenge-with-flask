from peewee import Model, CharField, DateField, DateTimeField
from database.customers import db
import datetime

class User(Model):
    name = CharField()
    cpf = CharField(unique=True)
    email = CharField()
    birthday = DateField()
    date_register = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Worker(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db