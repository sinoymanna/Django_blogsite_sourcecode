
from django.shortcuts import render
from .models import Posts

def  home(request):#-->homepage of the site

	context={'posts':Posts.objects.all()}

	return render(request,'blog/home.html',context)

def about(request):#-->about section for The site
	return  render(request,'blog/about.html', {'title':'About-Gurr'})



