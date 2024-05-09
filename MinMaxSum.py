array = [1,2,3,4,5]
#MK 1 Codigo gambiarra
def soma(array):
    array.sort()
    soma = 0
    soma1 = 0    
    for i in range(4):
        soma += array[i]
        negativo = len(array) - 1
        soma1 += array[negativo-i]
    print(soma)    
    print(soma1)
    

soma(array)
array = [3,1,5,9,7]
soma(array)
# MK2
def minMaxSum(array):
    max = array[0]
    min = array[0]
    soma = sum(array)
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]
    print(f"soma maxima {soma-min}, soma minima {soma-max}")

minMaxSum(array)

# Mais Performatico
def minMaxSum(array):
    max = array[0]
    min = array[0]
    soma = 0
    for i in range(len(array)):
        soma += array[i]
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]
    print(f"soma maxima {soma-min}, soma minima {soma-max}")

minMaxSum(array) 