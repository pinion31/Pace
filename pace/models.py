from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import auth
from django import forms

# Create your models here.
ACTIVITY_CHOICES = {
  ('Choose Activity', 'Choose Activity'),
  ('Running', 'Running'),
  ('Walking', 'Walking'),
  ('Weight-lifting', 'Weight-lifting'),
  ('Push-ups', 'Push-ups'),
  ('Sit-ups', 'Sit-ups'),
}

User = auth.get_user_model()

class PaceUser(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username

class Session(models.Model):
    session_length = models.PositiveIntegerField(default=0, blank=True, null=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("pace:session_list")

class Activity(models.Model):
    name= models.CharField(max_length=256, choices=ACTIVITY_CHOICES, default='Choose Activity')
    activity_type = models.CharField(max_length=256)
    hours = models.PositiveIntegerField(default=0)
    minutes = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pace:session_list")



