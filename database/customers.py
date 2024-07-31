from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv('POSTGRES_DATABASE')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('DB_PORT')

db = PostgresqlDatabase(
    db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
