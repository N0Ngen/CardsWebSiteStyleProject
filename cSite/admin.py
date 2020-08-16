from django.contrib import admin
from django.db import models
from .models import Tutorial

# Register your models here.

class cardview(admin.ModelAdmin):
  fieldsets = [
    ('Title/Date', {'fields': ['tut_title', 'tut_PD']}),
    ('Content', {'fields': ['tut_content']}),
  ]

admin.site.register(Tutorial, cardview)