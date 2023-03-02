FROM python:3.9.15-alpine
COPY ./ ./
RUN pip3 install -r requirements.txt
RUN chmod +x gunicorn.sh
ENTRYPOINT ["./gunicorn.sh"]