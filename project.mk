PROJECT_NAME := test_django_mongodb

define DJANGO_MONGODB_SETTINGS
DEFAULT_AUTO_FIELD = "django_mongodb.fields.MongoAutoField"
endef

export DJANGO_MONGODB_SETTINGS

django-install: django-install-default
	python -m pip install https://github.com/aclark4life/django-mongodb/archive/refs/heads/main.zip

django-mongodb-settings-default:
	echo $$DJANGO_MONGODB_SETTINGS >> backend/settings/base.py

settings: django-mongodb-settings
