umur_1018 = int(input("Input umur anda: "))
sim_1018 = input("Apakah anda sudah punya SIM C (y/t): ") [0]

if umur_1018 >= 17 and sim_1018 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_1018 >= 17 and sim_1018 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_1018 < 17 and sim_1018 == 'y':
    print("Anda belum cukup umur punya SIM")

if umur_1018 < 17 and sim_1018 != 'y':
    print("Anda belum cukup umur bawa motor")
