FROM python:latest

RUN pip3 install django

WORKDIR /app

COPY . .

EXPOSE 8000


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]