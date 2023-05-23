import random
import numpy as np

#Numero de dados jogados
rolagem = int(input('Quantos dados voce quer rolar?'))
dado = np.random.randint(1,6,(rolagem,1)) 

print(dado)
   
        


