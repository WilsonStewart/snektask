from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase("tasks.db")


class Task(Model):
    name = CharField()
    description = CharField(null=True)
    task_id = IntegerField(unique=True)
    status = CharField(choices=("New", "Completed"))

    class Meta:
        database = db
