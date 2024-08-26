from django.db import models
from student.models import Student
from parent.models import Parent
from tutor.models import Tutor

# Create your models here.

class CurrentProgres(models.Model):
    current_progres_id = models.AutoField(db_column='Current_Progres_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,db_column='Tutor_id')
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='Student_id')
    #parent_id = models.IntegerField(db_column='Parent_id')  # Field name made lowercase.
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,db_column='Parent_id')
    progress_report = models.CharField(db_column='Progress _Report', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'current_progres'
