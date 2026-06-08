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
    if indice == len(notas):
        return acumulado / len(notas) if notas else 0.0
    return media_recursiva(notas, acumulado + notas[indice], indice + 1)


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
   
    return list(map(
        lambda a: {
            "nome": a["nome"],
            "media": media_recursiva(a["notas"]),
            "situacao": situacao(media_recursiva(a["notas"]))
        }, 
        alunos
    ))    



# FILTER:
# filter(funcao, lista) retorna apenas os elementos para os quais
# a função retorna True.
def filtrar_aprovados(alunos_processados):
    """Usa filter para retornar somente os alunos aprovados."""
    return list(filter(lambda a: aprovado(a["media"]), alunos_processados))


def filtrar_reprovados(alunos_processados):
    """Usa filter para retornar somente os alunos reprovados."""
    return list(filter(lambda a: not aprovado(a["media"]), alunos_processados))


# REDUCE:
# reduce(funcao, lista) aplica a função acumulativamente sobre a lista,
# reduzindo-a a um único valor.
# Exemplo: reduce(lambda a, b: a + b, [1,2,3]) -> ((1+2)+3) -> 6
def media_geral(alunos_processados):
    """Usa reduce para somar todas as médias e calcular a média geral."""
    if not alunos_processados: return 0.0
    soma = reduce(lambda acc, aluno: acc + aluno["media"], alunos_processados, 0.0)
    return soma / len(alunos_processados)


def maior_nota(alunos_processados):
    """Usa reduce para encontrar o aluno com a maior média."""
    if not alunos_processados: return None
    return reduce(lambda a, b: a if a["media"] >= b["media"] else b, alunos_processados)


def menor_nota(alunos_processados):
    """Usa reduce para encontrar o aluno com a menor média."""
    if not alunos_processados: return None
    return reduce(lambda a, b: a if a["media"] < b["media"] else b, alunos_processados)


def ordenar_por_media(alunos_processados):
    """
    Usa sorted() com lambda como chave de ordenação.
    sorted() não modifica a lista original, retorna uma nova lista ordenada.
    Isso é uma característica funcional: imutabilidade dos dados originais.
    """
    return sorted(alunos_processados, key=lambda a: a["media"], reverse=True)


def exibir_lista_ordenada(alunos_ordenados):
    """
    Função dedicada apenas à exibição (I/O).
    Usa map para formatar as strings de saída.
    """
    print("\n" + "="*40)
    print("LISTAGEM ORDENADA DA TURMA (FUNCIONAL)")
    print("="*40)
    
    # Usa map para criar uma lista de strings formatadas
    strings_formatadas = list(map(
        lambda a: f"{a['nome']} | Média: {a['media']:.2f} | {a['situacao']}",
        alunos_ordenados
    ))
    
    # Imprime tudo juntando as strings (sem loop for)
    print("\n".join(strings_formatadas))
    print("="*40)


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

        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            # 1. Processamento puramente funcional (Membro 4)
            alunos_processados = processar_alunos(alunos)
            
            # 2. Ordenação funcional (Membro 4)
            alunos_ordenados = ordenar_por_media(alunos_processados)
            
            # 3. Exibição (Membro 4)
            exibir_lista_ordenada(alunos_ordenados)

            # 4. Estatísticas usando Reduce e Filter
            m_geral = media_geral(alunos_processados)
            melhor = maior_nota(alunos_processados)
            pior = menor_nota(alunos_processados)
            aprovados = filtrar_aprovados(alunos_processados)
            reprovados = filtrar_reprovados(alunos_processados)

            print("\n" + "="*40)
            print("ESTATISTICAS DA TURMA (FUNCIONAL)")
            print("="*40)
            print(f"Média geral: {m_geral:.2f}")
            print(f"Maior média: {melhor['nome']} ({melhor['media']:.2f})")
            print(f"Menor média: {pior['nome']} ({pior['media']:.2f})")
            print("="*40)

        resposta = input("\nDeseja executar novamente? [s/n]: ").strip().lower()
        if resposta != "s":
            break

if __name__ == "__main__":
    main()
