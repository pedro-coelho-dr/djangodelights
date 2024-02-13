FROM python:3.10-alpine3.18

WORKDIR /usr/src

COPY . .

EXPOSE 8080

RUN pip install -r requirements.txt && python manage.py makemigrations inventory && python manage.py makemigrations && python manage.py migrate

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]