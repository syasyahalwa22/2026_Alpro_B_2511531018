batas_1018 = int(input("Masukkan nilai batas: "))
for line in range(1, batas_1018 + 1):
    for i_1018 in range(1, (-1 * line + batas_1018) + 1):
        print(".", end=" ")
    print(line)