from django.db import models
from django.http import QueryDict

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
    print("0")
    boards = Boards.objects.all()
    print(boards.values())
    print("1")
    boards_dict = dict(boards.values())
    print("2")
    boards_dict["attachments"] = "hi"
    print("3")

    modified_query_dict = QueryDict('', mutable=True)
    m#odified_query_dict.update(boards_dict)
    return boards