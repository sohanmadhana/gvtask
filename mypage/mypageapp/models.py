from django.db import models
from django.http import request

# Create your models here.

class Employee(models.Model):
   
    # id = models.IntegerField(null=False,primary_key=True )
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    contact = models.IntegerField(null=False)
    salary = models.IntegerField(default=1000000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name 


                  