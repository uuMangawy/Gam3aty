from django.urls import path
from . import views

urlpatterns = [
    path("universities/", views.universities, name="universities"),
    path("university/<str:pk>/", views.university, name="university"),
]
