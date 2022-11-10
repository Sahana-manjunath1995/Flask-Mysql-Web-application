FROM python:3.8

WORKDIR /home/app
RUN apt update -y && apt install vim -y
COPY requirements.txt /home/app/
COPY  netflix1.py /home/app/
RUN pip install -r requirements.txt


