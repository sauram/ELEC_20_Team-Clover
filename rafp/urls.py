from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.enter,name='home'),
    path('record/',views.list,name='record'),
    path('',views.home.as_view(),name='landing'),
    path('about/',views.about.as_view(),name='about'),
]