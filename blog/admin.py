from django.contrib import admin
from .models import Query,PostCategory,Post,BlogComment
# Register your models here.
admin.site.register(Query)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(BlogComment)
