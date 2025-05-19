from django.urls import path
from . import views
#Мы написали, что отслеживаем адреса
#name что в конце функции аргумента path(), нужен просто для лучшего отслеживания перехода пользователя по страницам, а также для обращения сайта для перехода на другие страницы
urlpatterns = [
    path('work', views.work, name='work'),
    path('work_find', views.work_find, name='work_find'),
    path('vacancy', views.vacancy, name='vacancy')
]