FROM python:3.10-alpine

#RUN apt-get -y update --fix-missing && apt-get -y install vim less supervisor build-essential git \
#    && apt-get install -y python3.10 python3.10-dev python3.10-setuptools \
#    && apt-get install -y python3.10-pip

#RUN apt-get -y update --fix-missing && apt-get -y install vim less
RUN apk update && apk add --no-cache bash vim less

RUN mkdir /pandataproc
WORKDIR /pandataproc/
ENV PYTHONPATH=$PYTHONPATH:/pandataproc
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ADD tests /pandataproc/tests
ADD bin /pandataproc/bin
ADD data /pandataproc/data
ADD panlib /pandataproc/panlib


