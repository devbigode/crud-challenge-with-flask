from peewee import Model, CharField, DateTimeField
from database.customers import db
from flask_login import UserMixin
import datetime

class User(Model):
    name = CharField()
    birthday = CharField()
    cpf = CharField(unique=True)
    email = CharField()
    date_register = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Worker(Model, UserMixin):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db