from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
  url(r'^$', views.index),  #this matches the "/" pathway
]
