import estruturado.notas as estruturado
import orientado_objetos.main as oo
import funcional.notas as funcional


def exibir_menu():
    print("\n" + "=" * 40)
    print("  Sistema de Notas e Médias de Alunos")
    print("=" * 40)
    print("[1] Paradigma Estruturado")
    print("[2] Paradigma Orientado a Objetos")
    print("[3] Paradigma Funcional")
    print("[0] Sair")
    print("=" * 40)


def main():
    # Loop principal do menu. Fica rodando até o usuário escolher sair.
    # Sem esse loop, o programa encerraria logo após a primeira escolha.
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        match opcao:
            case "1":
                estruturado.main()
            case "2":
                oo.main()
            case "3":
                funcional.main()
            case "0":
                print("\nEncerrando o programa. Até mais!")
                break
            case _:
                print("\nOpcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
