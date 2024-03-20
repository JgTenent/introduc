jogador = {}
jogador['nome']= input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?' ))
gols = list()
reserva = totgols = 0
for c in range(0,partidas):
	reserva = int(input(f'Quantos gols na partida {c+1}? '))
	gols.append(reserva)
	totgols = totgols + reserva
print('-='*30)
for p, g in enumerate(gols):
	print(f'Na partida {g+1} fez: {g} gols ')
print('-='*30)
print(f'{jogador["nome"]} fez {totgols} gols ')
