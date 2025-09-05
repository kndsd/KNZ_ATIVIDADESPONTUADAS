import os
os.system("cls")

nome = input("escreva seu nome:")
sexo= int(input("escreva seu sexo 1 para masculino e 2 para feminino:"))

k1=int(input("digite 3 para casado e 4 para solteiro"))

      

if sexo == 1:
     k3= ("masculino")


else:
       k3=("feminino") 


if k1==3:
    k2=int(input("digite quantos anos de casado voce tem:"))
    k4=("casado")
else:
     ("soltero")





print(f"seu nome{nome}")

print(f"seu sexo {k3}")

print (f"estado civil {k4} a {k2}")


