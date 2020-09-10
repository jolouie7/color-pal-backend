from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (UserSerializer, PaletteSerializer)
from .models import (User, Palette)

# Create your views here.
@api_view(["GET"])
def apiOverview(request):
  api_urls = {
    "List": "/palette-list/",
    "Detail View": "/palette-detail/<str:pk>/",
    "Create": "/palette-create/",
    "Update": "/palette-update/<str:pk>/",
    "Delete": "/palette-delete/<str:pk>/",
  }

  return Response(api_urls)

# return all palettes
@api_view(["GET"])
def paletteList(request):
  palettes = Palette.objects.all().order_by("-id")
  serializer = PaletteSerializer(palettes, many=True)
  return Response(serializer.data)

# return a specfic palette
@api_view(["GET"])
def paletteDetail(request, pk):
  palette = Palette.objects.get(id=pk)
  serializer = PaletteSerializer(palette, many=False)
  return Response(serializer.data)

# Create a palette
@api_view(["POST"])
def paletteCreate(request):
  serializer = PaletteSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

# update palette
@api_view(["POST"])
def paletteUpdate(request, pk):
  palette = Palette.objects.get(id=pk)
  serializer = PaletteSerializer(instance=palette, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

# delete palette
@api_view(["DELETE"])
def paletteDelete(request, pk):
  palette = Palette.objects.get(id=pk)
  palette.delete()
  return Response("Palette successfully deleted!")
