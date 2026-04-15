from django.urls import path
from . import views

urlpatterns = [
    path("colleges/<str:pk>/", views.colleges, name="colleges"),
    path("college/<str:pk>/", views.college, name="college"),
]
