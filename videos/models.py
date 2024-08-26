from django.db import models
from student.models import Student
from tutor.models import Tutor

# Create your models here.

class Videos(models.Model):
    videos_id = models.AutoField(db_column='Videos_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,db_column='Tutor_id')
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='Student_id')
    video_upload = models.CharField(db_column='Video_upload', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'videos'