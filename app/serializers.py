from rest_framework import serializers
from .models import (User, Palette)

class UserSerializer(serializers.Serializer):
  class Meta:
    model = User
    fields = "__all__"

class PaletteSerializer(serializers.Serializer):
  class Meta:
    model = Palette
    fields = "__all__"