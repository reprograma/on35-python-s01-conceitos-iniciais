salario_hora = float(input("Informe seu salário por hora "))
horas_trabalhadas_mes = float(input("Informe as horas trabalhadas no mês "))
salario_bruto = salario_hora*horas_trabalhadas_mes
print(f"Seu salário bruto é {salario_bruto}")

desconto_ir = float(salario_bruto*0.11)
print(f"Seu desconto de Imposto de Renda é {desconto_ir}")

desconto_inss = float(salario_bruto*0.08)
print(f"Seu desconto de INSS é {desconto_inss}")

desconto_sindicato = float(salario_bruto*0.05)
print(f"Seu desconto do sindicato é {desconto_sindicato}" )

salario_liquido = salario_bruto-desconto_ir-desconto_inss-desconto_sindicato
print(f"Seu salário líquido é {salario_liquido}")


