from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','age','gender','occupation','email')
    list_display_links=('name','email')
admin.site.register(Profile,ProfileAdmin)
# Register your models here.
