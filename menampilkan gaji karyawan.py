gaji = int(input("masukkan gaji:"))
berkeluarga = (False, True)[input("sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("punya rumah? (Y/T)") == "Y"]

if gaji > 3000000:
    print ("gaji sudah diatas UMR")
if berkeluarga:
    print ("wajib ikutan asuransi dan menabung untuk pensiun")
else :
    print ("tidak perlu ikutan asuransi")

    if punya_rumah:
        print("wajib bayar pajak rumah")
    else :
        print ("tidak wajib bayar pajak rumah")
        print ("gaji belum UMR")