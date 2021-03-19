FROM python:3.8.3-alpine
ENV PYTHONBUFFERED=1
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
#COPY ./config/requirements.txt ./requirements.txt
RUN pip install -r ./config/requirements.txt

#COPY ./config/entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["sh", "./config/entrypoint.sh"]