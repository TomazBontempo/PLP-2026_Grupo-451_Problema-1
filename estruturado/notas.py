# =============================================================================
# PARADIGMA ESTRUTURADO
# =============================================================================
# No paradigma estruturado, o programa é dividido em funções independentes,
# cada uma responsável por uma tarefa específica. Não existem classes ou
# objetos: os dados são passados diretamente entre as funções como argumentos.
#
# Conceitos demonstrados aqui:
#   - Modularização: cada responsabilidade em sua própria função
#   - Funções/procedimentos: blocos reutilizáveis de código
#   - Separação lógica: entrada, processamento e saída bem definidos
#   - Legibilidade: nomes claros e comentários explicativos
# =============================================================================


def ler_alunos():
    """
    ENTRADA DE DADOS.
    Responsável por interagir com o usuário e coletar nome e notas.
    Retorna uma lista de dicionários, onde cada dicionário representa um aluno.

    Exemplo de retorno:
        [{"nome": "Ana", "notas": [8.0, 7.5, 9.0]}, ...]

    No paradigma estruturado, usamos dicionários simples no lugar de objetos
    para armazenar dados relacionados.
    """
    pass


def calcular_media(notas):
    """
    PROCESSAMENTO - cálculo individual.
    Recebe uma lista de notas e retorna a média aritmética.

    Esta função é um exemplo de modularização: ela faz uma única coisa
    e pode ser reutilizada em qualquer parte do programa.
    """
    pass


def determinar_situacao(media):
    """
    PROCESSAMENTO - regra de negócio.
    Recebe a média e retorna 'Aprovado' ou 'Reprovado'.

    Separar essa regra em uma função própria facilita a manutenção:
    se o critério de aprovação mudar, alteramos só aqui.
    """
    pass


def calcular_estatisticas(alunos):
    """
    PROCESSAMENTO - estatísticas gerais.
    Recebe a lista completa de alunos e calcula:
        - média geral da turma
        - maior nota
        - menor nota
    Retorna os três valores.
    """
    pass


def exibir_lista_ordenada(alunos):
    """
    SAÍDA DE DADOS.
    Exibe a lista de alunos ordenada por média de forma decrescente.

    Separar a saída em uma função própria é boa prática no paradigma
    estruturado: o restante do programa não precisa saber como os dados
    são exibidos, só chama essa função.
    """
    pass


def main():
    # Loop interno do paradigma estruturado.
    # Ao fim de cada execução, pergunta se o usuário quer rodar novamente.
    # Se não, retorna ao menu principal (encerra essa função).
    while True:
        alunos = ler_alunos()
        exibir_lista_ordenada(alunos)
        calcular_estatisticas(alunos)

        resposta = input("\nDeseja executar novamente? [s/n]: ").strip().lower()
        if resposta != "s":
            break
