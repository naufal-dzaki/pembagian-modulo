def check_tahun_kabisat(tahun):
    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
       return "tahun kabisat"
    else:
       return "bukan tahun kabisat"

tahun = int(input("Masukkan tahun : "))

hasil = check_tahun_kabisat(tahun)

print(f"{tahun} adalah {hasil}")