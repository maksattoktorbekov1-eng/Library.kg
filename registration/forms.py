from django import forms
from captcha.fields import CaptchaField
from .models import UserAccount

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    captcha = CaptchaField(label="Введите текст с картинки")

    class Meta:
        model = UserAccount
        fields = [
            'username', 'email', 'password', 'phone', 'birth_date', 'city',
            'address', 'education', 'experience', 'skills', 'portfolio_link'
        ]
        labels = {
            'username': "Имя пользователя",
            'email': "Адрес электронной почты",
            'phone': "Телефон",
            'birth_date': "Дата рождения",
            'city': "Город",
            'address': "Адрес",
            'education': "Образование",
            'experience': "Опыт работы",
            'skills': "Навыки",
            'portfolio_link': "Ссылка на портфолио",
        }
        help_texts = {
            'username': "Не более 150 символов. Только буквы, цифры и символы @/./+/-/_",
            'password': "Введите надёжный пароль",
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    captcha = CaptchaField(label="Введите текст с картинки")