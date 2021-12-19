FROM python:3.10

WORKDIR /opt/fintech

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./authentication/ ./authentication/
COPY ./finance/ ./finance/
COPY ./fintech/ ./fintech/
COPY ./recommendations/ ./recommendations/
COPY ./manage.py ./manage.py
COPY ./templates ./templates
COPY ./static ./static
