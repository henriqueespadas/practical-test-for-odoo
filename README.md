# Descrição Geral

Este repositório contém uma coleção de módulos desenvolvidos para a plataforma Odoo 14. Os módulos abordam diferentes aspectos do gerenciamento de negócios, desde funções de cálculo matemático até integração de e-commerce e contabilidade.

---

## Função Fibonacci em Python

### Descrição
Este projeto contém uma implementação da função Fibonacci, que retorna o n-ésimo termo da sequência de Fibonacci.

- Python 3.x

### Como Rodar
1. Clone o repositório.
2. Navegue até o diretório do projeto.
3. Execute o script em Python para ver o resultado.

\`\`\`bash
python fibonacci.py
\`\`\`

---

## E-Commerce API com Odoo

### Descrição
Este módulo implementa uma API RESTful de e-commerce no Odoo.

### Recursos
- Produto: Contém atributos como nome, preço e stock_quantity.
- Carrinho: Permite adicionar e remover produtos, calcular o total e finalizar a compra.
- Pedido: Contém informações sobre os produtos comprados e o total do pedido.

### Rotas da API
#### Produtos
- Listar Produtos: `GET /api/product`
- Criar Produto: `POST /api/product/create`

#### Carrinho
- Adicionar ao Carrinho: `POST /api/cart/add`
- Remover do Carrinho: `POST /api/cart/remove`

### Como Testar
#### Usando Postman
##### Listar Produtos
1. GET para `http://your_server_address:your_port/api/product`

##### Criar Produto
1. POST para `http://your_server_address:your_port/api/product/create`
2. Corpo da Requisição:

\`\`\`json
{
  "name": "Novo Produto",
  "price": 100.0,
  "stock_quantity": 20
}
\`\`\`

##### Adicionar ao Carrinho
1. POST para `http://your_server_address:your_port/api/cart/add`
2. Corpo da Requisição:

\`\`\`json
{
  "product_id": 1,
  "quantity": 2
}
\`\`\`

##### Remover do Carrinho
1. POST para `http://your_server_address:your_port/api/cart/remove`
2. Corpo da Requisição:

\`\`\`json
{
  "product_id": 1
}
\`\`\`

---

## Odoo Accounting Module with Currency Conversion

### Descrição
Este módulo adiciona funcionalidades para lidar com taxas de câmbio e conversão de moeda em transações contábeis no Odoo.

### Funcionalidades
- Permite o registro de taxas de câmbio.
- Adiciona lógica para converter automaticamente valores.

### Campos Adicionados
- `account.foreign.exchange.rate`: Taxas de câmbio.
- `account.move`: Lógica de conversão na função create.

### Uso
1. Navegue até as configurações e adicione novas taxas de câmbio.
2. A conversão é aplicada automaticamente ao criar um novo `account.move`.

---

## account_invoice_integration

### Descrição
O módulo é responsável pela integração de faturas do Odoo com um sistema financeiro externo.

### Campos do Modelo
- `invoice_id`: Relacionamento com a fatura no Odoo.
- `external_system_id`: ID da fatura no sistema externo.
- `status`: Status da integração.
- `response_message`: Mensagem de resposta.

### Funcionalidades
- Envio automático de dados de faturas para o sistema externo.
- Atualização automática do status e mensagem de resposta.

### Configuração
1. Ativar o modo desenvolvedor.
2. Ir em configurações, técnico, configurações do sistemas.
3. Inserir o endereço do ambiente externo em `api_endpoint`.
