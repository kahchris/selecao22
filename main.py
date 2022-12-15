print(" olá usuario, veja a seguir as seleções que participaram da Copa\n")

x = ['Brasil', 'Portugal', ' Catar', 'Coreia', 'Argentina']
print(x)

escolha = int(input('\nApos ver algumas das seleções, gostaria que nossosistema adicionasse mais alguma seleção?\n1-simn\n2-nao\n'))

if escolha == 1:
  x.insert(0, 'França')
  print(x)
  print('*França foi inserido com sucesso*')

if escolha== 2:
  print('Ok, continuaremos com a mesma lista de seleção:\n')
  print(x)

retirar=int(input('gostaria de remover alguma seleção da\ lista?\n1-sim\n2-nao\n'))

if retirar== 1:
  slc=input('qual a seleção que deseja remover?')

if retirar==  2:
  print(x)
