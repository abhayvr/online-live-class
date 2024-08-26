from django.db import models
from student.models import Student
from parent.models import Parent
from tutor.models import Tutor

# Create your models here.

class Notifications(models.Model):
    notification_id = models.AutoField(db_column='Notification_id', primary_key=True)  # Field name made lowercase.
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,db_column='Tutor_id')
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='Student_id')
    #parent_id = models.IntegerField(db_column='Parent_id')  # Field name made lowercase.
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,db_column='Parent_id',null=True)
    notification = models.CharField(db_column='Notification', max_length=400)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notifications'
