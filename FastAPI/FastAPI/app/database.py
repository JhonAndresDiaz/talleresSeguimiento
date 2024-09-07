from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
)

class UserModel(Model):
    id = AutoField(primary_key = True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class TableModel(Model):
    id = AutoField(primary_key = True)
    color = CharField(max_length=20)
    size = CharField(max_length=20)
    numberPeople = CharField(max_length=10)

    class Meta:
        database = database
        table_name = "tables"

class ShirtModel(Model):
    id = AutoField(primary_key = True)
    design = CharField(max_length=30)
    color = CharField(max_length=30)
    typeGarment = CharField(max_length=30)
    size = CharField(max_length=30)

    class Meta:
        database = database
        table_name = "shirts"

class CatModel(Model):
    id = AutoField(primary_key = True)
    name = CharField(max_length=50)
    gender = CharField(max_length=30)
    age = CharField(max_length=30)

    class Meta:
        database = database
        table_name = "cats"

class CarModel(Model):
    id = AutoField(primary_key = True)
    color = CharField(max_length=30)
    amount = CharField(max_length=30)
    price = CharField(max_length=30)
    year = CharField(max_length=30)

    class Meta:
        database = database
        table_name = "cars"