FROM python:3.10

WORKDIR /opt/fintech

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./fintech/ ./fintech/
COPY ./manage.py ./manage.py
COPY ./templates ./templates
COPY ./static ./static

COPY ./authentication/ ./authentication/
COPY ./finance/ ./finance/

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
