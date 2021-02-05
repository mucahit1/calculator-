def topla(a, b):
   return a + b
def cıkar(a, b):
   return a - b
def carp(a, b):
   return a * b
def bol(a, b):
 return a / b
yaz("İşlemi seçiniz.")
yaz("+")
yaz("-")
yaz("*")
yaz("/")
# kullanıcı gırısı
tercih = input("Islemı onayla:")
A = int(input("Bırıncı rakam: "))
B = int(input("Ikıncı rakam: "))
yinele tercih == '+':
   yaz(A,"+",B,"=", topla(A,B))
eger degilse tercih == '-':
   print(A,"-",B,"=", cıkar(A,B))
 eger degilse tercih == '*':
   yaz(A,"*",B,"=", carp(A,B))
eger degılse tercih == '/':
   print(A,"/",B,"=", bol(A,B))
degılse:
   yaz("Gecersız deger")
