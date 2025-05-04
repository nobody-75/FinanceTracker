from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from FinanceTracker.forms import TrackerForm
from FinanceTracker.models import SubCategory, Category, Type, Status, Tracker


class TrackerAdmin(admin.ModelAdmin):
    """
    Класс управления моделью Tracker в административной панели.
    """
    form = TrackerForm
    list_display = ('date', 'status', 'type', 'category',
                    'sub_category', 'amount', 'description')
    # Фильтр с указанием периода дат
    list_filter = (('date', DateFieldListFilter ),
                   'status', 'type', 'category', 'sub_category')


# Регистрация моделей в админ-панели
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Tracker, TrackerAdmin)