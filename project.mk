# Custom Makefile
# Add your custom makefile commands here
#
PROJECT_NAME := test-django-mongodb
MONGODB_MIGRATIONS_DIR := backend/migrations

# --- backend/apps.py ---
define DJANGO_MONGODB_APPS
from django.contrib.admin.apps import AdminConfig
from django.contrib.auth.apps import AuthConfig
from django.contrib.contenttypes.apps import ContentTypesConfig
from allauth.account.apps import AccountConfig


class MongoAdminConfig(AdminConfig):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"


class MongoAuthConfig(AuthConfig):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"


class MongoContentTypesConfig(ContentTypesConfig):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"


class MongoAccountConfig(AccountConfig):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"
endef
# ------------------------ 

# --- backend/settings/base.py ---
define DJANGO_MONGODB_SETTINGS
DATABASES = {
    'default': {
	# 'ENGINE': 'django_mongodb',
	'ENGINE': 'django_mongo',
	'NAME': 'test',
    }
}
DJANGO_COMPAT_CHECK_DISABLED = True
DEFAULT_AUTO_FIELD = "django_mongodb.fields.ObjectIdAutoField"
MIGRATION_MODULES = {
    "account": "backend.migrations.account",
    "admin": "backend.migrations.admin",
    "auth": "backend.migrations.auth",
    "contenttypes": "backend.migrations.contenttypes",
}
INSTALLED_APPS.remove("allauth.account")
INSTALLED_APPS.remove("django.contrib.admin")
INSTALLED_APPS.remove("django.contrib.auth")
INSTALLED_APPS.remove("django.contrib.contenttypes")
INSTALLED_APPS.append("backend.apps.MongoAccountConfig")
INSTALLED_APPS.append("backend.apps.MongoAdminConfig")
INSTALLED_APPS.append("backend.apps.MongoAuthConfig")
INSTALLED_APPS.append("backend.apps.MongoContentTypesConfig")
endef
# ------------------------ 

# --- Exported Variables ---
export DJANGO_MONGODB_APPS
export DJANGO_MONGODB_SETTINGS
# ------------------------ 

# --- Custom Makefile Commands ---
db-init:
	mongosh --eval "db.dropDatabase()"

django-admin-custom: django-admin-custom-default
	@echo "$$DJANGO_MONGODB_APPS" >> $(DJANGO_ADMIN_CUSTOM_APPS_FILE)

django-install-minimal: django-install-minimal-default
	pip install -e git+ssh://git@github.com/aclark4life/django-mongodb.git#egg=django-mongodb

django-install: django-install-default
	pip install -e git+ssh://git@github.com/aclark4life/django-mongodb.git#egg=django-mongodb

django-install-wagtail: django-install-wagtail-default
	pip install -e git+ssh://git@github.com/aclark4life/django-mongodb.git#egg=django-mongodb

django-migrate:
	-mkdir backend/migrations
	python manage.py makemigrations account auth admin contenttypes
	-$(GIT_ADD) $(MONGODB_MIGRATIONS_DIR)/*.py
	$(MAKE) django-migrate-default

django-settings-minimal: django-settings-minimal-default
	$(ADD_DIR) $(MONGODB_MIGRATIONS_DIR)
	@echo "$$DJANGO_MONGODB_SETTINGS" >> $(DJANGO_SETTINGS_BASE_FILE)

django-settings-base: django-settings-base-default
	$(ADD_DIR) $(MONGODB_MIGRATIONS_DIR)
	@echo "$$DJANGO_MONGODB_SETTINGS" >> $(DJANGO_SETTINGS_BASE_FILE)

install: 
	$(MAKE) npm-install django-install
# ------------------------ 
