FROM python:3.11-alpine

WORKDIR /app

COPY Sourcecode/addition.py /app/addition.py


CMD ["python", "addition.py"]
