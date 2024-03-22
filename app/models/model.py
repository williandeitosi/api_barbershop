from peewee import *
from datetime import date

db = SqliteDatabase("schedule.db")


class Hour(Model):
    date = DateField(default=date.today())  # Definindo a data atual como padrão
    hour = CharField()
    available = BooleanField(default=True)

    class Meta:
        database = db


def initialize_database():
    db.create_tables([Hour])

    # Adicionar alguns horários predefinidos
    horarios_predefinidos = [
        {"hour": "09:00"},
        {"hour": "10:00"},
        {"hour": "11:00"},
        # Adicione mais horários conforme necessário
    ]

    # Inserir os horários predefinidos na tabela
    for horario in horarios_predefinidos:
        Hour.create(**horario)


class User(Model):
    name = CharField()
    email = CharField(unique=True)
    phone_number = CharField()

    class Meta:
        database = db


if not db.table_exists([Hour]) or not db.table_exists([User]):
    db.create_tables([Hour, User])
