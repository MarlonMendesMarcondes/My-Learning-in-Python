import math
import matplotlib.pyplot as plt

a = float(input('Digite o primeiro lado do triângulo (a) : '))
b = float(input('Digite o segundo lado do triângulo (b): '))
c = float(input('Digite o terceiro lado do triângulo (c): '))

#Definição de um triângulo válido
def is_valid_triangle(a1, a2, a3):
    if a1 + a2 >= a3 and a2 + a3 >= a1 and a3 + a1 >= a2:
        return True
    else:
        return False

triangulo_valido = is_valid_triangle(a, b, c)

#Definição dos ângulos internos do triângulo
def angle(b1, b2, b3):
    return math.degrees(math.acos((b3 ** 2 - b2 ** 2 - b1 ** 2) / (-2.0 * b1 * b2)))


if triangulo_valido:
    print('O triângulo é valido!')
    A = angle(a, b, c)
    B = angle(b, c, a)
    C = angle(c, a, b)
    print('A = {:.2f}º, B = {:.2f}º, C = {:.2f}º'.format(A, B, C))

if A > 90 or B > 90 or C > 90:
    print('O triângulo é um Obtusângulo!')

elif A == 90 or B == 90 or C == 90:
    print('O triângulo é retângulo!')

else:
    print('O triângulo é um Acutângulo!')

if not triangulo_valido:
    print('O triângulo não é valido!')

if a == b == c and triangulo_valido is True:
    print('O triângulo de d lados {}, {}, {} é equilátero.'.format(a, b, c))
    h = a / 2 * math.sqrt(3)
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = a * h
    print('A Area do triângulo é: {:.2f}'.format(area))

elif a ** 2 == b ** 2 + c ** 2 and triangulo_valido is True:
    print('O triângulo é retângulo. E a é a hipotenusa')
    h = b
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = h * c
    print('A area do triângulo é: {:.2f}'.format(area))

elif a ** 2 + b ** 2 == c ** 2 and triangulo_valido is True:
    print('O triângulo é retângulo. e c é a hipotenusa')
    h = a
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = h * b
    print('A area do triângulo é: {:.2f}'.format(area))

elif b ** 2 == c ** 2 + a ** 2 and triangulo_valido is True:
    print('O triangulo é retangulo. e b é a hipotenusa')
    h = a
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = h * c
    print('A area do triângulo é: {:.2f}'.format(area))

elif a == b and triangulo_valido is True:
    print('O triângulo é simetrico por a/b.')
    h = a / 2 * math.sqrt(3)
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = c * h
    print('A Area do triângulo é: {:.2f}'.format(area))

elif a == c and triangulo_valido is True:
    print('O triângulo é simetrico por a/c.')
    h = a / 2 * math.sqrt(3)
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = b * h
    print('A Area do triângulo é: {:.2f}'.format(area))


elif c == b and triangulo_valido is True:
    print('O triângulo é simetrico por c/b')
    h = c / 2 * math.sqrt(3)
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = a * h
    print('A Area do triângulo é: {:.2f}'.format(area))

elif a != b != c and triangulo_valido is True:
    print('O triângulo é escaleno.')
    h = b * math.sqrt((math.sin(A)) ** 2)
    print('A altura do triângulo é: {:.2f}'.format(h))
    area = c * h
    print('A Area do triângulo é: {:.2f}'.format(area))

#Definição dos pontos do triângulo em um plano cartesiano
A_cartesiano = [0,0]
B_cartesiano = [c, 0]
C_cartesiano = [b * math.cos(math.radians(A)), b * math.sin(math.radians(A))]
C_carte_print = [math.trunc(C_cartesiano[0] * 100)/100, math.trunc(C_cartesiano[1]*100)/100]
print('As coordenadas dos pontos são:\nA = {}, B = {}, C = {}'.format(A_cartesiano, B_cartesiano, C_carte_print))

#Definição do baricentro
G = [c * math.tan(math.radians(B / 2)) / (math.tan(math.radians(A / 2)) + math.tan(math.radians(B / 2))),
     c * math.tan(math.radians(A / 2)) * math.tan(math.radians(B / 2)) / (math.tan(math.radians(B / 2)) + math.tan(math.radians(A / 2)))]
G_print = [math.trunc(G[0]*100)/100, math.trunc(G[1] * 100)/100]
print('O baricentro do triângulo está em:\n{}'.format(G_print))

#Definição do circulo circunscrito
#Centro do circulo
Ponto_circulo_circunscrito = [(A_cartesiano[0] + B_cartesiano[0] + C_cartesiano[0]) / 3,
                              (A_cartesiano[1] + B_cartesiano[1] + C_cartesiano[1]) / 3]
Ponto_circunscrito_print = [math.trunc(Ponto_circulo_circunscrito[0] * 100) / 100, 
                            math.trunc(Ponto_circulo_circunscrito[1] * 100) / 100]
print('O centro do circulo circunscrito está em: \n{}'.format(Ponto_circunscrito_print))
#Raio do circulo circunscrito
R = math.sqrt(Ponto_circulo_circunscrito[0] ** 2 + Ponto_circulo_circunscrito[1] ** 2)
print('O raio do circulo circunscrito é de: {:.2f}'.format(R))

#plotagem do triângulo
plt.plot([A_cartesiano[0], B_cartesiano[0], C_cartesiano[0], A_cartesiano[0]],
         [A_cartesiano[1], B_cartesiano[1], C_cartesiano[1], A_cartesiano[1]],
         scalex = 1, scaley = 1 )

plt.ylabel('y')
plt.xlabel('x')
plt.show()

