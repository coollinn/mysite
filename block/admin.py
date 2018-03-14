from django.contrib import admin
from block.models import Block

#add the new classasdf
class BlockAdmin(admin.ModelAdmin):
    list_display=("name", "desc", "manager_name", "status")

# Register your models here.
admin.site.register(Block, BlockAdmin)

