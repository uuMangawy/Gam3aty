from . import views
from django.urls import path

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("favorite/major/<int:pk>/", views.add_favorite_major, name="add_favorite_major"),
    path('favorite/university/<int:pk>/', views.toggle_favorite_university, name='toggle_favorite_university'),
    path('favorite/college/<int:pk>/', views.toggle_favorite_college, name='toggle_favorite_college'),
    path('profile/update/', views.profile_update, name='profile_update'),
]