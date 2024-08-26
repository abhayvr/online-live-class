from django.db import models

# Create your models here.


class ParentChat(models.Model):
    p_chat_id = models.AutoField(primary_key=True)
    tutor_id = models.IntegerField()
    parent_id = models.IntegerField()
    message = models.CharField(max_length=450)
    rectype = models.CharField(max_length=45)
    sendertype = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'parent_chat'

