FROM python:3.10.1

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app.py /code/
CMD ["uvicorn", "app:app", "--host", "195.140.146.3", "--port", "80"]
EXPOSE 80