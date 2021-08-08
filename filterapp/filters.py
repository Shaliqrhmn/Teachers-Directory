import django_filters

from login .models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        exclude = ['profile_picture']
        fields = {
            'last_name': ['icontains'],
            'subjects_taught': ['icontains'],
        }
