from django.db import models
from parent.models import Parent
from tutor.models import Tutor
from student.models import Student

# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_id', primary_key=True)  # Field name made lowercase.
    #parent_id = models.IntegerField(db_column='Parent_id')  # Field name made lowercase.
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,db_column='Parent_id')
    #tutor_id = models.IntegerField(db_column='Tutor_id')  # Field name made lowercase.
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,db_column='Tutor_id')

    card_holder_name = models.CharField(db_column='Card_holder_Name', max_length=45)  # Field name made lowercase.
    card_number = models.CharField(db_column='Card_Number', max_length=45)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'
