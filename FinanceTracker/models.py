from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

# Модель для типов
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель для статусов
class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель для категорий связанная с моделью типов
class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Связанная модель подкатегорий для категорий
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Модель для самих ДДС
class Tracker(models.Model):
    date = models.DateField(default=timezone.now)
    status = models.ForeignKey('Status', on_delete=models.PROTECT)
    type = models.ForeignKey('Type', on_delete=models.PROTECT, blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=False, null=False)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.PROTECT, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Сумма в рублях", blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'Дата создания: {self.date}'