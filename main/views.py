from django.shortcuts import render
from . import models

def index(request):
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    context = {
        'category': category,
        'region': region
    }
    return render(request, 'front/index.html', context)

def category(request, id):
    region = models.Region.objects.all()
    category = models.Category.objects.all()
    categor = models.Category.objects.get(id=id)
    post = models.Post.objects.filter(category=categor)
    context = {
        'region': region,
        'category': category,
        'post': post
    }
    return render(request, 'front/category.html', context)

def region(request, id):
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    regi = models.Region.objects.get(id=id)
    post = models.Post.objects.filter(region=regi)
    context = {
       'category': category,
       'region': region,
        'post': post
    }
    return render(request, 'front/region.html', context)

def contact(request):
    return render(request, 'front/contact.html')

def single(request):
    return render(request, 'front/single.html')

