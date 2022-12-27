https://github.com/KonstantinKlimenko/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg

### yamdb_final

Проект YaMDb собирает отзывы пользователей на произведения по категориям: «Книги», «Фильмы», «Музыка». Произведению может быть присвоен жанр из списка предустановленных. Пользователи оставляют к произведениям отзывы, оставляют комментарии к отзывам и ставят произведению оценку, из пользовательских оценок формируется рейтинг.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:KonstantinKlimenko/yamdb_final.git
```

```
cd yamdb_final
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/Scripts/activate
```

Для запуска контейнеров:
```
docker-compose up -d
```
```
docker-compose web python manage.py migrate --noinput
```
```
docker-compose web python manage.py collectstatic
```
```
docker-compose web python manage.py createsuperuser
```
## Создать и запонлить файл .env:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<имя пользователя>
POSTGRES_PASSWORD=<пароль>
DB_HOST=db
DB_PORT=5432
```
## Основные технологии: 
### python 3.8
### django
### drf
### posgresql
### docker