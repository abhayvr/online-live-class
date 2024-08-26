from django.db import models

# Create your models here.

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', max_length=45)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'
