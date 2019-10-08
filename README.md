Установка проекта.
Нужно склонировать проект с гитхаба.
    -  если гита на компе нет -> https://devpractice.ru/git-for-beginners-part-2-install-git/
Дальше вот это в консоли
git clone https://gitlab.com/antonmazun/wa_19_08.git
В папке с проектом нужно создать виртуальное окружение
"python -m venv env" (если система MACOs , эта команда будет такой -  "python3 -m venv env")
Следующий шаг : активировато env. На windows  - "cd env/Scripts " и запустить скрипит  "activate". На MACOS или Unix system  - source env/bin/activate.
В папке где находиться  "req.txt" нужно запустить  pip install -r req.txt для установки всех зависимостей в проекте
Дальше 
python manage.py migrate apply all migrations for django :)
python manage.py makemigrations  - create file of migrations
python manage.py migrate  - apply your changes in models.py to DB
python manage.py createsuperuser  - create admin user.
python manage.py runserver 9000 (optional you can changes port  , default port - 8000)
That`s all.