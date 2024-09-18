ARG API_IMAGE
ARG API_EXTERNAL_PORT

FROM ${API_IMAGE}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
VOLUME /backend
WORKDIR /backend
COPY . .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# EXPOSE ${API_EXTERNAL_PORT}
CMD ["python", "app.py"]
