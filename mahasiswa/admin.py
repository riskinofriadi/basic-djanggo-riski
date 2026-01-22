from django.contrib import admin
from .models import Mahasiswa, Dosen, MataKuliah

admin.site.register(Mahasiswa)
admin.site.register(Dosen)
admin.site.register(MataKuliah)
