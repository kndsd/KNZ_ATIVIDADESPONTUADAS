import os
os.system("cls")

print("""combustivel\tquantidade\tdescomto
      1\t alcool\t<25\t 10%
         alcool\t>26\t 20%
      2\tgasolina\t25<\t 15%
         gasolina\t>25\t30
""")

k1= int(input("escolha o produto:"))
k2= int(input("quantidade:"))

match k1:
    case 1 :
        g=6.59
        if k2 <= 25:
            k4= (g*k2) / 0.1

        elif k2 >= 25:
            k4= (g*k2) / 0.2



    
    case 2:
        g=3.75
        if k2 >= 25:
         k4= (g*k2) / 0.15     
        elif k2  >= 25:
         k4 = (g*k2) / 0.3


print(f"valor final:{k4}")         