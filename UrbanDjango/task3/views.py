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
    return render(request, 'third_task/lakehouse.html', context)

def book(request):
    title = 'Забронировать'
    description = 'Забронировать'
    button1 = 'Домик у Озера'
    button2 = 'Баня'
    button3 = 'Лодка'
    context = {
        'title': title,
        'description': description,
        'button1': button1,
        'button2': button2,
        'button3': button3,

    }
    return render(request, 'third_task/book.html', context)

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
    return render(request, 'third_task/info.html', context)