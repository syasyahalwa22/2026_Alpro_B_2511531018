print("==========================================")
print("       SISTEM TRANSAKSI TOKO")
print("==========================================")

# ==============================
# INPUT DATA PELANGGAN
# ==============================

nama_1018 = input("Masukkan Nama Pelanggan : ")
status_1018 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
belanja_1018 = float(input("Masukkan Total Harga Belanja : Rp"))
jumlah_1018 = int(input("Masukkan Jumlah Barang : "))
kode_promo_1018 = input("Masukkan Kode Promo : ").upper()


# OPERATOR PERBANDINGAN
syarat_belanja_1018 = belanja_1018 >= 200000
syarat_jumlah_1018 = jumlah_1018 >= 3
status_anggota_1018 = status_1018 == "member"


# OPERATOR KEANGGOTAAN
daftar_promo_1018 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_1018 = kode_promo_1018 in daftar_promo_1018
promo_tidak_tersedia_1018 = kode_promo_1018 not in daftar_promo_1018


# OPERATOR LOGIKA
diskon_member_1018 = status_anggota_1018 and syarat_belanja_1018

dapat_promo_1018 = (
    syarat_belanja_1018
    and syarat_jumlah_1018
    and promo_tersedia_1018
)

akses_pelanggan_1018 = (
    status_anggota_1018
    or promo_tersedia_1018
)


# OPERATOR ARITMATIKA
diskon_1018 = 0

if diskon_member_1018:
    diskon_1018 = belanja_1018 * 10 / 100

total_bayar_1018 = belanja_1018 - diskon_1018
rata_rata_1018 = belanja_1018 / jumlah_1018

sisa_bagi_1018 = belanja_1018 % jumlah_1018


# OPERATOR PENUGASAN
total_bayar_1018 += 0
diskon_1018 += 0

poin_1018 = 0
poin_1018 += int(total_bayar_1018 // 10000)


# OPERATOR IDENTITAS
objek_1_1018 = daftar_promo_1018
objek_2_1018 = daftar_promo_1018
objek_3_1018 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

identitas_sama_1018 = objek_1_1018 is objek_2_1018
identitas_berbeda_1018 = objek_1_1018 is not objek_3_1018
nilai_sama_1018 = objek_1_1018 == objek_3_1018


# OPERATOR BITWISE
status_bit_1018 = 0

if status_anggota_1018:
    status_bit_1018 |= 1       # 0001

if syarat_belanja_1018:
    status_bit_1018 |= 2       # 0010

if syarat_jumlah_1018:
    status_bit_1018 |= 4       # 0100

if promo_tersedia_1018:
    status_bit_1018 |= 8       # 1000

# AND
cek_anggota_1018 = status_bit_1018 & 1
cek_promo_1018 = status_bit_1018 & 8

# OR
kode_gabungan_1018 = 1 | 8

# XOR
kode_referensi_1018 = 11
hasil_xor_1018 = status_bit_1018 ^ kode_referensi_1018

# Pergeseran
hasil_shift_1018 = status_bit_1018 << 1


# HAK AKSES
kode_akses_1018 = 0

if status_anggota_1018:
    kode_akses_1018 |= 1

if promo_tersedia_1018:
    kode_akses_1018 |= 2

if kode_promo_1018 == "GRATISONGKIR":
    kode_akses_1018 |= 4

akses_anggota_1018 = (kode_akses_1018 & 1) != 0
akses_promo_1018 = (kode_akses_1018 & 2) != 0
akses_pengiriman_1018 = (kode_akses_1018 & 4) != 0


# OUTPUT DATA
print("\n==========================================")
print("             DATA TRANSAKSI")
print("==========================================")

print("Nama Pelanggan       :", nama_1018)
print("Status Pelanggan     :", status_1018)
print("Total Belanja        : Rp{:,.0f}".format(belanja_1018))
print("Jumlah Barang        :", jumlah_1018)
print("Kode Promo           :", kode_promo_1018)


# HASIL VALIDASI
print("\n==========================================")
print("             HASIL VALIDASI")
print("==========================================")

print("Belanja >= Rp200000  :", syarat_belanja_1018)
print("Jumlah Barang >= 3   :", syarat_jumlah_1018)
print("Status Anggota       :", status_anggota_1018)
print("Kode Promo Tersedia  :", promo_tersedia_1018)
print("Kode Promo Tidak Ada :", promo_tidak_tersedia_1018)
print("Dapat Diskon Member  :", diskon_member_1018)
print("Dapat Promo           :", dapat_promo_1018)


# HASIL PERHITUNGAN
print("\n==========================================")
print("             HASIL PERHITUNGAN")
print("==========================================")

print("Besarnya Diskon      : Rp{:,.0f}".format(diskon_1018))
print("Total Pembayaran     : Rp{:,.0f}".format(total_bayar_1018))
print("Rata-rata Barang     : Rp{:,.2f}".format(rata_rata_1018))
print("Sisa Pembagian       :", sisa_bagi_1018)
print("Poin Pelanggan       :", poin_1018)


# HAK AKSES PELANGGAN
print("\n==========================================")
print("          HAK AKSES PELANGGAN")
print("==========================================")

print("Kode Hak Akses       :", kode_akses_1018)
print("Akses Anggota        :", akses_anggota_1018)
print("Akses Promo          :", akses_promo_1018)
print("Akses Pengiriman Gratis :", akses_pengiriman_1018)


# OPERATOR IDENTITAS
print("\n==========================================")
print("          OPERATOR IDENTITAS")
print("==========================================")

print("Objek 1 is Objek 2   :", identitas_sama_1018)
print("Objek 1 is not Objek 3 :", identitas_berbeda_1018)
print("Objek 1 == Objek 3   :", nilai_sama_1018)


# OPERASI BITWISE
print("\n==========================================")
print("             OPERASI BITWISE")
print("==========================================")

print("Kode Status Transaksi")
print("Anggota             : 0001")
print("Belanja >= 200000   : 0010")
print("Jumlah >= 3         : 0100")
print("Promo tersedia      : 1000")

print("\nKode Biner           :", format(status_bit_1018, "04b"))
print("Kode Desimal        :", status_bit_1018)

print("\n--- AND ---")
print("Cek Anggota")
print(
    format(status_bit_1018, "04b"),
    "& 0001"
)
print("Hasil Biner         :", format(cek_anggota_1018, "04b"))
print("Hasil Desimal       :", cek_anggota_1018)

print("\nCek Promo")
print(
    format(status_bit_1018, "04b"),
    "& 1000"
)
print("Hasil Biner         :", format(cek_promo_1018, "04b"))
print("Hasil Desimal       :", cek_promo_1018)

print("\n--- OR ---")
print("0001 | 1000")
print("Hasil Biner         :", format(kode_gabungan_1018, "04b"))
print("Hasil Desimal       :", kode_gabungan_1018)

print("\n--- XOR ---")
print("Kode Transaksi      :", format(status_bit_1018, "04b"))
print("Kode Referensi      :", format(kode_referensi_1018, "04b"))
print(
    format(status_bit_1018, "04b"),
    "^",
    format(kode_referensi_1018, "04b")
)
print("Hasil Biner         :", format(hasil_xor_1018, "04b"))
print("Hasil Desimal       :", hasil_xor_1018)

print("\n--- PERGESERAN ---")
print(format(status_bit_1018, "04b"), "<< 1")
print("Hasil Biner         :", format(hasil_shift_1018, "b"))
print("Hasil Desimal       :", hasil_shift_1018)

print("\n==========================================")
print("              SELESAI")
print("==========================================")