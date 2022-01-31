class Cadastro:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def cadastrar(arquivo, nome, cpf):
        with open('arquivo.txt', mode='a+') as arquivo:
            arquivo.write(f'{cpf};{nome}\n')

def linha():
    print('-'*40)

def busca():
    search = str(input('Pesquisar por:'))
    with open('arquivo.txt','r') as arquivo:
        flag = 0
        index = 0
        for linha in arquivo:
            index += 1
            if search in linha:
                flag = 1
                break
        if flag == 0:
            print(f'CPF/Nome {search} não encontrado')
        else:
            print(f'{search} encontrado na linha {index}')
            with open('arquivo.txt','r') as arquivo:
                print(arquivo.readlines()[index-1])




