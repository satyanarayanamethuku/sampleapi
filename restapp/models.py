from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobile=models.IntegerField()
    password=models.CharField(max_length=20)


class Login(models.Model):
    mobile=models.IntegerField()
    password=models.CharField(max_length=20)