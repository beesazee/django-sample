from django.db import models
from json import dumps
# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=16,default='male')
    designation = models.CharField(max_length=64)
    department = models.CharField(max_length=64)

    def __unicode__(self):
        #employee_information =
        return dumps({'first name' : self.first_name,
                      'last name' : self.last_name,
                      'age' : self.age})