#input dari user
total_belanja_1018 = float(input("Masukkan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1018 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_1018 = input_member_1018 in ["y", 'ya']

#input status kode promo (mengecek apakah user mengeik 'y' atau 'ya')
input_promo_1018 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1018 = input_promo_1018 in ["y", "ya"]

total_diskon_persen_1018 = 0

if total_belanja_1018 > 1000000:
    total_diskon_persen_1018 += 10  #Diskon belanja besar

if is_member_1018:
    total_diskon_persen_1018 += 5 #Diskon member

if kode_promo_valid_1018:
    total_diskon_persen_1018 += 15 #Diskon voucher

#Menghitung nominal diskon dan total bayar
nominal_diskon_1018 = total_belanja_1018 * (total_diskon_persen_1018 / 100)
total_bayar_1018 = total_belanja_1018 - nominal_diskon_1018

#output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon    : {total_diskon_persen_1018}% (Rp {nominal_diskon_1018:,.0f})")
print(f"Total Bayar     : Rp {total_bayar_1018:,.0f}")

print(f"Total diskon yng Anda dapatkan: {total_diskon_persen_1018}%")
