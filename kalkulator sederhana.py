angka1 = float(input("masukkan angka pertama: "))
angka2 = float(input("masukkan angka kedua: "))
operator = input("masukkan operator (+, -, *, /): ")
if operator == '+':
    hasil = angka1 + angka2
    print(f"hasil: {angka1} {angka2} = {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print(f"hasil: {angka1} - {angka2} = {hasil}")
elif operator == '*':
    hasil = angka1 * angka2
    print(f"hasil: {angka1} * {angka2} = {hasil}")
elif operator == '/':
    hasil = angka1 / angka2
    print(f"hasil: {angka1} / {angka2} = {hasil}")
else: 
    print("error: pembagian dengan nol tidak diperbolehkan!")
print("operator tidak valid! silahkan masukkan +, -, *, atau /")