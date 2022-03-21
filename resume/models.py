from django.db import models

# Create your models here.

class User(models.Model):
    country = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile = models.IntegerField(default=0,null=True)
    email = models.CharField(max_length=100,null=True)
    hobby1 = models.CharField(max_length=200, null=True)
    hobby2 = models.CharField(max_length=200, null=True)
    hobby3 = models.CharField(max_length=200, null=True)



    def __str__(self):
        return self.country


class Education(models.Model):
    degree = models.CharField(max_length=100, null=True)
    hnd = models.CharField(max_length=100, null=True)



    def __str__(self):
        return self.degree


class Certification(models.Model):
    certification1 = models.CharField(max_length=100, null=True)
    certification2 = models.CharField(max_length=100, null=True)
    certification3 = models.CharField(max_length=100, null=True)
    certification4 = models.CharField(max_length=100, null=True)
    certification5 = models.CharField(max_length=100, null=True)



    def __str__(self):
        return self.certification1

