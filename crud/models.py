from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nrp = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    umur = models.IntegerField()
    gender =  models.CharField(max_length=1)
    alamat = models.CharField(max_length=255)
