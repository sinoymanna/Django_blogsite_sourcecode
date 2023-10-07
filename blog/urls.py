from django.urls import path
from . import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='blog-homepage'),
                           # transfers the user to home function of view page

    path('about/', views.about, name='blog-about'), 
                           # transfers the user to about function of view page
]
