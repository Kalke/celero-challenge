FROM python:3.8

ADD / /app
WORKDIR /app

RUN apt-get update
RUN apt install libpq-dev python3-dev -y
RUN pip install --upgrade pip


# Python dependencies
RUN pip --no-cache-dir --trusted-host pypi.python.org install -r /app/requirements.txt


