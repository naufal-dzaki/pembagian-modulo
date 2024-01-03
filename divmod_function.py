def hitung_pembagian(angka1, angka2):
  hasil_bagi, sisa_bagi = divmod(angka1, angka2)
  return hasil_bagi, sisa_bagi

angka1 = float(input("Masukkan angka yang akan dibagi: "))
angka2 = float(input("Masukkan angka pembagi: "))

if angka2 == 0:
    print("Oops, anda melakukan kesalahan! Angka pembagi tidak boleh nol.")
else:
    hasil_bagi, sisa_bagi = hitung_pembagian(angka1, angka2)

    print(f"Hasil bagi dari {angka1} dibagi {angka2} adalah {hasil_bagi}")
    print(f"Sisa bagi dari {angka1} dibagi {angka2} adalah {sisa_bagi}")