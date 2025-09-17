print("Bem-vindo ao calculador de peso ideal dependendo do seu sexo!");
altura = float(input("Digite a sua altura!"));
genero = input("Qual é o seu genero, h ou m?");
h = (72.7*altura)-58;
m = (62.1*altura)-44.7;
peso_ideal = int(genero == 'h') * h + int(genero == 'm') * m;
print(f"o seu peso ideal para o genero {genero} é de {peso_ideal:.2f}!");