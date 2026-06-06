# =============================================================================
# PARADIGMA ORIENTADO A OBJETOS - Subclasse e Turma
# =============================================================================
# Aqui definimos duas classes:
#   - Aluno: herda de Pessoa e adiciona comportamentos específicos de um aluno
#   - Turma: agrega uma coleção de alunos e opera sobre ela
# =============================================================================

from orientado_objetos.pessoa import Pessoa


# HERANÇA:
# Ao escrever class Aluno(Pessoa), dizemos que Aluno herda de Pessoa.
# Isso significa que Aluno recebe automaticamente todos os atributos e
# métodos de Pessoa, sem precisar reescrevê-los.
# Aluno é a SUBCLASSE (ou classe filha). Pessoa é a SUPERCLASSE (classe mãe).
class Aluno(Pessoa):

    def __init__(self, nome, notas):
        # super().__init__() chama o construtor da classe mãe (Pessoa).
        # Isso garante que o atributo __nome seja inicializado corretamente
        # pela lógica que já existe em Pessoa, sem duplicar código.
        super().__init__(nome)

        # __notas é privado por encapsulamento, igual ao __nome em Pessoa.
        self.__notas = notas

    @property
    def notas(self):
        return self.__notas

    def calcular_media(self):
        """
        Calcula e retorna a média aritmética das notas do aluno.

        TRATAMENTO DE EXCEÇÕES:
        Devemos tratar o caso em que a lista de notas está vazia,
        pois dividir por zero causaria um ZeroDivisionError.
        Usamos try/except para capturar esse erro e lidar com ele
        de forma controlada, em vez de deixar o programa quebrar.
        """
        try:
            # TODO: implementar o cálculo da média
            return sum(self.__notas) / len(self.__notas)
        except ZeroDivisionError:
            # TODO: tratar o caso de lista de notas vazia
            return 0.0

    def situacao(self):
        """Retorna 'Aprovado' ou 'Reprovado' com base na média."""
        # TODO: implementar usando self.calcular_media()
        return "Aprovado" if self.calcular_media() >= 6.0 else "Reprovado"

    # POLIMORFISMO:
    # Aluno sobrescreve o __str__ que foi definido em Pessoa.
    # Quando fizermos print(aluno), Python chama este método, e não o da Pessoa.
    # Isso é polimorfismo: o mesmo método (__str__) se comporta de forma
    # diferente dependendo de qual classe o objeto pertence.
    def __str__(self):
        # TODO: retornar uma string com nome, média e situação do aluno
        return f"{self.nome} | Média: {self.calcular_media():.2f} | {self.situacao()}"


# Turma é uma classe independente que AGREGA objetos do tipo Aluno.
# Ela representa o conceito de uma turma e opera sobre sua coleção de alunos.
class Turma:

    def __init__(self):
        # Lista privada que armazena os objetos Aluno da turma.
        self.__alunos = []

    def adicionar_aluno(self, aluno):
        """
        Adiciona um objeto Aluno à turma.

        TRATAMENTO DE EXCEÇÕES:
        Devemos verificar se o argumento recebido é realmente uma instância
        de Aluno. Caso contrário, lançamos um TypeError com mensagem clara.
        """
        if not isinstance(aluno, Aluno):
            raise TypeError(f"Esperado um objeto Aluno, mas recebeu {type(aluno).__name__}.")
        self.__alunos.append(aluno)

    def media_geral(self):
        """Calcula a média geral de todos os alunos da turma."""
        # TODO: implementar
        pass

    def maior_nota(self):
        """Retorna o aluno com a maior média."""
        # TODO: implementar
        pass

    def menor_nota(self):
        """Retorna o aluno com a menor média."""
        # TODO: implementar
        pass

    def listar_ordenado(self):
        """
        Retorna a lista de alunos ordenada por média de forma decrescente.
        O método sorted() com key= permite ordenar por um atributo específico.
        """
        # TODO: implementar usando sorted() com key= e lambda ou método
        pass
