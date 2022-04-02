# Desafio1

13 lines (13 sloc)  377 Bytes
   
from random import randint
from time import sleep
computador = randint(0,10)
print('-=-' * 15)
print('vou pensar em um número de 0 a 10')
print('-=-' * 15)
jogador = int(input('em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('parabens vc acertou')
else:
    print(f'ganhei! voce escolheu {jogador} e eu escolhi {computador}')
