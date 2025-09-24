from django.shortcuts import render
from .models import SuccessStory

def home(request):
  stories = SuccessStory.objects.all()
  return render(request, 'core/home.html', {'stories': stories})

def programs(request):
  return render(request, 'core/programs.html')

def yisa(request):
  return render(request, 'core/yisa.html')

def products(request):
  return render(request, 'core/products.html')

def aquafedha(request):
  return render(request, 'core/aquafedha.html')

def fishfeeds(request):
  return render(request, 'core/fishfeeds.html')

def hatchery(request):
  return render(request, 'core/hatchery.html')

def fishdeli(request):
  return render(request, 'core/fishdeli.html')

def fishfarmilia(request):
  return render(request, 'core/fishfarmilia.html')

def farmers(request):
  return render(request, 'core/farmers.html')

def about(request):
  return render(request, 'core/about.html')

def blog(request):
  return render(request, 'core/blog.html')

def contact(request):
  return render(request, 'core/contact.html')
