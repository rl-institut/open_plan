FROM python:3.8-alpine

ENV APP_ROOT /src
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && apk add --no-cache mariadb-dev \
    && pip install --no-cache-dir -r ${CONFIG_ROOT}/requirements.txt \
    && apk del .build-deps

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD . ${APP_ROOT}

RUN adduser appUser -D -h ${APP_ROOT} -s /bin/sh \
    && chown -R appUser ${APP_ROOT}
USER appUser