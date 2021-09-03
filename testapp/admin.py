from django.contrib import admin

from . import models

admin.site.register(models.CheckList)
admin.site.register(models.CheckListItem)
