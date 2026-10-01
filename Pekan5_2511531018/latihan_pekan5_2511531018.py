tinggi_1018 = int(input("Masukkan tinggi segitiga: "))

for i_1018 in range(1, tinggi_1018 + 1):
    for j_1018 in range(tinggi_1018 - i_1018):
        print(" ", end=" ")

    for j_1018 in range(2 * i_1018 - 1):
        print("*", end=" ")
    print() 