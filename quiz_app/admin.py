from django.contrib.gis import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps
from quiz_app.models import *

app_models = apps.get_app_config('quiz_app').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
