# docker-django-ca
Django CA Running in a Docker Container

Please ensure you read the docs for the django-ca project:

https://github.com/mathiasertl/django-ca

http://django-ca.readthedocs.io/

> This is in no way a production ready container'd solution!
> It is intended purely for the purposes of testing and PoC of Django CA.
> It is configured to use sqlite (non-persistent) and, by default, all
> state (certs, CA's...) will be lost on container destruction.

## Usage

I'm making the assumption that you have Docker (Toolbox) running and the
appropriate environment variables set.

To start the container:
```
docker-compose up
```

Create a super user:
```
docker-compose exec django-ca migrate.py createsuperuser
```
and complete the questions you are asked. Now login to the admin interface on:
`http://<<docker ip>>:8000/admin`.

Create a CA:
```
docker-compose exec django-ca migrate.py init_ca TestCA /C=AT/L=Vienna/O=Example/OU=ExampleUnit/CN=ca.example.com
```
