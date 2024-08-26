from django.db import models
from student.models import Student
from tutor.models import Tutor

# Create your models here.

class Live(models.Model):
    live_id = models.AutoField(db_column='Live_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    live_class = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'live'
