from django.db import models

# Create your models here.

class student(models.Model):
    roll = models.CharField(max_length=10,unique=True,primary_key=True)
    dept = models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)

class social(models.Model):
    roll = models.CharField(max_length=10,unique=True,primary_key=True)
    dept = models.CharField(max_length=50)
    fb=models.CharField(max_length=100,default='0')
    twr=models.CharField(max_length=100,default='0')
    lin=models.CharField(max_length=100,default='0')
    git = models.CharField(max_length=100,default='0')
    insta = models.CharField(max_length=100,default='0')