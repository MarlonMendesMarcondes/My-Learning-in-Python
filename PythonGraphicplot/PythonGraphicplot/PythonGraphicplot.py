import matplotlib.pyplot as plt
import numpy as np 
# O programa foi testado para funções de 1°, 2° e 3°grau  

print("Bem vindo ao graphicplot")
print("toda funcao funciona como F(x) = n.x^e + C")
print("O grau da funcao depende do numero que esta no expoente dela")
r = int(input("Insira o numero alcance da funcao(r)"))
i = int(input("Insira o intervalo da funcao (i)"))
e = float(input("Insira o numero expoente da funcao (e)"))
n = float(input("Insira o numero que multiplica o X (n)"))
n1 = float(input("Insira o numero que multiplica o X^e-1 (n1)"))
c = int(input("Insira a constante (C)"))

x1 = np.arange(-r,r,i)
plt.plot([-r*10,r*10],[0,0],'k')
plt.plot([0,0],[-r*10,r*10],'k')
plt.plot(x1,n*x1**e + n1*x1**(e-1) + c,'r--')
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')
plt.show()
