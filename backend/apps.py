from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = "backend.admin.CustomAdminSite"


from django.contrib.admin.apps import AdminConfig
from django.contrib.auth.apps import AuthConfig
from django.contrib.contenttypes.apps import ContentTypesConfig
from allauth.account.apps import AccountConfig


class MongoAdminConfig(AdminConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"


class MongoAuthConfig(AuthConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"


class MongoContentTypesConfig(ContentTypesConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"


class MongoAccountConfig(AccountConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"
