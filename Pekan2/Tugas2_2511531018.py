from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_1018 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_1018 = input("Masukkan Jenis Kelamin (L/P): ")
alamat_1018 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""
umur_1018 = int(input("Masukkan Umur : "))
nilai_1018 = float(input("Masukkan Skor Tes Awal : "))

id_token_1018 = 100 + 3j
lulus_1018 = nilai_1018 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_1018, "| Tipe:", type(nama_1018))
print("Jenis Kelamin :", jenis_kelamin_1018, "| Tipe:", type(jenis_kelamin_1018))

print("Alamat Domisili:")
print(alamat_1018, "| Tipe:", type(alamat_1018))

print("Umur :", umur_1018, "tahun | Tipe:", type(umur_1018))
print("Skor Tes Awal :", nilai_1018, "| Tipe:", type(nilai_1018))
print("ID Token Sinyal:", id_token_1018, "| Tipe:", type(id_token_1018))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", lulus_1018, "| Tipe:", type(lulus_1018))