from django.db import models

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    contents = models.TextField(help_text="Comment contents", blank=False, null=False)

    class Meta:
        db_table = "comments"
        managed = False

def get_comment_by_id(id):
    comments = Comments.objects.raw("select * from comments where id = 3")
    print(comments)
    return comments