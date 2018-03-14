from django.contrib import admin
from article.models import Article

#add the new classasdf
class ArticalAdmin(admin.ModelAdmin):
    list_display=("block", "title", "content", "create_timestamp", "last_update_timestamp" ,"status")

# Register your models here.
admin.site.register(Article, ArticalAdmin)
