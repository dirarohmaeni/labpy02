#!/usr/bin/python3
a = int(input("masukkan bilangan A: "))
b = int(input("masukkan bilangan B: "))
c = int(input("masukkan bilangan C: "))

if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")