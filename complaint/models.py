from django.db import models
from student.models import Student
from tutor.models import Tutor
# Create your models here.

class Complaint(models.Model):
    complaint_id = models.AutoField(db_column='Complaint_id', primary_key=True)  # Field name made lowercase.
    # tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    # student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    replay = models.CharField(db_column='Replay', max_length=450)  # Field name made lowercase.
    complaint = models.CharField(max_length=450)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaint'
