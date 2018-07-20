from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RestModel)
admin.site.register(models.RestMenu)
admin.site.register(models.RestReviews)
