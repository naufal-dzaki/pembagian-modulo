def check_ganjil_genap(angka):
   if angka % 2 == 0:
      return "genap"
   else:
      return "ganjil"

angka = float(input("Masukkan angka : "))

hasil = check_ganjil_genap(angka)

print(f"{angka} adalah angka {hasil}")