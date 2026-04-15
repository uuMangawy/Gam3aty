from django.shortcuts import render
from .models import University
from users.models import FavoriteUniversity
def universities(request):
    query = request.GET.get('q')
    universities = University.objects.all()
    
    if query:
        universities = universities.filter(name__icontains=query)
        
    return render(request, 'university/universities.html', {
        'universities': universities,
        'search_query': query,
        'show_search': True
    })

def university(request, pk):
    university = University.objects.get(id = pk)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = FavoriteUniversity.objects.filter(
        user=request.user,
        university=university
        ).exists()
    context = {"university":university,"is_favorite":is_favorite}
    return render(request, 'university/university.html', context)
