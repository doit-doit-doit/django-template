from django.db import models
from django.http import QueryDict
from django.db import connection

# Create your models here.
class Boards(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=1000, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "boards"
        managed = False

def get_board_list():
    with connection.cursor() as cursor: 
        cursor.execute("select * from boards")
        boards = cursor.fetchall()
    return boards

def get_board_detail(id):
    with connection.cursor() as cursor: 
        cursor.execute("select * from boards where id = 2")
        board = cursor.fetchone()
    return board