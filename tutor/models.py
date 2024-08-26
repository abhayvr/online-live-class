from django.db import models

# Create your models here.

class Tutor(models.Model):
    tutor_id = models.AutoField(db_column='Tutor_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=45)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=45)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='Pincode')  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_No', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    education = models.CharField(db_column='Education', max_length=250)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
    availability = models.CharField(db_column='Availability', max_length=45)  # Field name made lowercase.
    status = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    fees = models.CharField(max_length=45)
    fee_category = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'tutor'
