from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.email
    
class Activity(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    durationHr = models.IntegerField()
    durationMin = models.IntegerField()
    durationSec = models.IntegerField()
    paceMin =  models.IntegerField()
    paceSec = models.IntegerField()
    heartrate = models.IntegerField()

    def __str__(self):
        return self.title
    
class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=False)
    order = models.IntegerField()