print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_1018 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai Atas 
print("#", end="")
for k_1018 in range(4 * n_1018 + 5):
    print("=", end="")
print("#", end="")
print()
 
# Fase 1: Jam Pasir Atas (baris N turun sampai 1) 
for baris_1018 in range(n_1018, 0, -1):
    print("|", end="")
    print(" ", end="")                                  

    for spasi_1018 in range(2 * (n_1018 - baris_1018)): 
        print(" ", end="")

    for angka_1018 in range(baris_1018, 0, -1):         
        print(angka_1018, end=" ")

    print("<*>", end="")                               

    for angka_1018 in range(1, baris_1018 + 1):         
        print(" ", end="")
        print(angka_1018, end="")

    for spasi_1018 in range(2 * (n_1018 - baris_1018)): 
        print(" ", end="")

    print(" ", end="")                                  
    print("|", end="")
    print()

# Fase 2: Poros Titik Pusat 
print("|", end="")
for spasi_1018 in range(2 * n_1018 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_1018 in range(2 * n_1018 + 1):
    print(" ", end="")
print("|", end="")
print()

# Fase 3: Jam Pasir Bawah (baris 1 naik sampai N) 
for baris_1018 in range(1, n_1018 + 1):
    print("|", end="")
    print(" ", end="")

    for spasi_1018 in range(2 * (n_1018 - baris_1018)):
        print(" ", end="")

    for angka_1018 in range(baris_1018, 0, -1):
        print(angka_1018, end=" ")

    print("<*>", end="")

    for angka_1018 in range(1, baris_1018 + 1):
        print(" ", end="")
        print(angka_1018, end="")

    for spasi_1018 in range(2 * (n_1018 - baris_1018)):
        print(" ", end="")

    print(" ", end="")
    print("|", end="")
    print()

# Bingkai Bawah 
print("#", end="")
for k_1018 in range(4 * n_1018 + 5):
    print("=", end="")
print("#", end="")
print()