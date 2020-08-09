from django.contrib import admin
from .models import Query,PostCategory,Post
# Register your models here.
admin.site.register(Query)
admin.site.register(PostCategory)
admin.site.register(Post)
