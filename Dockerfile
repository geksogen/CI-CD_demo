FROM python:3.10.10

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app.py /code/
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
EXPOSE 8080