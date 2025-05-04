Данный проект выполнен в качестве тестового задания. Чтобы протестировать его следуйте инструкции ниже она должна Вам помочь в запуске.



# 🚀 Django Project README

Добро пожаловать в проект на фреймворке Django! Этот документ поможет быстро установить и запустить ваше приложение.

## ⚙️ Настройка окружения

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/nobody-75/FinanceTracker.git
cd FinanceTracker
```
### Шаг 1: Виртуальное окружение 
```bash
python -m venv env
source env/bin/activate   # Linux/MacOS
.\env\Scripts\activate.bat # Windows
```
##### Установка django 
```bash
pip install django
```

### Шаг 2: Применение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### Шаг 3: Создание супер пользователя 
```bash
python manage.py createsuperuser
```

### Шаг 4: Запуск проекта
```bash
python manage.py runserver
```
