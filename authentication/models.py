from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Deferrable, UniqueConstraint

class UserCustom(models.Model):
    class Meta:
        # db_table = '"name_left_in_lowercase"'
        db_table = 'UserCustom'
    username = models.CharField(max_length=40, default="", unique=True)
    password =  models.CharField(max_length=100,default="")
    salt =  models.CharField(max_length=40,default="")
    UniqueConstraint(
    name='unique_order',
    fields=['username','password'],
    
)
