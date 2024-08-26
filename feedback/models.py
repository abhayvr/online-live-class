from django.db import models
from student.models import Student
from parent.models import Parent
from tutor.models import Tutor

# Create your models here.

class Feedback(models.Model):
    feedback_id = models.AutoField(db_column='FeedBack_id', primary_key=True)  # Field name made lowercase.
    feedback = models.CharField(db_column='Feedback', max_length=500)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    #student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='Student_id')
    #parent_id = models.IntegerField(db_column='Parent_id')  # Field name made lowercase.
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,db_column='Parent_id')
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, db_column='Tutor_id')
    type=models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'feedback'
