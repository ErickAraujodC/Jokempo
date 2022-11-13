from time import sleep
from random import randint

print('-=-'*10)
print('     VAMOS JOGAR JOKEMPO')
print('-=-'*10)
print('''[0]  Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Faça sua jogada: '))
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
sleep(1)
print('JOOOO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POOOÔ')
print('-=-'*10)
print('Computador escolheu {}.'.format(itens[comp]))
print('Jogador escolheu {}.'.format(itens[jogador]))
print('-=-'*10)
sleep(0.3)

if comp == 0:
    if jogador == 0:
        print('EMPATE ')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif comp == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif comp == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')


