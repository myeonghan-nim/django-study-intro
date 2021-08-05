import datetime
import random

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def dinner(request):
    menu = ['korean', 'chinese', 'western']
    context = {'pick': random.choice(menu), 'menu': menu, }
    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'image.html')


def greeting(request, name):
    context = {'name': name, }
    return render(request, 'greeting.html', context)


def cube(request, num):
    context = {'num': num, 'cubic': num ** 3, }
    return render(request, 'cube.html', context)


def multiple(request, num1, num2):
    context = {'multiple': num1 * num2, 'num1': num1, 'num2': num2, }
    return render(request, 'multiple.html', context)


def flow(request):
    context = {'menu': ['korean', 'western', 'chinese'], 'empty': [], }
    return render(request, 'flow.html', context)


def christmas(request):
    now = datetime.datetime.now()
    context = {
        'result': True if now.month == 12 and now.day == 25 else False,
    }
    return render(request, 'christmas.html', context)
