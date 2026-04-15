from django.shortcuts import render, get_object_or_404
from college.models import College
from university.models import University
from .models import Major, Category
from users.models import FavoriteMajor
def majors(request, pk):
    college = College.objects.get(id = pk)
    majors = college.majors.all()
    context = {
        "college":college,
        "majors":majors,
        }
    return render(request, "major/majors.html", context)


def major(request, pk):
    major = get_object_or_404(Major, id=pk)

    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = FavoriteMajor.objects.filter(
            user=request.user,
            major=major
        ).exists()

    context = {
        "major": major,
        "is_favorite": is_favorite
    }
    
    return render(request, "major/major.html", context)


def select_major(request, pk):
    base_major = get_object_or_404(Major, id=pk)

    # الفلاتر من GET
    univ_id = request.GET.get('university')
    coll_id = request.GET.get('college')
    cat_id = request.GET.get('category')

    # استبعاد التخصص الأساسي
    majors = Major.objects.exclude(id=pk)

    # فلترة حسب الجامعة
    if univ_id:
        majors = majors.filter(college__university_id=univ_id)
        # عرض فقط الكليات التابعة للجامعة المختارة
        colleges = College.objects.filter(university_id=univ_id).order_by('name')
    else:
        colleges = College.objects.all()  # لا تعرض أي كلية إذا لم يتم اختيار جامعة

    # فلترة حسب الكلية
    if coll_id:
        majors = majors.filter(college_id=coll_id)

    # فلترة حسب الفئة
    if cat_id:
        majors = majors.filter(categories__id=cat_id)

    context = {
        "base_major": base_major,
        "majors": majors.order_by('name'),
        "universities": University.objects.all().order_by('name'),
        "colleges": colleges,
        "categories": Category.objects.all().order_by('name'),
        "selected_university": univ_id,
        "selected_college": coll_id,
        "selected_category": cat_id,
    }

    return render(request, "major/select_major.html", context)

def compare_majors(request, pk1, pk2):
    first_major = Major.objects.get(id = pk1)
    second_major = Major.objects.get(id = pk2)
    context = {
        "major1":first_major,
        "major2":second_major,
    }
    return render(request, "major/compare.html",context)

def explore_majors(request):
    majors = Major.objects.all()
    universities = University.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')

    # Standardizing on 'q' for the global search bar
    search_query = request.GET.get('q') or request.GET.get('search')

    # GET filters
    univ_id = request.GET.get('university')
    coll_id = request.GET.get('college')
    cat_id = request.GET.get('category')

    # Filter by University
    if univ_id:
        majors = majors.filter(college__university_id=univ_id)
        colleges = College.objects.filter(university_id=univ_id).order_by('name')
    else:
        colleges = College.objects.all().order_by('name')

    # Filter by College
    if coll_id:
        majors = majors.filter(college_id=coll_id)

    # Filter by Category
    if cat_id:
        majors = majors.filter(categories__id=cat_id)

    # GLOBAL SEARCH LOGIC
    if search_query:
        # This searches Major names OR the University name associated with the major
        from django.db.models import Q
        majors = majors.filter(
            Q(name__icontains=search_query) | 
            Q(college__university__name__icontains=search_query)
        )

    context = {
        "majors": majors.order_by('name'),
        "universities": universities,
        "colleges": colleges,
        "categories": categories,
        "selected_university": univ_id,
        "selected_college": coll_id,
        "selected_category": cat_id,
        "search_query": search_query,
        "show_search": True, # Keep the search bar visible
    }
    return render(request, "major/explore_majors.html", context)
