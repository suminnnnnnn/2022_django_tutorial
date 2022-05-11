from django.db import models
# create table column<DDL +DML>
class Curriculum(models.Model):
    name = models.CharField(max_length=255)