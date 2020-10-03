from django.shortcuts import render
from .models import Slide_Picture,Picture,Description
# Create your views here.
def Index(request):
    context={
        'Slide_Picture':Slide_Picture.objects.all()[0],
         'Picture':Picture.objects.all()[0],
         'Description':Description.objects.all()[0],   

    }
    return render(request,'Venue/index.html',context)
