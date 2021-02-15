FROM python:3.8.3 AS build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /app
WORKDIR /app

# Copy Python files
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txts

EXPOSE 8000