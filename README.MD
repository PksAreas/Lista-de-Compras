
# 🛒 Shopping List (CLI)

  

Este é um projeto de gerenciamento de listas de compras via linha de comando, desenvolvido como um exercício de "auto-teste" para consolidar conhecimentos em Python e bancos de dados relacionais.

  

## 🔄 Evolução do Projeto

  

Este repositório representa a evolução de um projeto antigo que utilizava arquivos de texto plano (`.txt`) para persistência de dados.

*  **Versão Atual:** Refatoração completa utilizando **Python 3.13.9** e **SQLite3**, garantindo integridade de dados e consultas estruturadas.

  

## 🛠️ Tecnologias e Recursos

  

*  **Linguagem:** Python 3.13.9 (utilizando `match-case` e tipagem moderna).

*  **Banco de Dados:** SQLite3 (Persistência relacional).

*  **Modularização:** Separação clara entre interface (`main.py`) e lógica de dados (`functions.py`).

*  **Compatibilidade:** Uso de `os.path.join` para funcionamento multiplataforma (Windows/Linux/macOS).

  

## 📋 Funcionalidades

  

*  **Internacionalização:** Escolha entre Português e Inglês na inicialização.

*  **Gestão de Listas:** Criação de múltiplas listas independentes.

*  **CRUD de Itens:** Adição, remoção e edição (nome, quantidade ou valor) de produtos.

*  **Cálculo Automático:** Exibição do valor total somado de todos os itens da lista.

*  **Inicialização Automática:** O sistema cria as tabelas do banco de dados automaticamente na primeira execução.

  

## 🏗️ Estrutura do Banco de Dados

  

O banco de dados `shopping_list.db` é composto por duas tabelas com relacionamento 1:N:

  

| Tabela | Colunas |

| :--- | :--- |

| `list` | `id`, `list_name`, `data` |

| `products` | `id`, `name`, `value`, `amount`, `id_list` (FK) |

  

## 🚀 Como Executar

  

1. Clone este repositório.

2. Certifique-se de que a pasta `db/` exista no diretório raiz.

3. Execute o arquivo principal:

```bash

python main.py

```

  

---

Desenvolvido por **Patrick Areas** para demonstrar evolução em *Clean Code* e SQL.