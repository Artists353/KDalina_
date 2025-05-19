from django.shortcuts import render, redirect
from .models import Reviews, Review
from .forms import ReviewsForm, ReviewForm
# Create your views here.
#МЫ будем показывать html файлы при помощи этого файла и узнавать куда пользователь идёт
# index и about это главные страницы сайта
def index(request):
    return render(request, 'main/index.html')

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews.html', {'reviews': reviews})

def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("review_list")
    return redirect("review_list")

def menu(request):
    return render(request, 'menu/menu.html')

def about(request):
    return render(request, 'main/about.html')


def review(request):
    reviews = Reviews.objects.order_by('-id')
    form = ReviewsForm()
    data = {
        'revie': reviews,
        'form': form,
    }
    return render(request, 'main/review.html', data)

def leave_feedback(request):
    error = ''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
        else:
            error == 'Вы не правильно ввели форму, попробуйте ещё раз'
    reviews = Reviews.objects.order_by('-id')
    form = ReviewsForm()
    data = {
        'revie': reviews,
        'form': form,
        'error': error,
    }
    return render(request, 'main/leave_feedback.html', data)


def work(request):
    return render(request, 'main/work.html')


