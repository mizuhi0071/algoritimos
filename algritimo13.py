print("calculador de salario mensal com descontos");
valor = float(input("Qual o valor recebido por horas trabalhadas?: "))
horas = float(input("Quantas horas foram trabalhadas no mês?: "))
resultado_bruto = valor*horas
imposto = (resultado_bruto*11/100);
inss = (resultado_bruto*8/100);
sindicato = (resultado_bruto*5/100);
liquido = (resultado_bruto - imposto - inss - sindicato)
print(f" + Salário Bruto : R${resultado_bruto}\n - IR (11%) : R${imposto}\n - INSS (8%) :R$ {inss}\n - Sindicato ( 5%) : R${sindicato}\n = Salário Liquido : R${liquido}.")

