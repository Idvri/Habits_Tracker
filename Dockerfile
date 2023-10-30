FROM python:3.11

WORKDIR /code/

COPY ./requirements.txt /code/
RUN pip install -r /code/requirements.txt
RUN psql -h db -U postgres -c "CREATE DATABASE habit_database"
COPY . .
