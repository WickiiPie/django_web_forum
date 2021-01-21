FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
