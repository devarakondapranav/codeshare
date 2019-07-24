from django.contrib import admin

# Register your models here.
from .models import Code, Comment

admin.site.register(Code)
admin.site.register(Comment)
