# =============================================================================
# PARADIGMA FUNCIONAL / DECLARATIVO
# =============================================================================
# No paradigma funcional, o programa é construído a partir de funções puras
# que recebem dados, processam e retornam resultados, sem modificar nada
# fora do seu escopo. Não existem classes, objetos ou estado compartilhado.
#
# Conceitos demonstrados aqui:
#   - Funções puras: sem efeitos colaterais, mesmo input = mesmo output
#   - Lambda: funções anônimas definidas em uma única linha
#   - map: aplica uma função a cada elemento de uma lista
#   - filter: filtra elementos de uma lista com base em uma condição
#   - reduce: reduz uma lista a um único valor acumulado
#   - Recursão: uma função que chama a si mesma para resolver um problema
# =============================================================================

from functools import reduce


# LAMBDA:
# Lambda é uma função anônima definida em uma única linha.
# Sintaxe: lambda parametros: expressao
# Aqui usamos lambdas para definir regras simples de negócio de forma concisa.

# Define o critério de aprovação como uma função pura.
# Recebe uma média e retorna True se aprovado, False se não.
aprovado = lambda media: media >= 6.0

# Usa a lambda 'aprovado' para retornar o texto da situação.
situacao = lambda media: "Aprovado" if aprovado(media) else "Reprovado"


# RECURSÃO:
# Uma função recursiva é aquela que chama a si mesma para resolver
# um problema menor, até atingir um caso base que encerra as chamadas.
# Aqui calculamos a média sem usar loops (for/while), só recursão.
def media_recursiva(notas, acumulado=0, indice=0):
    """
    Calcula a média de forma recursiva.
    Caso base: quando o índice chega ao fim da lista, retorna o acumulado
    dividido pelo total de notas.
    Caso recursivo: soma a nota atual ao acumulado e avança o índice.
    """
    # TODO: implementar o caso base (indice == len(notas))
    # TODO: implementar o caso recursivo
    pass


# MAP:
# map(funcao, lista) aplica a função a cada elemento da lista
# e retorna um iterador com os resultados.
# Usamos map para calcular média e situação de todos os alunos de uma vez,
# sem precisar de um loop explícito.
def processar_alunos(alunos):
    """
    Recebe lista de dicionários com nome e notas.
    Retorna nova lista com nome, média e situação de cada aluno.
    Usa map para transformar cada aluno sem modificar a lista original.
    """
    # TODO: usar map com lambda para calcular média e situação de cada aluno
    pass


# FILTER:
# filter(funcao, lista) retorna apenas os elementos para os quais
# a função retorna True.
def filtrar_aprovados(alunos_processados):
    """Usa filter para retornar somente os alunos aprovados."""
    # TODO: usar filter com lambda aprovado
    pass


def filtrar_reprovados(alunos_processados):
    """Usa filter para retornar somente os alunos reprovados."""
    # TODO: usar filter com lambda
    pass


# REDUCE:
# reduce(funcao, lista) aplica a função acumulativamente sobre a lista,
# reduzindo-a a um único valor.
# Exemplo: reduce(lambda a, b: a + b, [1,2,3]) -> ((1+2)+3) -> 6
def media_geral(alunos_processados):
    """Usa reduce para somar todas as médias e calcular a média geral."""
    # TODO: implementar com reduce
    pass


def maior_nota(alunos_processados):
    """Usa reduce para encontrar o aluno com a maior média."""
    # TODO: implementar com reduce
    pass


def menor_nota(alunos_processados):
    """Usa reduce para encontrar o aluno com a menor média."""
    # TODO: implementar com reduce
    pass


def ordenar_por_media(alunos_processados):
    """
    Usa sorted() com lambda como chave de ordenação.
    sorted() não modifica a lista original, retorna uma nova lista ordenada.
    Isso é uma característica funcional: imutabilidade dos dados originais.
    """
    # TODO: usar sorted() com key=lambda e reverse=True
    pass


def main():
    # Loop interno do paradigma funcional.
    # Ao fim de cada execução, pergunta se o usuário quer rodar novamente.
    # Se não, retorna ao menu principal (encerra essa função).
    while True:
        alunos = []
        n = int(input("Quantos alunos deseja cadastrar? "))
        for _ in range(n):
            nome = input("Nome do aluno: ").strip()
            notas_str = input(f"Notas de {nome} (separadas por espaco): ").split()
            notas = [float(nota) for nota in notas_str]
            alunos.append({"nome": nome, "notas": notas})

        # TODO: chamar processar_alunos()
        # TODO: chamar ordenar_por_media() e exibir resultado
        # TODO: chamar media_geral(), maior_nota(), menor_nota() e exibir

        resposta = input("\nDeseja executar novamente? [s/n]: ").strip().lower()
        if resposta != "s":
            break
