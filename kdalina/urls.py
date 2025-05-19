
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#Мы написали, что отслеживаем адреса

urlpatterns = [
    path('admin/', admin.site.urls),
    #Когда мы будем переходить на главную страницу будет октивироваться этот код.
    #Будет выполняться ниже меня отслеживание файлов
    #НИже код просто перенаправляет все действия в приложение "main" в файл urls
    path('', include('main.urls')), 
    path('menu/', include('menu.urls')), 
    path('work/', include('work.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
