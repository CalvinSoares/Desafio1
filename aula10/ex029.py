velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Multado! voce excedeu o limite.')
    multa = (velocidade - 80) * 7
    print(f'voce deve pagar uma multa de R${multa}')
print('tenha um bom dia!')