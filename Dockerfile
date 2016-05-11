FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app/
WORKDIR /app
RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
WORKDIR /app/apoio/

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
