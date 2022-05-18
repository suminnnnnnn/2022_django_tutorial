from pickle import TRUE
from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField

class Shop(models.Model):
    shop_id = IntegerField(primary_key=True)
    shop_name = CharField(max_length=100, null=True)
    shop_desc = CharField(max_length=100, null=True)
    rest_date = CharField(max_length=100, null=True)
    parking_info = CharField(max_length=100, null=True)
    img_path = CharField(max_length=255, null=True)
    class Meta:
        db_table = 'shop'
        app_label = 'thirdapp'
        managed = False
class JejuOlle(models.Model):
    course = CharField(max_length=10)
    course_name = CharField(max_length=10)
    distance = FloatField()
    time_info = CharField(max_length=10)
    start_end_info = CharField(max_length=30)
    cre_date = DateField()
    class Meta:
        db_table = 'jeju_olle'
        managed = False

class Owner(models.Model):
    name = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = 'owner'
        managed = False

class Animal(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'animal'
        managed = False

class Warranty(models.Model):
    model_nm = models.CharField(max_length=50, null=True)
    period = models.IntegerField(null=True)
    class Meta:
        db_table = 'warranty'
        managed = False
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    warranty = models.OneToOneField(Warranty, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'product'
        managed = False

class Playground(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    animals = models.ManyToManyField(Animal, null=True)
    class Meta:
         db_table = 'playground'
         managed = False

class Dept(models.Model):
    depno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14)
    loc = models.CharField( max_length=13)
    
    class Meta:
         db_table = 'dept'
         managed = False

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=9)
    mgr = models.IntegerField()
    hiredate = models.DateTimeField()
    sal = models.IntegerField()
    comm = models.IntegerField()
    depno = models.ForeignKey(Dept, on_delete=models.CASCADE)

    class Meta:
         db_table = 'emp'
         managed = False

class Hospital(models.Model):
    sido = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    medical = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    tel = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'hospital'
        managed = False

