from django.db import models
from student.models import Student
from parent.models import Parent
from tutor.models import Tutor

# Create your models here.

class ExamSchedule(models.Model):
    exam_schedule_id = models.AutoField(db_column='Exam_Schedule_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,db_column='Tutor_id')
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='Student_id')
    #parent_id = models.IntegerField(db_column='Parent_id')  # Field name made lowercase.
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,db_column='Parent_id',null=True)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=150)  # Field name made lowercase.
    questions = models.CharField(max_length=200)
    result = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'exam_schedule'
