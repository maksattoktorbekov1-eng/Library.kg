from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    birth_date = models.DateField("Дата рождения", blank=True, null=True)
    city = models.CharField("Город", max_length=100, blank=True, null=True)
    address = models.CharField("Адрес", max_length=255, blank=True, null=True)
    education = models.CharField("Образование", max_length=255, blank=True, null=True)
    experience = models.TextField("Опыт работы", blank=True, null=True)
    skills = models.TextField("Навыки", blank=True, null=True)
    portfolio_link = models.URLField("Ссылка на портфолио", blank=True, null=True)

    def __str__(self):
        return self.username