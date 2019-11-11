from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('thanks/', views.thanks),
    path('another/', views.another),
]
