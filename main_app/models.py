from django.db import models

class A02(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(db_column='NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    liandata = models.DateTimeField(blank=True, null=True)
    anno = models.CharField(max_length=20, blank=True, null=True)
    executegov = models.CharField(max_length=100, blank=True, null=True)
    biaodi = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    partycardnum = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a02'


class User(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
