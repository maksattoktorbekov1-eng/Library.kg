from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительно", {"fields": ("phone","birth_date","city","address","education","experience","skills","portfolio_link")}),
    )
    list_display = ("username", "email", "phone", "city")