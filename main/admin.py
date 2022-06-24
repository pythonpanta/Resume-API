from cProfile import Profile
from django.contrib import admin

from . models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','surname','email','age','gender','education','skills','photo','document','created_at']
