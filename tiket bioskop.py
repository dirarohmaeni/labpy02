# Program untuk menghitung harga tiket bioskop

# Harga tiket
harga_reguler = 50000
harga_vip = 100000

# Input dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Menentukan harga berdasarkan tipe tiket
if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
    total_harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    total_harga = 0

# Menghitung diskon jika user adalah member
if status_member == "ya":
    diskon = total_harga * 0.2
    total_harga -= diskon

# Menampilkan total harga yang harus dibayar
print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")