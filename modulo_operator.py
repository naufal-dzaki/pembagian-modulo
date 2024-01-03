def pembagian_modulo(angka1, angka2):
  if angka2 == 0:
    return "angka pembagi tidak boleh nol"

  sisa_bagi = angka1 % angka2
  return sisa_bagi

angka1 = float(input("Masukkan angka yang akan dibagi : "))
angka2 = float(input("Masukkan angka pembagi : "))

sisa_bagi = pembagian_modulo(angka1, angka2)

if sisa_bagi == "angka pembagi tidak boleh nol":
  print(f"Oops, anda melakukan kesalahan! {sisa_bagi}")
else:
  print(f"Modulus dari {angka1} dibagi {angka2} adalah {sisa_bagi}")