from statistics import mode
from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=255)
    education=models.CharField(max_length=255)
    skills=models.TextField()
    photo=models.ImageField(upload_to='userImage',null=True,default='no image')
    document=models.FileField(upload_to='userDoc',null=True,default='no image')
    created_at=models.DateTimeField(auto_now_add=True)
