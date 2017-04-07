# -*- coding: UTF-8 -*-
from django.db import models


# Create your models here.

class Employee(models.Model):
    username = models.CharField(max_length=30)
    realname = models.CharField(max_length=30)

    class Meta:
        db_table = 'employee'
        verbose_name = '员工表'
        verbose_name_plural = '员工表'
