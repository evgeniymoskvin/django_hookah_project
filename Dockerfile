FROM python:3.10

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/django_hookah_project

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/django_hookah_project

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


