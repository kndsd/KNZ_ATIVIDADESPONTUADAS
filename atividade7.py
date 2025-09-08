import os
os.system("cls")

print ("""maça \t 10.00
""")

k1= 10.00

k2 = int(input("quantidade"))


if k2 <= 5:
    k3= (k1*k2) / 0.02
    print (f"valor:{k3}")

elif k2 <= 10:
    k3= (k1*k2) / 0.03
    print (f"valor:{k3}")


   
   
elif k2 > 5:
    k3= (k1*k2) / 0.05
    print (f"valor:{k3}") 