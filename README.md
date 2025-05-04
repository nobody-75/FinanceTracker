

🚀 Django Project README
Добро пожаловать в проект на фреймворке Django! Этот документ поможет быстро установить и запустить ваше приложение.

⚙️ Настройка окружения
Шаг 1: Клонирование репозитория

git clone https://github.com/yourusername/yourproject.git
cd yourproject
Шаг 2: Установка виртуального окружения
Используйте virtualenv, чтобы создать изолированное окружение для проекта:


python -m venv env
source env/bin/activate # Linux/MacOS
.\env\Scripts\activate.bat # Windows
pip install -r requirements.txt
👷 Применение миграций
Создаем и применяем миграции для обновления структуры базы данных:


python manage.py makemigrations
python manage.py migrate
🛡️ Создание суперпользователя (опционально)
Чтобы получить доступ к административной панели Django, создайте суперпользователя командой:


python manage.py createsuperuser
Следуя подсказкам, введите имя пользователя, электронную почту и пароль.

🚀 Локальная разработка без настройки БД
По умолчанию Django создает встроенную базу данных SQLite. Это позволяет начать разработку сразу же без настройки внешних СУБД.

💥 Запуск сервера разработки
Запустите сервер локально:


python manage.py runserver
Теперь ваш сайт доступен по адресу http://localhost:8000/.

