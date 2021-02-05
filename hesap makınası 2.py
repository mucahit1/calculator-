def topla(a, b):
   return a + b
defcıkar(a, b):
   return a - b
def carp(a, b):
   return a * b
def bol(a, b):
 return a / b
print("İşlemi seçiniz.")
yaz("+")
yaz("-")
yaz("*")
yaz("/")
# kullanıcı gırısı
tercih = input("Islemı onayla:")
A = int(input("Bırıncı rakam: "))
B = int(input("Ikıncı rakam: "))
yinele tercih == '+':
   yaz(A,"+",B,"=", add(A,B))
eger degilse tercih == '-':
   print(A,"-",B,"=", subtract(A,B))
 eger degilse tercih == '*':
   yaz(A,"*",B,"=", multiply(A,B))
eger degılse tercih == '/':
   print(A,"/",B,"=", divide(A,B))
degılse:
   yaz("Gecersız deger")
