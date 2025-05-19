from django.contrib import admin
from .models import Review, Reviews  # Убедись, что импортируешь нужную модель

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at", "parent")  # исправленный список полей
    list_filter = ("created_at", "parent")  # фильтр по дате и родительскому отзыву
    search_fields = ("title", "content")  # поиск по заголовку и тексту

admin.site.register(Review, ReviewAdmin)  # Регистрируем модель правильно
admin.site.register(Reviews)

