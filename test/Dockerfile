FROM python:2

RUN apt-get update -y && apt-get install -y nodejs sqlite3
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib mock pytest

COPY . /rpi-web-temperature-monitor-with-google-drive-upload
RUN cd /rpi-web-temperature-monitor-with-google-drive-upload/test && ./run.sh