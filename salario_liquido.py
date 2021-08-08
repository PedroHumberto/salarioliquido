from calculadora import Calculadora



salario = float(input("Digite seu salario: "))
resp = input("Desconta Vale Transporte? Sim (s) ou Não (n): ")
baseINSS = Calculadora.salario_liquido(salario)
salario_liq = Calculadora.salario_liquido(salario) - Calculadora.imposto_de_renda(salario) - Calculadora.vale_transporte(resp, salario)
aliquota  = Calculadora.aliquota(baseINSS,salario)

print(f"A aliquota do INSS é de: {aliquota:.4f}%")
print(f'O valor do seu IR é de {Calculadora.imposto_de_renda(salario):.2f}')
if resp == "s":
    print(f"Seu V.T é de: {Calculadora.vale_transporte(resp, salario)}")
else:
    
    print(f"Seu salario liquido é {salario_liq:.2f}")

# print("Seu salario liquido é %0.2f" % salario_liq) modelo antigo
# print("Seu salario liquido é {:0.2f}".format(salario_liq))
 