FROM python:3.9

WORKDIR /DjangoApps

COPY . .

RUN pip install --upgrade pip

RUN pip install -r /DjangoApps/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]