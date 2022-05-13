from calendar import month
from cgitb import text
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()


class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField((""))
    name = models.TextField((""))
    class Meta:
        db_table = 'army_shop'
        # 이미 생성되어 있으므로
        managed = False