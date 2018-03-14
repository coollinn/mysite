from django.db import models

# Create your models here.


class Block(models.Model):
    name = models.CharField("Block_name", max_length=100)
    desc = models.CharField("Block_Desc", max_length=100)
    manager_name = models.CharField("Block_Admin", max_length=100)
    status = models.IntegerField("Status", choices=((0, "GOOD"), (-1, "DELETE")))
