from django.db import models

# Create your models here.
# 

class Outer(models.Model):
    out_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=5)


class Event(models.Model):
    name = models.CharField(max_length=10)
class People(models.Model):
    event = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
    school = models.CharField(null=True,max_length=10)
    name = models.CharField(null=True, max_length=5)

class Find(models.Model):
    school = models.CharField(null=True,max_length=10)
    name = models.CharField(null=True, max_length=5)

class Outer2(models.Model):
    out_time = models.DateTimeField(null=True,auto_now_add=True)
    name = models.CharField(null=True,max_length=5)
    school= models.CharField(null=True,max_length=10) #필드 추가
    event = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)#필드 추가