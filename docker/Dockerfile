FROM python:3.9.15-alpine
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY /source_code /source_code
WORKDIR /source_code
ENTRYPOINT ["./gunicorn.sh"]