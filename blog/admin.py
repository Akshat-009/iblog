from django.contrib import admin
from .models import Query,PostCategory,Post,BlogComment
# Register your models here.
admin.site.register(Query)
admin.site.register(PostCategory)

admin.site.register(BlogComment)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tiny.js',)
