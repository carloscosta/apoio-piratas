FROM golang:alpine

ADD . /app/
WORKDIR /app/

RUN apk add --update --no-cache --virtual .build-deps make
RUN make build
RUN apk del .build-deps

CMD ["./apoio.server"]

EXPOSE 8991
