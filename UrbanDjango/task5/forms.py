from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите ваше имя:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Введите пароль:')
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод пароля:')
    age = forms.IntegerField(max_value=99, min_value=0, label='Введите ваш возраст:')