"""
URL configuration for django_first_try project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('register/', user_views.register,name='register'),
    path('', include('blog.urls'),name='blog-home'), #homepage


    #    '''path('about/', include('blog.urls')),'''

            #not required as the homepage transfers the user to blog.urls anyway where about/ 
            # is located

            # Django checks for path to homepage first and then sends the user to url of
              # assocoiated app from homepage if the url is found 
                

]
