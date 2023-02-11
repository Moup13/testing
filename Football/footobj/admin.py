from django.contrib import admin

# Register your models here.
from footobj.models import Football, MinyFootball

admin.site.register(Football)
admin.site.register(MinyFootball)