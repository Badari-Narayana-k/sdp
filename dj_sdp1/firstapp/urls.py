from django.urls import path
from . import views

#URLConfiguration
urlpatterns = [
    path('', views.coverpage),
    path('second/', views.second),
    path('index/', views.index),
    path('album/', views.album),
    path('welcome/',views.welcome),

]