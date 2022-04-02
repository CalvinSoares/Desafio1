salário = float(input('qual o salario do funcionario? '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f' quem ganhava R${salário} passa a ganhar R${novo}')