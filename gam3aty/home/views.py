from django.shortcuts import render
from django.db.models import Count

from users.models import FavoriteUniversity, FavoriteCollege, FavoriteMajor, Major, University, College

def home(request):

    # ===== Top Universities =====
    top_universities = University.objects.annotate(
        total_favorites=Count('favoriteuniversity')
    ).order_by('-total_favorites')[:5]

    # ===== Top Colleges =====
    top_colleges = College.objects.annotate(
        total_favorites=Count('favoritecollege')
    ).order_by('-total_favorites')[:5]

    # ===== Top Majors =====
    top_majors = Major.objects.annotate(
        total_favorites=Count('favoritemajor')
    ).order_by('-total_favorites')[:5]

    context = {
        "top_universities": top_universities,
        "top_colleges": top_colleges,
        "top_majors": top_majors,
    }

    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")