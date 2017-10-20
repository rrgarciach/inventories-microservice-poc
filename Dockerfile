FROM python:2.7.14-alpine3.6

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN export FLASK_APP=main.py


CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
