from django.shortcuts import render, redirect
from .models import Vacancy
from .forms import VacancyForm

def work_find(request):
    return render(request, 'work/work_find.html')

def work(request):
    return render(request, 'work/work.html')


def vacancy(request):
    error = ''
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_find')
        else:
            error == 'Вы не правильно ввели форму, попробуйте ещё раз'
    find_work_id = Vacancy.objects.order_by('-id')
    form = VacancyForm()
    data = {
        'revie': find_work_id,
        'form': form,
        'error': error,
    }
    return render(request, 'work/vacancy.html', data)