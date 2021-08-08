from django.urls import path
from . import views
app_name = 'loginapp'

urlpatterns = [
    path('', views.adminlogin, name='login'),
    path('home/', views.TeacherListView.as_view(), name='home'),
    path('add/', views.add, name='add'),
    # path('save/', views.save_data, name='save'),
    path('uploadfile/', views.uploadfile, name='uploadfile'),
    path('detail/<int:teacher_id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.edit, name='edit'),
    path('filter/<int:id>/', views.Filter, name='filter'),
    path('logout', views.logout, name='logout'),
]
