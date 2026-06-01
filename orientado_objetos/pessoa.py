# =============================================================================
# PARADIGMA ORIENTADO A OBJETOS - Classe Base
# =============================================================================
# Uma classe é um molde que define atributos (dados) e métodos (comportamentos)
# de um tipo de objeto. Aqui definimos a classe Pessoa, que representa qualquer
# pessoa no sistema, independente do seu papel (aluno, professor, etc).
#
# Pessoa é a classe BASE (ou superclasse). Ela será herdada por Aluno.
# =============================================================================


class Pessoa:
    # ENCAPSULAMENTO:
    # Encapsulamento significa proteger os dados internos de um objeto,
    # controlando como eles são acessados ou modificados.
    # Em Python, atributos com __ (duplo underscore) são privados,
    # ou seja, não podem ser acessados diretamente de fora da classe.
    # Ex: pessoa.__nome  -> causa erro
    #     pessoa.nome    -> funciona, pois usamos o @property abaixo

    def __init__(self, nome):
        # __nome é privado. Só a própria classe pode acessá-lo diretamente.
        self.__nome = nome

    # @property transforma o método em um "getter", permitindo ler
    # o atributo privado de fora da classe com a sintaxe: objeto.nome
    @property
    def nome(self):
        return self.__nome

    # @nome.setter define como o atributo privado pode ser alterado.
    # Aqui podemos adicionar validações antes de aceitar o novo valor.
    @nome.setter
    def nome(self, valor):
        # TODO: validar se o valor é uma string não vazia antes de atribuir
        pass

    # __str__ é um método especial do Python chamado "dunder method".
    # Ele define o que é retornado quando fazemos print(objeto) ou str(objeto).
    # Isso é um exemplo de POLIMORFISMO: subclasses podem sobrescrever
    # esse método para exibir informações de formas diferentes.
    def __str__(self):
        # TODO: retornar uma representação legível da pessoa
        pass
