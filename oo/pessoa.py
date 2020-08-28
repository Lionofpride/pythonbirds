class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    del moreira.filhos
    moreira.olhos = 1
    del moreira.olhos
    print(levon.__dict__)
    print(moreira.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(moreira.olhos)
    print(levon.olhos)
    print(id(Pessoa.olhos), id(moreira.olhos), id(levon.olhos))
    print(Pessoa.metodo_estatico(), levon.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), levon.nome_e_atributo_de_classe())

