from django.db import models

# Create your models here.
class Outer(models.Model):
    out_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=5)

