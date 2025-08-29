SoftWare de busca e organização de produtos de um estoque.

### 1. Entendimento do Probema
- *Definição da necessidade:* O Software tem como objetivo organizar e catalogar itens de um estoque ajudando a resolver problemas de organização, compras e catalogar itens do estoque.
- *Público alvo:* Estoquistas e donos de loja, empresarios que possuam um estoque de produtos/itens.
- *Objetivo principal:* O sistema deve entregar uma aplicação de gerenciamento e logistica de um estoque, deve conter cadastros de produtos para contagem e compras.

### 2. Levantamento e Especificação de Requisitos

## Fase 2.1: O Núcles do MVP (Produto Mínimo Viável)
- *Requisitos Funcionais (RF)*:
  
RF01 - O sistema DEVE permitir que o Estoquista e o Empresário façam login com credencias (e-mail e senha).

RF02 - Cadastro de Usuário e Empresa:
- O sistema DEVE permitir o cadastro de informações pessoais do Estoquista (nome, CPF, e-mail, etc.).
- O sistema DEVE permitir o cadastro das informações da Empresa (razão social, CNPJ, endereço e nome fantasia ).
- O sistema DEVE vincular automaticamente o perfil do Estoquista à sua respectiva Empresa.

RF03 - Gerenciamento de Produtos: O sistema DEVE permitir ao Estoquista e ao Empresário realizarem as seguintes operações com itens do estoque:
- Cadastrar: Incluir novos itens (nome, descrição, quantidade, categoria, preço, Und. de medida e código).
- Atualizar:  Alterar informações de itens existentes.
- Excluir: Remover itenss do estoque.
- Consultar/Buscar: Localizar itens por nome, categoria ou código.
  
RF04 - O sistema DEVE armazenar de forma segura todas as informações de usuários, empresas e produtos em um banco de dados.



- *Requisitos Não Funcionais (RNF):*

RNF01 - *Desenpenho:* O sistema deve responder às requisições em até 3s.
- Ao criar e alterar produtos
- Cadastros e logins

RNF02 - *Disponibilidade:* O sistema deve estar disponível 99% do tempo e 24 horas por dia, 7 dias por semana.

RNF03 - *Segurança:* Todas as senhas de usuários devem ser armazenadas de forma cirtografada utilizando um algoritmo de has seguro, como Bcrypt ou Argon2.

