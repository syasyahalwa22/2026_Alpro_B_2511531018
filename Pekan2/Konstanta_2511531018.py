from typing import final
PI: Final =3.14
print("pi: %f" % (PI))
jari_1018 = float(input('Masukkan nilai jari-jari: '))
luas_1018 = PI * jari_1018 * jari_1018
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1018, luas_1018))