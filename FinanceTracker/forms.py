from django import forms
from .models import Tracker


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = '__all__'

    def clean(self):
        """
        Метод для дополнительной проверки полей перед сохранением экземпляра модели.
        Проверяет валидность связи между категориями и подкатегориями, проверяет допустимость суммы и типы операций.
        """
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('sub_category')
        type = cleaned_data.get('type')
        amount = cleaned_data.get('amount')


        # Проверяем, относится ли подкатегория к категории
        if subcategory and subcategory.category != category:
            raise forms.ValidationError(f'Подкатегория "{subcategory}" не принадлежит категории "{category}".')

        # Проверяем, относится ли тип к категории
        if category and category.type != type:
            raise forms.ValidationError(f'Категория "{category}" не является типом "{type}".')

        # Проверяем, что сумма не меньше нуля и является обязательным к заполнению
        if amount is not None and amount < 0:
            raise forms.ValidationError('Сумма не может быть меньше нуля.')


        return cleaned_data