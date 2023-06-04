from peewee import *

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Lab6(BaseModel):
    class Meta:
        db_table = "products"

    id = PrimaryKeyField(unique=True)  # article_number
    name = TextField()
    count = IntegerField()
    price = IntegerField()

    def get_columns(self):
        cursor = db.cursor()
        cursor.execute('PRAGMA table_info("products")')

        return [i[1] for i in cursor.fetchall()]

    def get_rows(self):
        cursor = db.cursor()
        cursor.execute("SELECT * from products")
        rows = cursor.fetchall()

        return rows

    def add_item(self, name, count, price):
        Lab6(name=name, count=count, price=price).save()

    def update_item(self, article, name, count, price):
        lab = Lab6.get(id=article)
        lab.name = name
        lab.count = count
        lab.price = price
        lab.save()
