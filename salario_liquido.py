class Calculadora:
    def salario_liquido (salario):
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




salario = float(input("Digite seu salario: "))
salario_liq = Calculadora.salario_liquido(salario)

print("Seu salario liquido é", salario_liq)
 