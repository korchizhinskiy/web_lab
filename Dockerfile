FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update -y
RUN apt-get install gcc musl-dev bash zlib1g-dev libjpeg-dev netcat -y
RUN apt-get autoremove -y && apt-get clean

ADD ./ /opt
WORKDIR /opt
RUN pip install -r requirements.txt

VOLUME /opt/media
VOLUME /opt/static_files

EXPOSE 8000
