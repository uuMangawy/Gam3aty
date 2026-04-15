from django.urls import path
from . import views

urlpatterns = [
    path("majors/<str:pk>", views.majors, name="majors"),
    path("major/<str:pk>", views.major, name="major"),
    path("major/select/<str:pk>/", views.select_major, name="select_major"),
    path("major/compare/<str:pk1>/<str:pk2>", views.compare_majors, name="compare_major"),
    path('explore/majors/', views.explore_majors, name='explore_majors'),

]
