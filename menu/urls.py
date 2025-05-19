from django.urls import path
from . import views
urlpatterns = [
    path('pie', views.pie, name='pie'), 
    path('cake', views.cake, name='cake'),
    path('brownie', views.brownie, name='brownie'),
    path('cookie', views.cookie, name='cookie'),
    path('roll', views.roll, name='roll'),
    path('tubes', views.other, name='other'),
]