distância = float(input('Qual é a distãncia da sua viagem? '))
print(f'A distância é {distância}km')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')