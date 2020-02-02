from django.contrib import admin
from pladform.models import Blog, Author, Entry


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
# Register your models here.
