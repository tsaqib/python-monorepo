FROM python:3.9-slim as py39slimbase
RUN apt-get update -y && apt-get install nano htop gcc make -y

FROM py39slimbase
WORKDIR /src
COPY ./common ./common
# Not copying source since it takes time, rather a volume would be mounted

COPY ./worker1/requirements.txt ./worker1/requirements.txt 
RUN pip install -r /src/worker1/requirements.txt

ENTRYPOINT celery -A worker1.main worker -B -E -l INFO