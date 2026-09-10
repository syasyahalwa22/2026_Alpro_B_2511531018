is_lulus_1018 = True
is_cumlaude_1018 = True

#menggunakan boolean
nilai_1018 =85
batas_lulus_1018 = 75

# menentukan nilai boolean dari kondisi
status_kelulusan_1018 = nilai_1018 >= batas_lulus_1018 # hasilnya akan true

print("=== Ceck kelulusan ===")
print("Nilai: ", nilai_1018)
print("Apakah lulus? ", status_kelulusan_1018)
if is_lulus_1018 and is_cumlaude_1018:
   print("Selamat, Anda lulus dengan predikat Cumlaude!")