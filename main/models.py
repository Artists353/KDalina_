from django.db import models

class Reviews(models.Model):
    title = models.CharField('Название', max_length=50)
    review = models.TextField('Описание отзыва')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class Review(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст отзыва")
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    