from math import pi
print("Bem-vindo ao calculador de raio de um quadrado e dobra o resultado!");
quadrado = float(input("digite o raio do quadrado que deseja calcular!"));
resultado = (pi *(quadrado**2)) *2
print(f"{resultado:.2f}")