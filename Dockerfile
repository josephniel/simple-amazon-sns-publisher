FROM python:3.6

ENV ENVIRONMENT_CONFIG_FILE /srv/.env

WORKDIR /srv

COPY ./app ./app
COPY ./setup.py ./setup.py
COPY ./app.py ./app.py
COPY ./.env ./.env

RUN pip3 install -e .

CMD python3 app.py
