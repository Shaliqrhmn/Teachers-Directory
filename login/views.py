from django.contrib import auth, messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Teacher
from .forms import TeacherForm
from django.views.generic.edit import UpdateView
from .filters import TeacherFilter


# Create your views here.


def testlogin(request):
    return render(request, 'login.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Success')
            return redirect('loginapp:home')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def homepage(request):
    return render(request, 'home.html')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'home.html'
    context_object_name = 'items'


def detail(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'detail.html', {'teacher': teacher})


def add(request):
    form = TeacherForm
    teacher = Teacher.objects.all()
    if request.method == 'POST':
        print('printing', request.POST)
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginapp:home')
    context = {'form': form}
    return render(request, 'add.html', {'form': form, 'teacher': teacher})


def uploadfile(request):
    form = TeacherForm(request.POST or None, request.FILES or None)
    return render(request, 'uploadfile.html', {'form': form})


#
# def save_data(request):
#     if request.method == "POST":
#         form = TeacherForm(request.POST)
#         if form.is_valid():
#             first_name = request.POST['id_first_name']
#             last_name = request.POST['id_last_name']
#             profile_picture = request.POST['id_profile_pic']
#             email_address = request.POST['id_email_address']
#             phone_number = request.POST['id_phone_number']
#             room_number = request.POST['id_room_number']
#             subjects_taught = request.POST['id_subjects_taught']
#             teacher = Teacher(first_name=first_name, last_name=last_name,profile_picture=profile_picture, email_address=email_address, phone_number=phone_number,room_number=room_number,subjects_taught=subjects_taught)
#             teacher.save()
#             test = Teacher.objects.values()
#             print(test)
#
#             return JsonResponse({'status': 'Save'})
#         else:
#             return JsonResponse({'status': 0})


# def update(request, id):
#     teacher = Teacher.objects.get(id=id)
#     form = TeacherForm(request.POST or None, request.FILES, instance=teacher)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'edit.html', {'form': form, 'teacher': teacher})

def edit(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(request.POST or None, instance=teacher)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'teacher': teacher})


def Filter(request, id):
    filt = Teacher.objects.get(id=id)

    myFilter = TeacherFilter(request.GET, queryset=filt)
    filt = myFilter.qs

    context = {'filt': filt, 'myFilter': myFilter}
    return render(request, 'search.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')
