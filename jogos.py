import json
import os

ARQUIVO_JSON = "jogos.json"

# 6 - 21: Persistência
def carregar_json(caminho=ARQUIVO_JSON):
    if not os.path.exists(caminho):
        return []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        print("Arquivo JSON inválido ou inacessível. Iniciando lista vazia.")
        return []

def salvar_json(jogos, caminho=ARQUIVO_JSON):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(jogos, arquivo, ensure_ascii=False, indent=4)

# Busca por ID
def buscar_por_id(jogos, jogo_id):
    for jogo in jogos:
        if jogo["id"] == jogo_id:
            return jogo
    return None

# Cadastrar jogo
def incluir_jogo(jogos):
    try:
        jogo_id = int(input("ID do jogo: "))
    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")
        return

    if buscar_por_id(jogos, jogo_id) is not None:
        print("Erro: já existe um jogo cadastrado com esse ID.")
        return

    nome = input("Nome do jogo: ").strip()
    genero = input("Gênero (ex: Soulslike, Aventura, RPG): ").strip()

    try:
        ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("Erro: o ano deve ser um número inteiro.")
        return

    if not nome or not genero:
        print("Erro: nome e gênero não podem ficar vazios.")
        return

    novo_jogo = {
        "id": jogo_id,
        "nome": nome,
        "genero": genero,
        "ano": ano,
    }
    jogos.append(novo_jogo)
    salvar_json(jogos)
    print("Jogo incluído com sucesso!")

# Editar jogo pelo ID
def alterar_jogo(jogos):
    try:
        jogo_id = int(input("Digite o ID do jogo que deseja alterar: "))
    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")
        return

    jogo = buscar_por_id(jogos, jogo_id)
    if jogo is None:
        print("Jogo não encontrado.")
        return

    print(f"Editando: {jogo['nome']} ({jogo['ano']}) - {jogo['genero']}")
    print("(Pressione Enter para manter o valor atual)")

    novo_nome = input(f"Novo nome [{jogo['nome']}]: ").strip()
    novo_genero = input(f"Novo gênero [{jogo['genero']}]: ").strip()
    novo_ano_str = input(f"Novo ano [{jogo['ano']}]: ").strip()

    if novo_nome:
        jogo["nome"] = novo_nome
    if novo_genero:
        jogo["genero"] = novo_genero
    if novo_ano_str:
        try:
            jogo["ano"] = int(novo_ano_str)
        except ValueError:
            print("Aviso: ano inválido, mantendo o ano anterior.")

    salvar_json(jogos)
    print("Jogo alterado com sucesso!")

# Exclui jogo pelo ID
def excluir_jogo(jogos):
    try:
        jogo_id = int(input("Digite o ID do jogo que deseja excluir: "))
    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")
        return

    jogo = buscar_por_id(jogos, jogo_id)
    if jogo is None:
        print("Jogo não encontrado.")
        return

    jogos.remove(jogo)
    salvar_json(jogos)
    print(f"Jogo '{jogo['nome']}' excluído com sucesso!")

# Mostra os jogos no terminal
def exibir_jogos(jogos):
    if not jogos:
        print("\nNenhum jogo encontrado para exibir.")
        return

    print("\n" + "-" * 65)
    print(f"{'ID':<5} | {'NOME':<30} | {'GÊNERO':<15} | {'ANO':<4}")
    print("-" * 65)
    for jogo in jogos:
        print(
            f"{jogo['id']:<5} | "
            f"{jogo['nome'][:30]:<30} | "
            f"{jogo['genero'][:15]:<15} | "
            f"{jogo['ano']:<4}"
        )
    print("-" * 65)

# Pesquisa por nome ou gênero
def pesquisar_por_texto(jogos):
    print("\nPesquisar por qual campo?")
    print("1 - Nome")
    print("2 - Gênero")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        campo = "nome"
    elif opcao == "2":
        campo = "genero"
    else:
        print("Opção de campo inválida.")
        return

    termo = input(f"Digite o texto para buscar em {campo}: ").strip().lower()
    if not termo:
        print("Digite pelo menos um caractere para pesquisar.")
        return

    resultados = [jogo for jogo in jogos if termo in jogo[campo].lower()]
    print(f"\nResultados da pesquisa em '{campo}' por '{termo}': {len(resultados)} encontrado(s)")
    exibir_jogos(resultados)

# Mostra os jogos ordenados por nome ou ano
def listar_ordenado(jogos):
    if not jogos:
        print("\nNenhum jogo cadastrado ainda.")
        return

    print("\nOrdenar lista por qual campo?")
    print("1 - Nome (A-Z)")
    print("2 - Ano (mais antigo para o mais recente)")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        ordenados = sorted(jogos, key=lambda jogo: jogo["nome"].lower())
        print("\nLista ordenada por NOME:")
    elif opcao == "2":
        ordenados = sorted(jogos, key=lambda jogo: jogo["ano"])
        print("\nLista ordenada por ANO:")
    else:
        print("Opção de ordenação inválida.")
        return

    exibir_jogos(ordenados)

def exibir_menu():
    print("\n================ CATÁLOGO DE JOGOS ================")
    print("1 - Incluir jogo")
    print("2 - Alterar jogo")
    print("3 - Excluir jogo")
    print("4 - Pesquisar jogo por Nome ou Gênero")
    print("5 - Listar jogo por Nome ou Ano")
    print("0 - Sair")
    print("=====================================================")


def main():
    jogos = carregar_json()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            incluir_jogo(jogos)
        elif opcao == "2":
            alterar_jogo(jogos)
        elif opcao == "3":
            excluir_jogo(jogos)
        elif opcao == "4":
            pesquisar_por_texto(jogos)
        elif opcao == "5":
            listar_ordenado(jogos)
        elif opcao == "0":
            salvar_json(jogos)
            print("Dados salvos.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()