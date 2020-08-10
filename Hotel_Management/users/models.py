from django.db import models


# Create your models here.

class U_Registration(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.TextField(max_length=50)
    phone_no = models.IntegerField
    password = models.TextField(max_length=30)


class S_Registration(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.TextField(max_length=50)
    phone_no = models.IntegerField
    password = models.TextField(max_length=30)
