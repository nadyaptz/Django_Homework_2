from django.shortcuts import render
from django.views.generic import TemplateView

# python manage.py runserver


def anchor(request):
    return render(request, 'anchor.html')

def main_page(request):
    title = 'Домик у Озера'
    description = 'Домик у Озера. C видом на счастье...'
    context = {
        'title': title,
        'description': description,

    }
    return render(request, 'forth_task/lakehouse.html', context)

def book(request):
    title = 'Забронировать'
    description = 'Забронировать'
    buttons = ['Домик у Озера', 'Баня', 'Лодка']
    context = {
        'title': title,
        'description': description,
        'buttons': buttons,

    }
    return render(request, 'forth_task/book.html', context)

def info(request):
    title = 'Информация о Домике у Озера'
    description = 'Позвольте вам рассказать о нашем Домике у Озера...'
    photo_summer = 'images/lakehouse_summer.jpg'
    photo_winter = 'images/lakehouse_winter.jpg'
    context = {
        'title': title,
        'description': description,
        'photo_summer': photo_summer,
        'photo_winter': photo_winter,

    }
    return render(request, 'forth_task/info.html', context)

def menu(request):
    return render(request, 'forth_task/menu.html')