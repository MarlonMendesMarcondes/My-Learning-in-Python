import matplotlib.pyplot as plt

print("Para iniciar a função coloque o valor de n e do C como mostra o exemplo a baixo")
print("Y =nX + C")
n = int(input("insira"))

def função(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(4,5,8,7,9)
