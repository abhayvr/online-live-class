from django.db import models

# Create your models here.

class Questions(models.Model):
    question_id = models.AutoField(db_column='Question_id', primary_key=True)  # Field name made lowercase.
    questions = models.CharField(db_column='Questions', max_length=500)  # Field name made lowercase.
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(db_column='Correct option', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subject = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'questions'
