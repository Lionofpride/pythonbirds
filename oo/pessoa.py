class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    levon = Pessoa(nome='Levon')
    moreira = Pessoa(levon, nome='Moreira')
    print(Pessoa.cumprimentar(moreira))
    print(id(moreira))
    print(moreira.cumprimentar())
    print(moreira.nome)
    print(moreira.idade)
    for filho in moreira.filhos:
        print(filho.nome)
    moreira.sobrenome = 'Azevedo'
    del moreira.sobrenome
    print(moreira.__dict__)
    print(levon.__dict__)

