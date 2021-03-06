FROM python:3

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY app.py /
COPY swagger.yaml /
COPY genetic.py /

CMD /app.py