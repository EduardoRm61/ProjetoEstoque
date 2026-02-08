# Documentação Técnica - Projeto Estoque

## 1. Visão Geral
O **Projeto Estoque** é uma solução de Backend para gerenciamento e logística de estoques. O sistema visa atender estoquistas e empresários, permitindo o controle de produtos, categorias e perfis de acesso, facilitando a organização de compras e inventário.

## 2. Tecnologias Utilizadas

### Backend
- **Linguagem:** Python 3
- **Framework Web:** Flask (com `flask-restx`)
- **ORM:** Flask-SQLAlchemy
- **Banco de Dados:** MySQL 8.0 (via Driver `PyMySQL`)

### Infraestrutura & Ferramentas
- **Containerização:** Docker & Docker Compose
- **Gerenciamento de Dependências:** pip (`requirements.txt`)

## 3. Configuração e Instalação

### Pré-requisitos
- Docker e Docker Compose instalados.
- Python 3.x (caso opte por rodar fora do Docker).

### Como Rodar (Via Docker)
A forma recomendada de executar o projeto é utilizando o Docker Compose, que sobe tanto a API quanto o Banco de Dados MySQL automaticamente.

1. **Construir e iniciar os containers:**
   ```bash
   docker-compose up --build
   ```
   *O serviço da API estará acessível na porta `5002` e o MySQL na porta `3306`.*

2. **Verificar status:**
   A API possui healthchecks configurados no arquivo compose para garantir que o banco esteja pronto antes da aplicação iniciar.

### Configuração de Ambiente
As variáveis de ambiente são gerenciadas no `docker-compose.yml` ou podem ser exportadas localmente. As principais são:

| Variável | Descrição | Valor Padrão (Dev) |
| :--- | :--- | :--- |
| `DB_HOST` | Host do banco de dados | `db` (nome do serviço no docker) |
| `DB_PORT` | Porta do banco | `3306` |
| `DB_NAME` | Nome do banco | `Estoque` |
| `DB_USER` | Usuário do banco | `adm` |
| `DB_PASSWORD` | Senha do banco | `12345` |
| `HOST` | Interface de rede do Flask | `0.0.0.0` |
| `PORT` | Porta da aplicação | `5002` |

## 4. Arquitetura do Projeto

O projeto segue uma arquitetura modular baseada em **Blueprints** do Flask, separando responsabilidades por domínio (Empresa, Produto, Usuário).

### Estrutura de Pastas
```
ProjetoEstoque/
├── apps/
│   ├── app.py                 # Ponto de entrada da aplicação (Entrypoint)
│   ├── config.py              # Configurações do Flask e Banco de Dados
│   ├── empresa/               # Módulo de Empresa
│   │   ├── model_empresa.py   # Modelos (ORM), Exceções e Regras de Negócio
│   │   └── route_empresa.py   # Controladores e Rotas da API
│   ├── produto/               # Módulo de Produto (Em desenvolvimento)
│   ├── usuario/               # Módulo de Usuário (Em desenvolvimento)
│   └── categoria/             # Módulo de Categoria (Em desenvolvimento)
├── docker-compose.yml         # Orquestração dos containers
├── Dockerfile                 # Definição da imagem Docker da aplicação
└── requirements.txt           # Dependências do Python
```

## 5. Engenharia de Requisitos

### 5.1 Requisitos Funcionais (RF)

#### Módulo: Autenticação e Usuários
- **[RF01]** O sistema deve permitir login via e-mail e senha.
- **[RF02]** O sistema deve permitir o cadastro de Estoquistas (Nome, CPF, E-mail, Nascimento).
- **[RF05]** O Empresário deve poder aprovar ou rejeitar cadastros pendentes de estoquistas.

#### Módulo: Empresa (Implementado)
- **[RF02.1]** O sistema deve permitir o cadastro de Empresas (Razão Social, Nome Fantasia, CNPJ, Endereço).
- **[RF02.2]** Deve ser possível listar, buscar por ID, alterar e excluir empresas.

#### Módulo: Estoque e Produtos
- **[RF03]** O sistema deve permitir CRUD (Criar, Ler, Atualizar, Deletar) de itens do estoque.
    - Dados do item: Nome, descrição, quantidade, categoria, preço, und. medida, código.
- **[RF06]** O sistema deve permitir criar categorias e subcategorias de produtos.

### 5.2 Requisitos Não Funcionais (RNF)

- **[RNF01 - Desempenho]** O sistema deve processar requisições de criação e leitura em até 3 segundos.
- **[RNF02 - Disponibilidade]** O sistema deve operar em regime 24/7 com disponibilidade de 99%.
- **[RNF03 - Segurança]** Senhas devem ser armazenadas com criptografia forte (Hash).
- **[RNF04 - Dados]** A persistência deve ser feita em banco relacional (MySQL) garantindo integridade ACID.

### 5.3 Regras de Negócio (RN)
Baseado na implementação atual do módulo `Empresa`:

- **[RN01 - Obrigatoriedade]** Não é permitido cadastrar uma empresa sem: Razão Social, Nome Fantasia, Endereço e CNPJ.
- **[RN02 - Unicidade]** O ID da empresa é único e gerado automaticamente pelo banco.
- **[RN03 - Validação de Atualização]** Ao atualizar uma empresa, apenas os campos enviados serão modificados; dados omitidos mantêm seu estado atual.

## 6. Documentação da API (Endpoints)

### Recurso: Empresa
Base URL: `/empresa`

| Método | Rota | Descrição | Corpo da Requisição (JSON) |
| :--- | :--- | :--- | :--- |
| `GET` | `/empresa` | Lista todas as empresas | N/A |
| `GET` | `/empresa/<id>` | Busca empresa por ID | N/A |
| `POST` | `/empresa` | Cria uma nova empresa | `{ "razao_social": "...", "nome_fantasia": "...", "endereco": "...", "cnpj": "..." }` |
| `PUT` | `/empresa/<id>` | Atualiza dados da empresa | `{ "razao_social": "...", ... }` (Parcial) |
| `DELETE` | `/empresa/<id>` | Remove uma empresa | N/A |

### Códigos de Resposta Comuns
- `200 OK`: Sucesso na consulta ou exclusão.
- `201 Created`: Recurso criado com sucesso.
- `400 Bad Request`: Erro de validação (campos faltando).
- `500 Internal Server Error`: Erro no servidor ou banco de dados.

---
*Documentação gerada automaticamente em 08/02/2026.*
