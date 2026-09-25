print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. INPUT DATA PENGUNJUNG & STRING HANDLING
nama_1018 = input("Masukkan Nama Pengunjung        : ")
umur_1018 = int(input("Input umur anda                 : "))
sim_1018 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].strip().lower()

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_1018 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1018 = int(input("Masukkan jumlah tiket           : "))

input_member_1018 = input("Apakah Anda member? (y/t)       : ").strip().lower()
is_member_1018 = input_member_1018 in ["y", "ya"]

input_promo_1018 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()
kode_promo_valid_1018 = input_promo_1018 in ["y", "ya"]

# 2. IF TUNGGAL - VALIDASI KELOGISAN JUMLAH TIKET
if jumlah_tiket_1018 <= 0:
    print("\nPeringatan: Jumlah tiket tidak valid! Transaksi dihentikan.")
    exit()

# 3. MATCH-CASE - PEMILIHAN WAHANA (1-5 DAN DEFAULT _)
match paket_1018:
    case 1:
        nama_wahana_1018 = "Wahana Safari Rimba"
        harga_satuan_1018 = 50000
    case 2:
        nama_wahana_1018 = "Wahana Arung Jeram"
        harga_satuan_1018 = 75000
    case 3:
        nama_wahana_1018 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1018 = 120000
    case 4:
        nama_wahana_1018 = "Wahana Roller Coaster Kilat"
        harga_satuan_1018 = 100000
    case 5:
        nama_wahana_1018 = "Wahana All-Access VIP"
        harga_satuan_1018 = 220000
    case _:
        print("\nPaket wahana tidak valid! Transaksi dihentikan.")
        exit()

# 4. IF-ELIF-ELSE DENGAN OPERATOR LOGIKA (KHUSUS PAKET 3 = ATV)
#    UNTUK PAKET LAIN: IF-ELSE SEDERHANA CEK UMUR >= 10
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_1018 == 3 and umur_1018 >= 17 and sim_1018 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_1018 == 3 and umur_1018 >= 17 and sim_1018 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_1018 == 3 and umur_1018 < 17 and sim_1018 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_1018 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_1018 >= 10:
    print("Status Akses: Umur Anda memenuhi syarat minimal untuk menaiki wahana ini.")
else:
    print("Status Akses: Umur Anda belum memenuhi syarat minimal (10 tahun) untuk menaiki wahana ini.")

# 5. MULTI-IF TERPISAH - AKUMULASI DISKON BERTINGKAT
subtotal_1018 = harga_satuan_1018 * jumlah_tiket_1018
total_diskon_persen_1018 = 0

if subtotal_1018 >= 200000:
    total_diskon_persen_1018 += 10  # Diskon Belanja Besar

if is_member_1018:
    total_diskon_persen_1018 += 5  # Diskon Member

if kode_promo_valid_1018:
    total_diskon_persen_1018 += 15  # Diskon Voucher Promo

if jumlah_tiket_1018 >= 5:
    total_diskon_persen_1018 += 5  # Diskon Tambahan Rombongan

nominal_diskon_1018 = subtotal_1018 * (total_diskon_persen_1018 / 100)
total_bayar_1018 = subtotal_1018 - nominal_diskon_1018

# 6. IF-ELSE - EVALUASI KELULUSAN AUDIT (BONUS SOUVENIR)
if total_bayar_1018 > 300000:
    catatan_layanan_1018 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_1018 = "Terima kasih telah berkunjung."

# 7. OUTPUT RINCIAN PEMBAYARAN
print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_1018}")
print(f"Wahana Dipilih   : {nama_wahana_1018}")
print(f"Subtotal Belanja : Rp {subtotal_1018:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1018}% (Rp {nominal_diskon_1018:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1018:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_1018}")
print("Program Selesai")
