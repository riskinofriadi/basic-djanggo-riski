print("FORMS.PY TERLOAD")
from django import forms
from .models import Mahasiswa, Dosen, MataKuliah


class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'npm', 'email']


class DosenForm(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = ['nama', 'nidn', 'email', 'no_hp', 'alamat', 'homebase']


class MataKuliahForm(forms.ModelForm):
    class Meta:
        model = MataKuliah
        fields = [
            'nama_mk',
            'kode_mk',
            'sks',
            'semester',
            'dosen',
            'mahasiswa',
        ]
print("MATAKULIAHFORM ADA:", "MataKuliahForm" in globals())
class UploadCSVForm(forms.Form):
    file = forms.FileField(label="Upload file CSV Mahasiswa")