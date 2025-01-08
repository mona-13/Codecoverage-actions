#FROM python:3.11-alpine
FROM python:3.11.0-alpine

WORKDIR /app

COPY Sourcecode/circle.py /app/circle.py


CMD ["python", "circle.py"]
