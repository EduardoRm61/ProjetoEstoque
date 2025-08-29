SoftWare de busca e organização de produtos de um estoque.

# 1. Entendimento do Probema
- *Definição da necessidade:* O Software tem como objetivo organizar e catalogar itens de um estoque ajudando a resolver problemas de organização, compras e catalogar itens do estoque.
- *Público alvo:* Estoquistas e donos de loja, empresarios que possuam um estoque de produtos/itens.
- *Objetivo principal:* O sistema deve entregar uma aplicação de gerenciamento e logistica de um estoque, deve conter cadastros de produtos para contagem e compras.

## 2. Levantamento e Especificação de Requisitos

### Fase 2.1: __O Núcles do MVP (Produto Mínimo Viável)__
- *Requisitos Funcionais (RF)*:
  
RF01 - O sistema __DEVE__ permitir que o Estoquista e o Empresário façam login com credencias (e-mail e senha).

RF02 - Cadastro de Usuário e Empresa:
- O sistema __DEVE__ permitir o cadastro de informações pessoais do Estoquista (nome, CPF, e-mail, etc.).
- O sistema __DEVE__ permitir o cadastro das informações da Empresa (razão social, CNPJ, endereço e nome fantasia ).
- O sistema __DEVE__ vincular automaticamente o perfil do Estoquista à sua respectiva Empresa.

RF03 - Gerenciamento de Produtos: O sistema __DEVE__ permitir ao Estoquista e ao Empresário realizarem as seguintes operações com itens do estoque:
- __Cadastrar__: Incluir novos itens (nome, descrição, quantidade, categoria, preço, Und. de medida e código).
- __Atualizar__:  Alterar informações de itens existentes.
- __Excluir__: Remover itenss do estoque.
- __Consultar/Buscar__: Localizar itens por nome, categoria ou código.
  
RF04 - O sistema __DEVE__ armazenar de forma segura todas as informações de usuários, empresas e produtos em um banco de dados.

###Fase 3: __Requisitos Não Funcionais (RNF)__:

RNF01 - __Desenpenho__: O sistema deve responder às requisições em até 3s.
- Ao criar e alterar produtos
- Cadastros e logins

RNF02 - __Disponibilidade__: O sistema deve estar disponível 99% do tempo e 24 horas por dia, 7 dias por semana.

RNF03 - __Segurança__: Todas as senhas de usuários devem ser armazenadas de forma cirtografada utilizando um algoritmo de has seguro, como Bcrypt ou Argon2.

