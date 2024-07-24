from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    fName = models.CharField(max_length = 200)
    lName = models.CharField(max_length = 200)
    age = models.IntegerField()
    weight = models.IntegerField()