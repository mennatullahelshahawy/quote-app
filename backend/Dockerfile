FROM python:3.13.14-trixie

WORKDIR /quote-app

COPY requirements.txt .

RUN pip install requirements.txt

COPY app.py

CMD["python","app.py"]
