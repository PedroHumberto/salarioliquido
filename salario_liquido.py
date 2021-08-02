class Calculadora:
    def salario_liquido(salario):
        if salario <= 1100:
            
            sal_liq = salario - (salario * 0.075)
            return sal_liq

        if salario >= 1100.01 and salario <=2203.48:
            
            sal_liq = salario - (salario * 0.09 - 16.50)
            return sal_liq

        if salario >= 2203.49 and salario <= 3305.22:
            alq_3 = salario - (salario * 0.12 - 82.60)
            return alq_3

        if salario >= 3305.23:
            alq_3 = salario - (salario * 0.14 - 148.71)
    
    def aliquota(salario_liq):
        if salario_liq <= 1100:
            aliquota = ((salario_liq * 100) / - salario) + 100
            return aliquota

        if salario_liq >= 1100.01 and salario <=2203.48:
            aliquota = ((salario_liq * 100) / - salario) + 100
            return aliquota    
    
    def imposto_de_renda(salario):
        return




salario = float(input("Digite seu salario: "))
salario_liq = Calculadora.salario_liquido(salario)
aliquota  = Calculadora.aliquota(salario_liq)

print(f"Seu salario liquido é {salario_liq:.2f}")
print(f"A aliquota do INSS é de: {aliquota:.2f}%")
# print("Seu salario liquido é %0.2f" % salario_liq) modelo antigo
# print("Seu salario liquido é {:0.2f}".format(salario_liq))
 