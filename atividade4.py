import os
os.system("cls")


print("""codigo\tfrutas\tpreço cheio\tdescoto
            1\tmaça\t2.50\t2.20
            2\tmorango\t1.80\t1.50


""")

k1= int (input("dijite produto"))
k2= int(input("quilos:"))

k4= 100

match k1:

    case 1:
        if k2 => 10
           k3= 2.20
        else:
            k3= 2.50

    case 2:
        if k2 => 10
           k3= 1.50

        else: 
            k3 = 1.80


k5= k3 * k2

if k2 => 15
    k3 = k3 * 0.1


k5= k3 * k2  

  