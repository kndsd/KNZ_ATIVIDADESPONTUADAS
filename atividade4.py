import os
os.system("cls")


print("""codigo\tfrutas\tpreço cheio\tdescoto
            1\tmaça\t2.50\t2.20
            2\tmorango\t1.80\t1.50


""")

k1= int (input("dijite produto"))
k2= int(input("quilos:"))




match k1:

    case 1:
        k6=("maça")
        if k2 >= 10:
           k3= 2.20
           

        else:
            k3= 2.50

    case 2:
        k6=("morango")   
        if k2 >= 10:
           k3= 1.50

        else: 
            k3 = 1.80



if k2 >= 15:
    k4 = k3 * 0.1
    k5 = k4 * k2
    print(f"voce comprou {k2} kilos de {k6} preço total é {k5}")

  
