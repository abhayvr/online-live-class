from django.db import models
from student.models import Student
from tutor.models import Tutor

# Create your models here.

class StudyMaterial(models.Model):
    studymaterial_id = models.AutoField(db_column='Studymaterial_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,db_column='Tutor_id')
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='Student_id')
    description = models.CharField(max_length=45)
    study_material = models.CharField(max_length=450)


    class Meta:
        managed = False
        db_table = 'study_material'
