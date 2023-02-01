from peewee import *
import os

conn = SqliteDatabase('static.db')


class BaseModel(Model):
    class Meta:
        database = conn


class Static(BaseModel):
    char_id = AutoField(column_name='Id')
    char_name = TextField(column_name='Игрок', null=False)
    char_role = TextField(column_name='Роль', null=True)
    char_class = TextField(column_name='Класс', null=True)
    char_itemlvl = FloatField(column_name='Средний илвл', null=True)
    char_set_count = IntegerField(column_name='Сет-вещи', null=True)
    char_set_head = IntegerField(column_name='Голова', null=True)
    char_set_shoulder = IntegerField(column_name='Плечи', null=True)
    char_set_chest = IntegerField(column_name='Грудь', null=True)
    char_set_legs = IntegerField(column_name='Ноги', null=True)
    char_set_hands = IntegerField(column_name='Кисти', null=True)
    char_mythic_done = IntegerField(column_name='Ключ за неделю', null=True)

    class Meta:
        table_name = 'Статик'


def table_start():
    Static.create_table()


table_start()
cursor = conn.cursor()
conn.close()
