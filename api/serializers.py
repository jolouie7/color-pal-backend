from rest_framework import serializers
from .models import (User, Palette)

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"


class PaletteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Palette
    fields = "__all__"
