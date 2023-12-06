.PHONY: migrations-init superuser migrations migrate run requirements collectstatic freeze

migrations-init:
	python manage.py makemigrations inventory

superuser:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver 8080

requirements:
	pip install -r requirements.txt

collectstatic:
	python manage.py collectstatic

freeze:
	pip freeze > requirements. txt  
