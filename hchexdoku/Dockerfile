# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12.7-alpine3.20 AS builder
EXPOSE 8000
WORKDIR /hchexdoku 
COPY requirements.txt /hchexdoku/requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /hchexdoku