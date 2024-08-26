from django.db import models
from student.models import Student
from tutor.models import Tutor

# Create your models here.

class Doubt(models.Model):
    doubt_id = models.AutoField(db_column='Doubt_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    replay = models.CharField(db_column='Replay', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doubt'
