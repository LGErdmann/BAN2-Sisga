ARG API_IMAGE

FROM ${API_IMAGE}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
VOLUME /api
WORKDIR /api
COPY . .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
