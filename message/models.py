from django.db import models

# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'question'

