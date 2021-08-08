class Calculadora:
    def salario_liquido(salario):

        if salario <= 1100:            
            sal_liq = salario - (salario * 0.075)
            return sal_liq

        elif salario >= 1100.01 and salario <=2203.48:            
            sal_liq = salario - (salario * 0.09 - 16.50)
            return sal_liq

        elif salario >= 2203.49 and salario <= 3305.22:
            sal_liq = salario - (salario * 0.12 - 82.60)
            return sal_liq

        elif salario >= 3305.23:
            sal_liq = salario - (salario * 0.14 - 148.71)
            return sal_liq

    def imposto_de_renda(salario):
        
        if salario >= 1903.99 and salario <= 2826.65:
           ir = (salario * 0.075) - 142.80 
           return ir

        elif salario >= 2826.66 and salario <= 3751.05:
            ir = (salario * 0.15) - 354.80
            return ir

        elif salario >= 3751.06 and salario <= 4664.68:
            ir = (salario * 0.225) - 636.13
            return ir
            
        elif salario >= 4664.68:
            ir = (salario * 0.275) - 869.36
            return ir
    
    def aliquota(baseINSS, salario):
        
        if baseINSS <= 1100:
            aliquota = ((baseINSS * 100) / - salario) + 100
            return aliquota

        elif baseINSS >= 1100.01 and salario <=2203.48:
            aliquota = ((baseINSS * 100) / - salario) + 100
            return aliquota

        elif baseINSS >= 2206.49 and salario <= 3305.22:
            aliquota = ((baseINSS * 100) / - salario) + 100
            return aliquota

        elif baseINSS >= 3305.23:
            aliquota= ((baseINSS * 100) / -salario) + 100
            return aliquota
    
    def vale_transporte(resp, salario):
        if resp =="s":
            desconto = salario * 0.06
            return desconto
        else:
            return 0