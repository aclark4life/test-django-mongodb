PROJECT_NAME := test_django_mongodb

django-install: django-install-default
	python -m pip install https://github.com/aclark4life/django-mongodb/archive/refs/heads/main.zip
