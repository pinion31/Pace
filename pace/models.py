from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib import auth
from django import forms

# Create your models here.
class PaceUser(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username

class Session(models.Model):
    session_length = models.PositiveIntegerField()

class Exercise(models.Model):
    name= models.CharField(max_length=256)
    duration = models.PositiveIntegerField()
