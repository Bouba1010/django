from enum import auto
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    topic= models.ForeignKey (Topic,on_delete=models.SET_NULL,null=True)
    name= models.CharField(max_length=100)
    description= models.TextField(null=True,blank=True)
    createdDate= models.DateTimeField(auto_now_add=True)
    updateDate= models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Message (models.Model):
    room= models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    body= models.TextField(null=False,blank=True)
    dateC= models.DateTimeField(auto_now_add=True)
    updateDate= models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.body[0:50]
    



