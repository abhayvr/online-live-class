from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(db_column='Chat_id', primary_key=True)  # Field name made lowercase.
    student_id = models.IntegerField()
    tutor_id = models.IntegerField()
    sendertype = models.CharField(max_length=100)
    rectype = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'chat'

