from django.db import models

class Vacancy(models.Model):
    name_surname = models.CharField('ФИО', max_length=100)
    iphone = models.CharField('Номер телефона', max_length=50)
    email = models.CharField('email', max_length=100)
    year_of_birth = models.CharField('Год рождения', max_length=100)
    job_title = models.CharField('На какую вакаснию вы хотите попасть ?', max_length=100)
    experience = models.TextField('Ваш опыт работы ')
    about_myself = models.TextField('Расскажите о себе')

    def __str__(self):
        return self.name_surname
    
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работа'