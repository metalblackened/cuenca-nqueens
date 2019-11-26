FROM python:3.6.0-alpine
RUN apk update
RUN apk add postgresql-dev make automake gcc g++ subversion python3-dev
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# copy project
COPY . /usr/src/app/ 
