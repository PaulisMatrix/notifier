FROM python:3.9.1-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY ./src/ /app/

ENV PORT=3001

EXPOSE 3001

CMD ["python3","app.py"]