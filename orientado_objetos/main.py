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

        n = int(input("Quantos alunos deseja cadastrar? "))
        for _ in range(n):
            nome = input("Nome do aluno: ").strip()
            notas_str = input(f"Notas de {nome} (separadas por espaco): ").split()
            notas = [float(nota) for nota in notas_str]
            aluno = Aluno(nome, notas)
            turma.adicionar_aluno(aluno)

        # TODO: exibir lista ordenada usando turma.listar_ordenado()
        print("\n" + "="*40)
        print("LISTAGEM ORDENADA DA TURMA (POO)")
        print("="*40)
        for aluno in turma.listar_ordenado():
            print(aluno)
        print("="*40)

        # TODO: exibir estatísticas usando turma.media_geral(),
        #       turma.maior_nota(), turma.menor_nota()
        print("\n" + "="*40)
        print("ESTATISTICAS DA TURMA (POO)")
        print("="*40)
        print(f"Média geral: {turma.media_geral():.2f}")
        print(f"Maior nota:  {turma.maior_nota()}")
        print(f"Menor nota:  {turma.menor_nota()}")
        print("="*40)

        resposta = input("\nDeseja executar novamente? [s/n]: ").strip().lower()
        if resposta != "s":
            break
