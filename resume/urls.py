from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from myresume.resume import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

]

urlpatterns += staticfiles_urlpatterns()