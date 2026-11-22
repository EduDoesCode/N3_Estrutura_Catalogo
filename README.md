# Catálogo de Jogos — Atividade N3

Projeto desenvolvido em **Python** para a disciplina de **Estrutura de Dados e Organização de Arquivos**, implementando um sistema de cadastro via terminal com persistência em JSON, pesquisa por campos de texto e ordenação por dois critérios distintos.

- **Autor:** Eduardo Cezar Dyba
- **Disciplina:** Estrutura de Dados e Organização de Arquivos

---

## Sobre o `jogos.json` de exemplo

O arquivo `jogos.json` incluído neste repositório já vem pré-populado com **8 jogos de exemplo** divididos em **4 gêneros** (2 jogos por gênero: *Plataforma*, *RPG*, *Aventura* e *Soulslike*, incluindo títulos como *The Legend of Zelda*, *Dark Souls* e *Bloodborne*) para facilitar os testes logo na primeira execução.

- Caso queira começar do zero, você pode apagar o conteúdo do `jogos.json` (deixando apenas `[]`) ou remover/alterar os registros diretamente pelas opções do menu.

---

## Requisitos atendidos

1. **Cadastro (`incluir`, `alterar`, `excluir`):** Permite adicionar novos jogos, editar informações de um jogo existente pelo `id` e excluir registros, mantendo `id` único e validando entradas numéricas.
2. **Persistência em JSON:** Os dados são carregados de `jogos.json` ao iniciar o programa e salvos automaticamente após operações de inclusão, alteração ou exclusão.
3. **Pesquisa por campos de texto:** Permite buscar registros parcialmente e sem diferenciação entre maiúsculas e minúsculas pelos campos `nome` ou `genero`.
4. **Impressão de listas ordenadas por 2 campos:** Exibe os jogos ordenados sem alterar a ordem original da lista em memória, permitindo ordenar por **Nome (A–Z)** ou por **Ano (crescente)**.

---

## Estrutura dos dados

Cada jogo é representado como um dicionário com os seguintes campos:

| Campo | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `id` | `int` | Identificador único do jogo | `4` |
| `nome` | `str` | Título do jogo | `"Dark Souls"` |
| `genero` | `str` | Gênero/categoria do jogo | `"Soulslike"` |
| `ano` | `int` | Ano de lançamento | `2011` |

---

## Como executar o programa

### Pré-requisitos
- **Python 3.x** instalado (utiliza apenas bibliotecas padrão do Python: `json` e `os`).

### Passos
1. Baixe a pasta do projeto e extraia o conteúdo na sua máquina.
2. Abra a pasta no seu editor de código e execute `python jogos.py` no terminal. Se você usa Linux ou macOs, execute `python3 jogos.py`.

---

## Como usar o menu

Ao rodar o `jogos.py`, o terminal exibe o menu principal:

- `1 - Incluir jogo`: Cadastra um novo jogo informando `id`, `nome`, `genero` e `ano`.
- `2 - Alterar jogo`: Busca pelo `id` e permite atualizar `nome`, `genero` e `ano` (pressionar `Enter` mantém o valor atual).
- `3 - Excluir jogo`: Remove o jogo correspondente ao `id` informado.
- `4 - Pesquisar jogo por Nome ou Gênero`: Filtra os jogos cujo campo escolhido contenha o termo digitado.
- `5 - Listar jogo por Nome ou Ano`: Imprime os registros ordenados alfabeticamente por `nome` ou numericamente por `ano`.
- `0 - Sair`: Garante o salvamento em `jogos.json` e encerra o programa.