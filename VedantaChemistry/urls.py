from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name="index"),
    path('Accounts', views.accounts , name="accounts"),
    path('Videos', views.videos , name="videos"),
    path('Gallery', views.gallery , name="gallery"),
    path('Docs', views.docs , name="docs"),
    path('Contact', views.contact , name="contact"),
    path('Logout', views.logout , name="logout"),
    path('verify/<auth_token>', views.verify , name="verify"),
]
