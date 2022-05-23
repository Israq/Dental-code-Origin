from django.shortcuts import render
from . models import Image

def photos(request):
    pics=Image.objects.all()
    return render(request,'photos.html',{"pics":pics})