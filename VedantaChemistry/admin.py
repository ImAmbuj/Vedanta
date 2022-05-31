from django.contrib import admin
from .models import Profile,Gallery,Video, Document,Notification,Message

# Register your models here.

admin.site.register(Profile)
admin.site.register(Gallery)
admin.site.register(Video)
admin.site.register(Notification)
admin.site.register(Document)
admin.site.register(Message)