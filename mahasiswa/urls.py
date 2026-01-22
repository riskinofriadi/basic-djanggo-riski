from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Mahasiswa
    path('mahasiswa/', views.mahasiswa_list, name='mahasiswa_list'),
    path('mahasiswa/input/', views.input_mahasiswa, name='input_mahasiswa'),
    path('mahasiswa/<int:id>/edit/', views.edit_mahasiswa, name='edit_mahasiswa'),
    path('mahasiswa/<int:id>/delete/', views.delete_mahasiswa, name='delete_mahasiswa'),
    path('mahasiswa/import-csv/', views.import_csv_mahasiswa, name='import_csv'),
    path('mahasiswa/export-csv/', views.export_csv_mahasiswa, name='export_csv'),

    # Dosen
    path('dosen/', views.dosen_list, name='dosen_list'),
    path('dosen/input/', views.input_dosen, name='input_dosen'),
    path('dosen/<int:id>/edit/', views.edit_dosen, name='edit_dosen'),
    path('dosen/<int:id>/delete/', views.delete_dosen, name='delete_dosen'),
    path('dosen/import-csv/', views.import_csv_dosen, name='import_csv_dosen'),
    path('dosen/export-csv/', views.export_csv_dosen, name='export_csv_dosen'),

    # Mata Kuliah
    path('matakuliah/', views.matakuliah_list, name='matakuliah_list'),
    path('matakuliah/input/', views.input_matakuliah, name='input_matakuliah'),
    path('matakuliah/<int:id>/edit/', views.edit_matakuliah, name='edit_matakuliah'),
    path('matakuliah/<int:id>/delete/', views.delete_matakuliah, name='delete_matakuliah'),
    path('matakuliah/export-csv/', views.export_csv_matakuliah, name='export_csv_matakuliah'),
    path('matakuliah/import-csv/', views.import_csv_matakuliah, name='import_csv_matakuliah'),

]
