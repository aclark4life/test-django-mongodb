# test_django_mongodb

Via https://github.com/mongodb-labs/django-mongodb/pull/18/commits/15e97c543b4e80d7496fe8445f4d76d58703940b

In your Django settings, you must specify that all models should use
`MongoAutoField`.

```python
DEFAULT_AUTO_FIELD = "django_mongodb.fields.MongoAutoField"
```

This won't override any apps that have an `AppConfig` that specifies
`default_auto_field`. For those apps, you'll need to create a custom
`AppConfig`.

For example, you might create `mysite/apps.py` like this:

```python
from django.contrib.admin.apps import AdminConfig
from django.contrib.auth.apps import AuthConfig
from django.contrib.contenttypes.apps import ContentTypesConfig


class MongoAdminConfig(AdminConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"


class MongoAuthConfig(AuthConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"


class MongoContentTypesConfig(ContentTypesConfig):
    default_auto_field = "django_mongodb.fields.MongoAutoField"
```

Then replace each app reference in the `INSTALLED_APPS` setting with the new
``AppConfig``. For example, replace  `'django.contrib.admin'` with
`'mysite.apps.MongoAdminConfig'`.

Because all models must use `MongoAutoField`, each third-party and contrib app
you use needs to have its own migrations specific to MongoDB.

For example, you might configure your settings like this:

```python
MIGRATION_MODULES = {
    "admin": "mongo_migrations.admin",
    "auth": "mongo_migrations.auth",
    "contenttypes": "mongo_migrations.contenttypes",
}
```

After creating a `mongo_migrations` directory, you can then run:

```console
$ python manage.py makemigrations admin auth contenttypes
Migrations for 'admin':
  mongo_migrations/admin/0001_initial.py
    - Create model LogEntry
...
```


