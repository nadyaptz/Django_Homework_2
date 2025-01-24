from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm

users = [{'username': 'vasya', 'password': 'qw1qw1qw1', 'age': 21},
         {'username': 'petya', 'password': 'petya12345', 'age': 24},
         {'username': 'kolya', 'password': 'kolya12345', 'age': 40}]


# Create your views here.
def sign_up_by_html(request):
    if request.method == 'POST':
        # получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        age = request.POST.get('age')

        info = {'username': username,
                'age': age,

                }

        user_exists = any(user['username'] == username for user in users)

        if user_exists:
            info['error'] = "Такой пользователь уже существует"
        elif password != password_repeat:
            info['error'] = "Пароли не совпадают"
        elif int(age) < 18:
            info['error'] = "Вам нет 18 лет"
        else:
            # Если ошибок нет, добавляем пользователя в список
            users.append({'username': username, 'password': password, 'age': int(age)})
            return HttpResponse(f"Приветствуем, {username}!")
        return render(request, 'fifth_task/registration_page.html', info)
    # если это метод GET
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            age = form.cleaned_data['age']

            info = {'form': form
                    }
            user_exists = any(user['username'] == username for user in users)

            if user_exists:
                info['error'] = "Такой пользователь уже существует"
            elif password != password_repeat:
                info['error'] = "Пароли не совпадают"
            elif int(age) < 18:
                info['error'] = "Вам нет 18 лет"
            else:
                # Если ошибок нет, добавляем пользователя в список
                users.append({'username': username, 'password': password, 'age': int(age)})
                return HttpResponse(f"Приветствуем, {username}!")
            return render(request, 'fifth_task/registration_page_django.html', info)

    else:
        form = UserRegistrationForm()
    return render(request, 'fifth_task/registration_page_django.html', {'form': form})