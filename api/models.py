from django.db import models

# How to extend user model in django allauth
# https://stackoverflow.com/questions/56192922/how-to-correctly-combine-django-allauth-and-custom-user-profile-app
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  email = models.CharField(max_length=200)
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  # How many palettes they have
  palettes = models.IntegerField(default=0)

  def __str__(self):
    return self.username

class Palette(models.Model):
  # Hexcode / RGBA code
  code = models.CharField(max_length=200)
  # the name the user uses for this palette
  name = models.CharField(max_length=200)
  # the number of likes this palette has
  likes = models.IntegerField(default=0)
  # one user can have many palettes
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
