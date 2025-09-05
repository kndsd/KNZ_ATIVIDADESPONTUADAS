import os
os.system("cls")

a=float(input("ensira o primero numero"))
b=float(input("ensira o segundo numero"))
c=float(input("terseiro numero"))

k1= a + b

if k1 > c:
    print (f"{k1} e maior que {c}")

elif k1 < c :
    print(f"{k1} e menor que {c}")


else:
    print(f"{k1} e igual a {c}")         