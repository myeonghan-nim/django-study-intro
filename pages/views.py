from django.shortcuts import render

import datetime
import random

# Create your views here.
# html must exist in app/templates folder.
def index(request):
    return render(request, 'index.html')


def dinner(request):

    menu = ['korean', 'chinese', 'western']
    pick = random.choice(menu)

    # for hand over datas in django, use context(dict).
    context = {
        'pick': pick,
        'menu': menu,
    }

    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'image.html')


def greeting(request, name):

    context = {
        'name': name,
    }

    return render(request, 'greeting.html', context)


def cube(request, num):

    cubic = num ** 3

    context = {
        'num': num,
        'cubic': cubic,
    }

    return render(request, 'cube.html', context)


def mul(request, num1, num2):

    context = {
        'mul': num1 * num2,
        'num1': num1,
        'num2': num2,
    }

    return render(request, 'mul.html', context)


def dtl(request):

    menus = ['korean', 'western', 'chinese', 'jap']
    sentences = 'Life is short, you need python'

    messages = {
        'apple': 'red',
        'banana': 'yellow',
        'cat': 'cute'
    }

    now = datetime.datetime.now()
    empty = []

    context = {
        'menus': menus,
        'sentences': sentences,
        'messages': messages,
        'now': now,
        'empty': empty,
    }

    return render(request, 'dtl.html', context)


def christmas(request):

    now = datetime.datetime.now()

    if now.month == 12 and now.day == 25:
        result = True
    else:
        result = False

    context = {
        'result': result
    }

    return render(request, 'christmas.html', context)
    