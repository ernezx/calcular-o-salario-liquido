porh = input('quanto voce ganha por hora?')
horasnomes = input('quantas horas voce trabalha no mes?')
salariobruto = int(porh) * int(horasnomes)
inss = int(salariobruto) * 8 / 100
sind = int(salariobruto) * 5 / 100
ir = int(salariobruto) * 11 / 100
gastouir = int(salariobruto) - int(ir)
gastouinss = int(salariobruto) - int(inss) - int(ir)
gastousind = int(salariobruto) - int(sind) - int(inss) - int(ir) 
salarioliquido = int(salariobruto) - int(ir) - int(sind) - int(inss)
print (
'+ Salário Bruto : R$' + str(salariobruto) 
+ '- IR (11%) : R$' + str(gastouir) 
+'- INSS (8%) : R$' + str(gastouinss)
+'- Sindicato ( 5%) : R$' + str(gastousind)
+'= Salário Liquido : R$' + str(salarioliquido))



