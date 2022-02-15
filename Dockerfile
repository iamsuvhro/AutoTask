FROM python:3.8

WORKDIR /manage.py .

ADD AutoTask .

COPY requirements.txt .

COPY manage.py .

RUN pip3 install -r requirements.txt

CMD [ "python", "manage.py", "runserver" ,"0.0.0.0:80"]