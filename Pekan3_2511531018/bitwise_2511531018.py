print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_1018 = int(input("Masukkan angka bitwise-1: "))
angka2_1018 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_1018 =", angka1_1018, "| biner =", bin(angka1_1018))
print("angka2_1018 =", angka2_1018, "| biner =", bin(angka2_1018))

#Bitwise AND
hasil_1018 = angka1_1018 & angka2_1018
print("\nBitwise AND (&)")
print(angka1_1018, "&", angka2_1018, "=", hasil_1018,)
print("Biner hasil =", bin(hasil_1018))
print("Biner hasil (8 bit) =", format(hasil_1018, '08b'))

#Bitwise OR
hasil_1018 = angka1_1018 | angka2_1018
print("\nBitwise OR (|)")
print(angka1_1018, "|", angka2_1018, "=", hasil_1018)
print("Biner hasil =", bin(hasil_1018))
print("Biner hasil (8 bit) =", format(hasil_1018, '08b'))

#Bitwise XOR
hasil_1018 = angka1_1018 ^ angka2_1018
print("\nBitwise XOR (^)")
print(angka1_1018, "^", angka2_1018, "=", hasil_1018)
print("Biner hasil =", bin(hasil_1018))
print("Biner hasil (8 bit) =", format(hasil_1018, '08b'))

#Bitwise NOT
hasil_1018 = ~angka1_1018
print("\nBitwise NOT (~)")
print("~", angka1_1018, "=", hasil_1018)
print("Biner hasil =", bin(hasil_1018))
print("Biner hasil (8 bit) =", format(hasil_1018, '08b'))

#Bitwise geser kiri
jumlah_geser_1018 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1018 = angka1_1018 << jumlah_geser_1018
print("\nBitwise geser kiri (<<)")
print(angka1_1018, "<<", jumlah_geser_1018, "=", hasil_1018)
print("Biner hasil =", bin(hasil_1018))
print("Biner hasil (8 bit) =", format(hasil_1018, '08b'))

#Bitwise geser kanan
hasil_1018 = angka1_1018 >> jumlah_geser_1018
print("\nBitwise geser kanan (>>)")
print(angka1_1018, ">>", jumlah_geser_1018, "=", hasil_1018)
print("Biner hasil =", bin(hasil_1018))
print("Biner hasil (8 bit) =", format(hasil_1018, '08b'))
