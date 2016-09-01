
FROM python:latest

MAINTAINER Tim Birkett

RUN rm -f /bin/sh && ln -s /bin/bash /bin/sh

# Install dependencies
RUN apt-get update && apt-get -y install gcc git python3-dev libffi-dev libssl-dev virtualenv

# Install django-ca
RUN cd /usr/local/share &&\
    git clone https://github.com/mathiasertl/django-ca.git &&\
    cd django-ca &&\
    virtualenv -p /usr/bin/python3 . &&\
    source bin/activate &&\
    pip install -U pip setuptools &&\
    pip install -r requirements.txt

WORKDIR '/usr/local/share/django-ca'

ADD localsettings.py ca/ca/localsettings.py

RUN source bin/activate &&\
    python ca/manage.py migrate &&\
    python ca/manage.py collectstatic --noinput

ADD manage.py /usr/local/bin/manage.py
RUN chmod 0755 /usr/local/bin/manage.py

ADD run-ca.sh bin/run-ca.sh
RUN chmod 0755 bin/run-ca.sh

# Run server in dev mode
EXPOSE 8000
ENTRYPOINT ["bin/run-ca.sh"]
