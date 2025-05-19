from .models import Vacancy
from django.forms import ModelForm, TextInput, Textarea

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ["name_surname", "iphone", "email", "year_of_birth", "job_title", "experience", "about_myself"]
        widgets = {
        'name_surname': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ФИО",
        }),
        'iphone': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Номер телефона",
        }),
        'email': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Email",
        }),
        'year_of_birth': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Дата рождения",
        }),
        'job_title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "На какую вакаснию вы хотите попасть ?",
        }),
        'experience': Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Ваш опыт работы",
        }),
        'about_myself': Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Расскажите о себе",
        }),
    }