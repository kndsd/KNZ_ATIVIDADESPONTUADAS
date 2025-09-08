import os
os.system("cls")

k1=float(input("digite uma nota:"))
k2=float(input("digite uma nota:"))



k4= k1 + k2 

k5= k4 / 2

print(f"media:{k5}")

if k5 >= 6 :
  print("aprovado")

elif 4.1 >=  k5 <= 5.9:

    print("recuperacao")

else:
   print ("perovado")

print(f"nota:{k5}")   
