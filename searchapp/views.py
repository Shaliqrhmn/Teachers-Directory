from django.shortcuts import render
from login.models import Teacher
from django.db.models import Q


# Create your views here.
def SearchResult(request):
    teacher = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        teacher = Teacher.objects.all().filter(Q(last_name__contains=query) | Q(subject_choices__contains=query))
        return render(request, 'search.html', {'query': query, 'teacher': teacher})
