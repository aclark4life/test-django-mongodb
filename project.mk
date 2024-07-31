PROJECT_NAME := test-django-mongodb

django-settings:
	export SETTINGS=backend/settings/base.py DEV_SETTINGS=backend/settings/dev.py; $(MAKE) django-settings-default; echo "DATABASE_URL = os.environ.get('DATABASE_URL', 'django_mongodb://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(PROJECT_NAME)')" >> $(SETTINGS); echo "DEFAULT_AUTO_FIELD = 'django_mongodb.fields.MongoAutoField'" >> $(SETTINGS) 

install:
	$(MAKE) pip-install-default
	python -m pip install https://github.com/aclark4life/django-mongodb/archive/refs/heads/main.zip
