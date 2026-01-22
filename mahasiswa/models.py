from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def clean(self):
        if not self.npm.isdigit():
            raise ValidationError({'npm': 'NPM harus berupa angka'})

    def __str__(self):
        return f"{self.nama} ({self.npm})"


class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    nidn = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    homebase = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class MataKuliah(models.Model):
    nama_mk = models.CharField(max_length=100)
    kode_mk = models.CharField(max_length=10, unique=True)
    sks = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    semester = models.PositiveSmallIntegerField()

    dosen = models.ForeignKey(
        Dosen,
        on_delete=models.CASCADE,
        related_name='mata_kuliah'
    )

    mahasiswa = models.ManyToManyField(
        Mahasiswa,
        blank=True,
        related_name='mata_kuliah'
    )

    def __str__(self):
        return f"{self.nama_mk} ({self.kode_mk})"
