from django.contrib import admin
from .models import Article

#add the new classasdf
class ArticalAdmin(admin.ModelAdmin):
    list_display=("block", "title", "content")

# Register your models here.
admin.site.register(Article, ArticalAdmin)
