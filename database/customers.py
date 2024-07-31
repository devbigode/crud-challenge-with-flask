from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv('POSTGRES_URL')

db = PostgresqlDatabase(db_name)
