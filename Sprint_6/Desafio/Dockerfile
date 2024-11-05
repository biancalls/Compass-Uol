FROM python:3.12-slim

WORKDIR /app

VOLUME ["/app/volume"]

COPY lib.txt /app/lib.txt
COPY desafio.py /app/volume/desafio.py
COPY series.csv /app/volume/series.csv
COPY movies.csv /app/volume/movies.csv

RUN pip install --no-cache-dir -r /app/lib.txt

CMD ["python","/app/volume/desafio.py"]