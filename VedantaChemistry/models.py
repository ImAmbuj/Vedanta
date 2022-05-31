from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STANDARD_CHOICES = (('11th', '11th'),('12th','12th'))

class Profile(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     contact = models.IntegerField(blank=False, null=False)
     standard = models.CharField(choices=STANDARD_CHOICES, max_length=50)
     verified = models.BooleanField(default=False)
     fee = models.BooleanField(default=False) 
     auth_token = models.CharField(max_length=100, null=True)

     def __str__(self):
      return str(self.user)


class Notification(models.Model):
     notification = models.CharField(max_length=500)

     def __str__(self):
      return str(self.notification)

class Gallery(models.Model):
     
     file = models.FileField(upload_to='Gallery')
     caption = models.TextField(max_length=50, blank=True, null=True)
     featured = models.BooleanField(default=False)
     def __str__(self):
      return str(self.caption)

class Document(models.Model):
     
     file = models.FileField(upload_to='Docs')
     caption = models.TextField(max_length=50, blank=True, null=True)

     def __str__(self):
      return str(self.caption)

class Video(models.Model):
     
     video = models.FileField(upload_to='Videos')
     title = models.TextField(max_length=1000)
     standard = models.CharField(choices=STANDARD_CHOICES, max_length=50)
     thumbnail = models.ImageField(upload_to="video_thumbs",default="default.jpg")

     def __str__(self):
      return str(self.standard + self.title)

class Message(models.Model):
   
    full_name = models.CharField(max_length=200)   
    email = models.CharField(max_length=30)   
    phone =  models.IntegerField()
    text = models.TextField(max_length=1000)   

    def __str__(self):
        return str(self.full_name) 
      