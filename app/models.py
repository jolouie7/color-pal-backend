from django.db import models

class User(models.Model):
  email = models.CharField(max_length=200)
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  # How many palettes they have
  palettes = models.IntegerField(default=0)

  def __str__(self):
    return self.email

class Palette(models.Model):
  # Hexcode / RGBA code
  code = models.CharField(max_length=200)
  # the name the user uses for this palette
  name = models.CharField(max_length=200)
  # the number of likes this palette has
  likes = models.IntegerField(default=0)

  def __str__(self):
    return self.name