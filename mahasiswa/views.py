from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from io import TextIOWrapper
from django.db import IntegrityError

# =========================
# IMPORT MODEL
# =========================
from .models import Mahasiswa, Dosen, MataKuliah

# =========================
# IMPORT FORM
# =========================
from .forms import MahasiswaForm, DosenForm, UploadCSVForm
from .forms_matakuliah import MataKuliahForm


# =========================
# DASHBOARD
# =========================
def dashboard(request):
    return render(request, 'mahasiswa/dashboard.html')


# =====================================================
# MAHASISWA
# =====================================================

def mahasiswa_list(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/home.html', {
        'mahasiswa': mahasiswa
    })


def input_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa_list')
    else:
        form = MahasiswaForm()

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'title': 'Tambah Mahasiswa'
    })


def edit_mahasiswa(request, id):
    mahasiswa = get_object_or_404(Mahasiswa, id=id)

    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa_list')
    else:
        form = MahasiswaForm(instance=mahasiswa)

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'title': 'Edit Mahasiswa'
    })


def delete_mahasiswa(request, id):
    mahasiswa = get_object_or_404(Mahasiswa, id=id)
    mahasiswa.delete()
    return redirect('mahasiswa_list')


# =====================================================
# IMPORT CSV MAHASISWA
# =====================================================

def import_csv_mahasiswa(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                return render(request, 'mahasiswa/import_csv.html', {
                    'form': form,
                    'error': 'File harus berformat CSV'
                })

            file_data = TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.DictReader(file_data)

            for row in reader:
                try:
                    mahasiswa = Mahasiswa(
                        nama=row['nama'],
                        npm=row['npm'],
                        email=row['email']
                    )
                    mahasiswa.full_clean()
                    mahasiswa.save()
                except IntegrityError:
                    continue
                except Exception:
                    continue

            return redirect('mahasiswa_list')

    else:
        form = UploadCSVForm()

    return render(request, 'mahasiswa/import_csv.html', {
        'form': form
    })


# =====================================================
# EXPORT CSV MAHASISWA
# =====================================================

def export_csv_mahasiswa(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mahasiswa.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nama', 'NPM', 'Email'])

    for m in Mahasiswa.objects.all():
        writer.writerow([m.nama, m.npm, m.email])

    return response


# =====================================================
# DOSEN
# =====================================================

def dosen_list(request):
    dosen = Dosen.objects.all()
    return render(request, 'mahasiswa/dosen.html', {
        'dosen': dosen
    })


def input_dosen(request):
    if request.method == 'POST':
        form = DosenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dosen_list')
    else:
        form = DosenForm()

    return render(request, 'mahasiswa/dosen_form.html', {
        'form': form,
        'title': 'Tambah Dosen'
    })


def edit_dosen(request, id):
    dosen = get_object_or_404(Dosen, id=id)

    if request.method == 'POST':
        form = DosenForm(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            return redirect('dosen_list')
    else:
        form = DosenForm(instance=dosen)

    return render(request, 'mahasiswa/dosen_form.html', {
        'form': form,
        'title': 'Edit Dosen'
    })


def delete_dosen(request, id):
    dosen = get_object_or_404(Dosen, id=id)
    dosen.delete()
    return redirect('dosen_list')


# =====================================================
# IMPORT CSV DOSEN
# =====================================================

def import_csv_dosen(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                return render(request, 'mahasiswa/import_csv_dosen.html', {
                    'form': form,
                    'error': 'File harus berformat CSV'
                })

            file_data = TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.DictReader(file_data)

            for row in reader:
                try:
                    dosen = Dosen(
                        nama=row['nama'],
                        nidn=row['nidn'],
                        email=row['email'],
                        no_hp=row['no_hp'],
                        alamat=row['alamat'],
                        homebase=row['homebase']
                    )
                    dosen.full_clean()
                    dosen.save()
                except IntegrityError:
                    continue
                except Exception:
                    continue

            return redirect('dosen_list')

    else:
        form = UploadCSVForm()

    return render(request, 'mahasiswa/import_csv_dosen.html', {
        'form': form
    })


# =====================================================
# EXPORT CSV DOSEN
# =====================================================

def export_csv_dosen(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dosen.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Nama', 'NIDN', 'Email', 'No HP', 'Alamat', 'Homebase'
    ])

    for d in Dosen.objects.all():
        writer.writerow([
            d.nama, d.nidn, d.email, d.no_hp, d.alamat, d.homebase
        ])

    return response


# =====================================================
# MATA KULIAH
# =====================================================

# =====================================================
# IMPORT CSV MATA KULIAH (ADVANCED)
# =====================================================

def import_csv_matakuliah(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                return render(request, 'mahasiswa/import_csv_matakuliah.html', {
                    'form': form,
                    'error': 'File harus berformat CSV'
                })

            file_data = TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.DictReader(file_data)

            for row in reader:
                try:
                    dosen = Dosen.objects.get(nidn=row['nidn_dosen'])

                    mk = MataKuliah(
                        nama_mk=row['nama_mk'],
                        kode_mk=row['kode_mk'],
                        sks=int(row['sks']),
                        semester=int(row['semester']),
                        dosen=dosen
                    )
                    mk.full_clean()
                    mk.save()

                except Dosen.DoesNotExist:
                    # dosen tidak ditemukan → dilewati
                    continue
                except IntegrityError:
                    continue
                except Exception:
                    continue

            return redirect('matakuliah_list')

    else:
        form = UploadCSVForm()

    return render(request, 'mahasiswa/import_csv_matakuliah.html', {
        'form': form
    })


def matakuliah_list(request):
    matakuliah = MataKuliah.objects.all()
    return render(request, 'mahasiswa/matakuliah.html', {
        'matakuliah': matakuliah
    })


def input_matakuliah(request):
    if request.method == 'POST':
        form = MataKuliahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matakuliah_list')
    else:
        form = MataKuliahForm()

    return render(request, 'mahasiswa/matakuliah_form.html', {
        'form': form,
        'title': 'Tambah Mata Kuliah'
    })


def edit_matakuliah(request, id):
    matakuliah = get_object_or_404(MataKuliah, id=id)

    if request.method == 'POST':
        form = MataKuliahForm(request.POST, instance=matakuliah)
        if form.is_valid():
            form.save()
            return redirect('matakuliah_list')
    else:
        form = MataKuliahForm(instance=matakuliah)

    return render(request, 'mahasiswa/matakuliah_form.html', {
        'form': form,
        'title': 'Edit Mata Kuliah'
    })


def delete_matakuliah(request, id):
    matakuliah = get_object_or_404(MataKuliah, id=id)
    matakuliah.delete()
    return redirect('matakuliah_list')


# =====================================================
# EXPORT CSV MATA KULIAH
# =====================================================

def export_csv_matakuliah(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mata_kuliah.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Nama Mata Kuliah', 'Kode MK', 'SKS', 'Semester', 'Dosen'
    ])

    for mk in MataKuliah.objects.select_related('dosen').all():
        writer.writerow([
            mk.nama_mk,
            mk.kode_mk,
            mk.sks,
            mk.semester,
            mk.dosen.nama if mk.dosen else '-'
        ])

    return response
