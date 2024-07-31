PROJECT_NAME := test-django-mongodb

define DJANGO_MONGODB_SETTINGS
DEFAULT_AUTO_FIELD = 'django_mongodb.fields.MongoAutoField'
DATABASES = {
    "default": {
        "ENGINE": "django_mongodb",
        "NAME": "test",
    },
}
endef
export DJANGO_MONGODB_SETTINGS

django-settings:
	echo "$$DJANGO_MONGODB_SETTINGS" >> backend/settings/base.py

install:
	$(MAKE) pip-install-default
	python -m pip install https://github.com/aclark4life/django-mongodb/archive/refs/heads/main.zip
