FROM python:3.10-alpine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /source_code ./source_code
COPY /static ./static
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "source_code.infrastructure.app:app"]