## STARTUP

Установка поетри, если нет(вместо пип)

`pip install poetry`

Клоним проект с гита

`git clone git@github.com:burn-in-soul/sellout.git`

Устанавливаем зависимости

`poetry install`

Создаем бд, у меня постгрес

```bash
sudo psql -U postgres

CREATE ROLE sellout_user WITH PASSWORD 'sellout_password';

ALTER ROLE sellout_user WITH LOGIN;

CREATE DATABASE sellout_db OWNER sellout_user;
```

Создаем файлик `/src/sellout/local_settings.py` для конфига

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sellout_db',
        'USER': 'sellout_user',
        'PASSWORD': 'sellout_password',
        'HOST': 'localhost',
    }
}

ALLOWED_HOSTS = ['127.0.0.1']
```

Активируем среду poetry (аналог `source venv/bin/activate`)

`poetry shell`

Мигрируем базу данных (создаем таблички)

`python manage migrate`

Создаем директорию `/src/media/posters/` для загрузки изображений через бд

Создаем пользователя для входа в админку

`python manage.py createsuperuser`

и вводим все нужные данные

Запускаем сервак

`python manage.py runserver`

По ссылке http://127.0.0.1:8000/ будет главная страница

По ссылке http://127.0.0.1:8000/admin/ будет админка для добавления мероприятий и тд

Для правок нужно создать свою ветку

`git checkout -b <название>`

При первом пуше нужно указать

`git push --set-upstream origin <название ветки>`

Она создастся на гите. Для добавления в мастер нужно создавать Pull Request на гитхабе из твоей ветки в мастер.

### В МАСТЕР ВЕТКУ НИЧЕГО НЕ ПУШИТЬ

