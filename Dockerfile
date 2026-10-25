

FROM python:3.14.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "uvicorn","app.orm:app","--host","0.0.0.0","--port","8000" ]

## commands docker build -t fastapi .
#docker build -t fastapi .
#docker image ls
