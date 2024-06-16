from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories
    return render(request, 'main/index.html', context)

def categoryPage(request, slug):
    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]

    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category
    return render(request, 'main/category.html', context)

def imageDetailPage(request, slug1, slug2):
    category = Category.objects.get(slug=slug1)
    image = get_object_or_404(Image, slug=slug2)

    context = {}
    context['image'] = image
    context['category'] = category

    return render(request, 'main/image.html', context)
