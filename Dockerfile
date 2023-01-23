FROM python:3.10
COPY . /app
WORKDIR /app
RUN [ "pip", "install", "-r", "/app/requirements.txt" ]
ENTRYPOINT [ "python", "-u", "/app/app.py" ]