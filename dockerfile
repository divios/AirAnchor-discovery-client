FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 8000
CMD ["gunicorn", "app.main:app"]