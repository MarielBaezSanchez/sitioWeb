from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #('contact/')
    path('contact/', views.contact, name='contact'),
    #('about/')
    path('about/', views.about, name='about'),
    #('portafolio/')
    path('portfolio/', views.portfolio, name='portfolio'),
]
