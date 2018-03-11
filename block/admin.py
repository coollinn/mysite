from django.contrib import admin
from .models import Block

#add the new class
class BlockAdmin(admin.ModelAdmin):
    list_display=("name", "desc", "manager_name")

# Register your models here.
admin.site.register(Block, BlockAdmin)

