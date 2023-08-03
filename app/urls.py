from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('blog', views.blog,name='blog'),
    path('form',views.form, name='form'),
]
