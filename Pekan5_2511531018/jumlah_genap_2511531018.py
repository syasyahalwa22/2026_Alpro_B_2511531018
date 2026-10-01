ulang_1018 = int(input("Masukkan nilai batas: "))

jumlah_1018 = 0
for i_1018 in range(1, ulang_1018 + 1):
    if i_1018 % 2 == 0:
        print(i_1018, end=" ")
        jumlah_1018 = jumlah_1018 + i_1018

        if i_1018 < ulang_1018:
            print("+", end=" ")
        else:
            print("=", jumlah_1018, end=" ")
print()
print("Jumlah =", jumlah_1018)