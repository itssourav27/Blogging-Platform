from django.contrib import admin

# Register your models here.
from .models import Blogpost

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    

    list_dispaly = ('title', 'author', 'created_at')
    prepopulated_fields = {"slug":("title",)}

