from django.contrib import admin
from . import models


def add_admin(model):
    name = '%sAdmin' % model.__name__
    attrs = {
        'list_display': ('position', 'category', 'sub_category', model.fkey),
        'list_filter': ('category', 'sub_category'),
    }
    cls = type(name, (admin.ModelAdmin,), attrs)
    admin.site.register(model, cls)


for model in (models.FullTimeJob,models.PersonalJob,
              models.PartTimeJob):
    add_admin(model)
