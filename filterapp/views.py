from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from login.models import Teacher
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import TeacherFilter


class SnippetListView(ListView):
    model = Teacher
    template_name = 'filter_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TeacherFilter(self.request.GET, queryset=self.get_queryset())
        return context
