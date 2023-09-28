FROM python:3.11.2

WORKDIR /src

COPY  requiremets.txt /src/


RUN pip install -U pip
RUN pip install -r requiremets.txt

COPY  . /src/


CMD [ "gunicorm", 'Downloader.wsgi', ":8000" ]