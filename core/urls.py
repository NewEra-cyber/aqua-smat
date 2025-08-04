from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('programs/', views.programs, name='programs'),
  path('yisa/', views.yisa, name='yisa'),
  path('products/', views.products, name='products'),
  path('aquafedha/', views.aquafedha, name='aquafedha'),
  path('fishfeeds/', views.fishfeeds, name='fishfeeds'),
  path('hatchery/', views.hatchery, name='hatchery'),
  path('fishmarket/', views.fishdeli, name='fishdeli'),
  path('fishfarmilia/', views.fishfarmilia, name='fishfarmilia'),
  path('farmers/', views.farmers, name='farmers'),
  path('about/', views.about, name='about'),
  path('blog/', views.blog, name='blog'),
  path('contact/', views.contact, name='contact'),
]
