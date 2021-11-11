print("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")
ikan_bakar = int(input("IKAN BAKAR      RP 25.000,00    : "))
es_doger = int(input("ES DOGER      RP 6.000,00    : "))
rujak_cingur = int(input("RUJAK CINGUR      RP 8.000,00    : "))

total_ikan_bakar = ikan_bakar * 25000
total_es_doger = es_doger * 6000
total_rujak_cingur = rujak_cingur * 8000
total_bayar = total_ikan_bakar + total_es_doger + total_rujak_cingur

print("=====TOTAL=====")
print("TOTAL IKAN BAKAR     : Rp ", total_ikan_bakar, "")
print("TOTAL ES DOGER     : Rp ", total_es_doger, "")
print("TOTAL RUJAK CINGUR     : Rp ", total_rujak_cingur, "")
print("Jumlah total biaya yang harus dibayar adalah Rp ", total_bayar)