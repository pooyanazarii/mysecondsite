from django.contrib import admin
from myblog.models import Post
# Register your models here.
@admin.register(Post)
class Post_Admin (admin.ModelAdmin):
    empty_value_display = '-empty-'
    #list_display = ['title']
    search_fields = ['content','title']
