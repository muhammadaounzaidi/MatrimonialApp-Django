from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs=FileSystemStorage(location=settings.MEDIA_ROOT)
# Create your models here.
class Profile(models.Model):
    GENDER_COICES=[
        ('M','Male'),
        ('F','Female'),
    ]
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(null=True, blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=GENDER_COICES)
    occupation=models.CharField(max_length=100,null=True, blank=True)
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    email=models.EmailField(max_length=254, unique=True)