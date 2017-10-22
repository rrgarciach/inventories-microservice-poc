FROM python:2.7.14-alpine3.6

WORKDIR /usr/src/app

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN export FLASK_APP=main.py

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
