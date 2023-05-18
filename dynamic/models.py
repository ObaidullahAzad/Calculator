from django.db import models

class Dynamic(models.Model):
    First=models.CharField(max_length=500)
    Last=models.CharField(max_length=500)
    Email=models.CharField(max_length=500)
    Password=models.CharField(max_length=500)
