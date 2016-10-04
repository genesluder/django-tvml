
from django.contrib import admin

from .models import Category, Collection, Video

admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Video)