from .models import Reviews, Review
from django.forms import ModelForm, TextInput, Textarea

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ["title", "review"]
        widgets = {
        'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите вкратце оценку о заведении",
        }),
        'review': Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Введите вашу аргументацию оценки",
        }),
    }
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'parent']
