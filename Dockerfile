FROM --platform=linux/amd64 python:3.11.3-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat
RUN pip install --upgrade pip

ENV TZ=Europe/Moscow
RUN apt install tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY . .

CMD sh entrypoint.sh