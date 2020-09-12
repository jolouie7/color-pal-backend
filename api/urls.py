from django.urls import path
from . import views

urlpatterns = [
  path("", views.apiOverview, name="api-overview"),
  path("user-list/", views.userList, name="user-list"),
  path("palette-list/", views.paletteList, name="palette-list"),
  path("palette-detail/<str:pk>/", views.paletteDetail, name="palette-detail"),
  path("palette-create/", views.paletteCreate, name="palette-create"),
  path("palette-update/<str:pk>/", views.paletteUpdate, name="palette-update"),
  path("palette-delete/<str:pk>/", views.paletteDelete, name="palette-delete"),
]
