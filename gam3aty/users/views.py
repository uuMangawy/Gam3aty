from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import FavoriteUniversity, FavoriteCollege, FavoriteMajor, Major, University, College, Profile
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

@login_required
def profile(request):

    fav_universities = FavoriteUniversity.objects.filter(user=request.user)
    fav_colleges = FavoriteCollege.objects.filter(user=request.user)
    fav_majors = FavoriteMajor.objects.filter(user=request.user)

    return render(request, "users/profile.html", {
        "fav_universities": fav_universities,
        "fav_colleges": fav_colleges,
        "fav_majors": fav_majors,
    })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

def login_view(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            error = "No account found with this email"
            return render(request, "users/login.html", {"error": error})

        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid password"

    return render(request, "users/login.html", {"error": error})

@login_required
def add_favorite_major(request, pk):
    major = get_object_or_404(Major, id=pk)

    favorite = FavoriteMajor.objects.filter(
        user=request.user,
        major=major
    )

    if favorite.exists():
        favorite.delete()   # remove from favorites
    else:
        FavoriteMajor.objects.create(
            user=request.user,
            major=major
        )

    return redirect("major", pk=pk)

@login_required
def toggle_favorite_university(request, pk):
    university = get_object_or_404(University, id=pk)

    fav, created = FavoriteUniversity.objects.get_or_create(
        user=request.user,
        university=university
    )

    if not created:
        fav.delete()

    return redirect('university', pk=pk)

@login_required
def toggle_favorite_college(request, pk):
    college = get_object_or_404(College, id=pk)

    fav, created = FavoriteCollege.objects.get_or_create(
        user=request.user,
        college = college
    )

    if not created:
        fav.delete()

    return redirect('college', pk=pk)

def logout_view(request):
    logout(request)
    return redirect("home")

from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile_update(request):
    user = request.user

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect("profile")  # 🔥 redirect after update

    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=profile)

    return render(request, "users/profile_update.html", {
        "u_form": u_form,
        "p_form": p_form,
    })