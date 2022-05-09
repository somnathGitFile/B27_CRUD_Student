from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    marks = models.FloatField()
    sdept = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
