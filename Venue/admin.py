from django.contrib import admin

# Register your models here.
#Admin-admin@123
from .models import Slide_Picture,Picture,Description

admin.register(Slide_Picture,Picture,Description)(admin.ModelAdmin)