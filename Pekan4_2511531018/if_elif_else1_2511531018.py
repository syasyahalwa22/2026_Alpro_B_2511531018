umur_1018 = int(input("Input umur anda: "))
sim_1018 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_1018 >= 17 and sim_1018 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

elif umur_1018 >= 17 and sim_1018 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

elif umur_1018 < 17 and sim_1018 == 'y': 
    print("Anda Belum Cukup Umur punya SIM")

else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")