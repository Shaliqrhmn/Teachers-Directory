from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    email_address = models.EmailField(max_length=250, unique=True)
    phone_number = models.IntegerField()
    room_number = models.CharField(max_length=250)
    subject_choices = (
        (1, 'Physics'),
        (2, 'Computer Science'),
        (3, 'History'),
        (4, 'Mathematics'),
        (5, 'Biology'),
        (6, 'Chemistry'),
        (7, 'English'),
        (8, 'Arabic'),
        (9, 'Geography')

    )
    subjects_taught = MultiSelectField(choices=subject_choices, max_choices=5)

    def __str__(self):
        return self.first_name
