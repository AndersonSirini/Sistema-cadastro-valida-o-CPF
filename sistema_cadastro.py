from classe_cadastro import linha, busca
from validate_docbr import CPF
from classe_cadastro import Cadastro

while True:
    titulo = 'UNDER TECH'
    linha()
    print(titulo.center(40))
    linha()
    print('1 - NOVO CADASTRO')
    print('2 - VISUALIZAR CADASTRO')
    print('3 - BUSCAR CADASTRO')
    print('4 - SAIR')
    linha()

    opcao = str(input('Digite sua opção:'))

    while opcao not in '1234':
        opcao = str(input('Opção inválida. Digite uma opção:'))
    if opcao == '1':
       num = str(input('CPF:'))
       cpf = CPF()
       cpf.validate(num)
       while not cpf.validate(num):
           num = str(input('CPF inválido. Digite um CPF válido:'))
           if cpf.validate(num):
               cpf = num
               break
       nome = str(input('Nome:'))
       cadastro = Cadastro(cpf, nome)
       with open('arquivo.txt', mode='a+') as arquivo:
           arquivo.write(f'{num};{cadastro.nome}\n')

    elif opcao == '2':
        try:
            with open('arquivo.txt') as arquivo:
                leitura = arquivo.read()
                print(leitura)
        except:
            print('Arquivo não encontrado.')
            continue

    elif opcao == '3':
        busca()


    else:
        print('Saindo do sistema...')
        break
