from django.urls import path

#from myresume.resume import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]