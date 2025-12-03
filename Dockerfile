FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y make \
    && pip install --upgrade pip \
    && pip install pytest
CMD ["pytest"]
