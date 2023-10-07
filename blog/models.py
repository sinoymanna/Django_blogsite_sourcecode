from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Posts (models.Model):
    titles = models.CharField(max_length=25)
    author = models.CharField(max_length=20)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=User.objects.get(username='sinoy'))

  