from django.contrib import admin

# Register your models here.
from .models import Code, Comment, Like


admin.site.register(Code)
admin.site.register(Comment)
admin.site.register(Like)
