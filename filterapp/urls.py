
from django.urls import path, include
from . import views

app_name = 'filterapp'
urlpatterns = [
    path('', views.SnippetListView.as_view(), name='list'),
]
