from django.shortcuts import render
from university.models import University
from .models import College
from users.models import FavoriteCollege
def colleges(request, pk):
    university = University.objects.get(id = pk)
    colleges = university.colleges.all()
    context = {
        "university":university,
        "colleges": colleges
        }
    return render(request, "college/colleges.html",context)


def college(request, pk):
    college = College.objects.get(id = pk)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = FavoriteCollege.objects.filter(
        user=request.user,
        college=college
        ).exists()
    context = {
        "college":college,
        "is_favorite":is_favorite
    }
    return render(request, "college/college.html",context)