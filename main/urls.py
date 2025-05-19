from django.urls import path
from . import views
#Мы написали, что отслеживаем адреса
#name что в конце функции аргумента path(), нужен просто для лучшего отслеживания перехода пользователя по страницам, а также для обращения сайта для перехода на другие страницы
urlpatterns = [
    path('', views.index, name='home'),
    path('menu', views.menu, name='menu'),
    path('about', views.about, name='about'),
    path('review', views.review, name='review'),
    path('leave_feedback', views.leave_feedback, name='leave_feedback'),
    path('work', views.work, name='work'),
    path('reviews/', views.review_list, name='review_list'),
]