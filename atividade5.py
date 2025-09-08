import os
os.system("cls")


k1= float(input("ensira o primero numero:"))
k2= float(input("digite o segundo"))


print("""1\t soma 
         2\t muteplicasao
         3\t divisao
         4\t subitrasao
      

""")


k3= int(input("digite as operasoes matematicas"))
 

 
match k3: 

  case 1:
    k4= k1 + k2  
   
  case 2:
    k4= k1 * k2 
  case 3:
    k4= k1/ k2
  case 4:
    k4= k1 - k2


print (f"{k4}")   