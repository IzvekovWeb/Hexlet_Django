make runserver:
	poetry run python manage.py runserver 7000

make gunicorn:
	export DJANGO_SETTINGS_MODULE=hello_django.settings
	GUNICORN_CMD_ARGS="--bind=127.0.0.1:5000" poetry run gunicorn hello_django.wsgi
# poetry run gunicorn hello_django.wsgi


# Получакем миграции
make migrations:
	poetry run python manage.py makemigrations

# Приеняем миграции
make migrate:
	poetry run python manage.py migrate