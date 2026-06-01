# =============================================================================
# PARADIGMA ORIENTADO A OBJETOS - Ponto de entrada
# =============================================================================
# Este arquivo orquestra a execução do paradigma OO.
# Aqui instanciamos os objetos e conectamos os comportamentos definidos
# nas classes Aluno e Turma.
# =============================================================================

from orientado_objetos.aluno import Aluno, Turma


def main():
    # Loop interno do paradigma OO.
    # Ao fim de cada execução, pergunta se o usuário quer rodar novamente.
    # Se não, retorna ao menu principal (encerra essa função).
    while True:

        # Instanciando um objeto do tipo Turma.
        # 'turma' é um objeto: uma instância concreta da classe Turma.
        turma = Turma()

        # TODO: ler dados dos alunos via input e adicionar à turma
        # Exemplo do que será feito aqui:
        #   aluno = Aluno(nome, notas)  <- instancia um objeto Aluno
        #   turma.adicionar_aluno(aluno) <- chama método da Turma

        # TODO: exibir lista ordenada usando turma.listar_ordenado()

        # TODO: exibir estatísticas usando turma.media_geral(),
        #       turma.maior_nota(), turma.menor_nota()

        resposta = input("\nDeseja executar novamente? [s/n]: ").strip().lower()
        if resposta != "s":
            break
