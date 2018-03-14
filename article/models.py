from django.db import models
from django.contrib import admin
from .models import Block

# Create your models here.
class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name="BlockID")
    title = models.CharField("BlockName", max_length=100)
    content = models.CharField("BlockDesc", max_length=10000)
    status = models.IntegerField("Status", choices=((0, "GOOD"), (-1, "DELETE")))
    create_timestamp = models.DateTimeField("CreateTime", auto_now_add=True)
    last_update_timestamp = models.DateTimeField("LastUpdateTime", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Artical"
        verbose_name_plural = "Artical"
