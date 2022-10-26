salario = int(input())
if ( salario > 0 and salario <=600 ):
    percentual_reajuste = 17
    aumento_salario = salario*(percentual_reajuste/100)
    novo_salario = salario + aumento_salario
elif(salario > 600 and salario <= 900):
    percentual_reajuste = 13
    aumento_salario = salario*(percentual_reajuste/100)
    novo_salario = salario + aumento_salario
elif ( salario >900 and salario <= 1500 ):
    percentual_reajuste = 12
    aumento_salario = salario*(percentual_reajuste/100)
    novo_salario = salario + aumento_salario
elif ( salario >1500 and salario <= 2000 ):
    percentual_reajuste = 10
    aumento_salario = salario*(percentual_reajuste/100)
    novo_salario = salario + aumento_salario
else:
    percentual_reajuste =5
    aumento_salario = salario*(percentual_reajuste/100)
    novo_salario = salario + aumento_salario
print (f'Novo salario: {novo_salario:.2f} \n Reajuste ganho: {aumento_salario:.2f} \n Em percentual: {percentual_reajuste}%')

