from math import pi
print("Bem-vindo ao calculador de raio de um circulo!");
circulo = float(input("digite o raio do circulo que deseja calcular!"));
resultado = pi *(circulo**2)
print(f"{resultado:.2f}")