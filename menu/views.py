from django.shortcuts import render

# Create your views here.
def pie(request):
    # В классе дата мы будем содержать данные о ценнке на товары
    data = {
        
    }
    return render(request, 'menu/pie.html')

def cake(request):
    # В классе дата мы будем содержать данные о ценнке на товары
    data = {
        
    }
    return render(request, 'menu/cake.html')


def cookie(request):
    # В классе дата мы будем содержать данные о ценнке на товары
    data = {
        
    }
    return render(request, 'menu/cookie.html')

def roll(request):
    # В классе дата мы будем содержать данные о ценнке на товары
    data = {
        
    }
    return render(request, 'menu/roll.html')


def other(request):
    # В классе дата мы будем содержать данные о ценнке на товары
    data = {

    }
    return render(request, 'menu/other.html')

def brownie(request):
    # В классе дата мы будем содержать данные о ценнке на товары
    data = {

    }
    return render(request, 'menu/brownie.html')