from django.contrib import admin

# Register your models here.
from .models import model_class

admin.site.register(model_class)
