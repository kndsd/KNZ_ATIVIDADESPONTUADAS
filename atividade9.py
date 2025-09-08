import os
os.system("cls")

renda=float(input("salario:"))

valor=float(input("valor pidido"))

parse=float(input("parselas"))
                  

if valor <=10 * renda and valor / parse <= 0.3 * renda :
  print("aprovado")


else: 
    print ("!!!!!!negadp!!!!!")                    
