from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv('POSTGRES_URL')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = int(os.getenv('DB_PORT'))

db = PostgresqlDatabase(db_name)