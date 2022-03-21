FROM python:3.10.2

RUN pip3 install django

VOLUME /app

WORKDIR /app

EXPOSE 8888

# CMD sh -c "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:80"

RUN pip3 install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8888", "neo.wsgi:application"]

RUN pip3 install mysqlclient

RUN pip3 install djangorestframework

