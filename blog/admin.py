from django.contrib import admin
from .models import Topic,Blog,Comment
# Register your models here.

admin.site.register(Topic)
admin.site.register(Blog)
admin.site.register(Comment)