b = float(input("Digite o valor o de um dos lados do retângulo: "))

if  b > 0:
     h = float(input("Digite o valor o outro lado do retângulo:"))
     if h > 0:
         a = b * h
         print("A área do retângulo é",a,"Cm²")
     else:
         print("Erro, não existe área negativa !")
         
else:
    print("Erro, não existe área negativa !")
