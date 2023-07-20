FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

ARG api_id

ARG api_hash

ARG session_name

ENV API_ID=$api_id

ENV API_HASH=$api_hash

ENV SESSION_NAME=$session_name

CMD ["python", "app.py"]