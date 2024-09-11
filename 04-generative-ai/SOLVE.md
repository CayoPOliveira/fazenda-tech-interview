<!-- @format -->

# FazendaTech - Programming Challenge

## 04 - Generative AI - Solving the problem from [README.md](README.md)

### Problem 01 - Prompt Management and Adjustments

For this tasks I used
[ChatGPT to model the JSON](https://chatgpt.com/share/676b3042-603d-4f56-8080-351735693f3a) and [ChatGPT to create user prompts situations](https://chatgpt.com/share/10cc94fb-c63c-4662-b258-b6ec4d10f85d).

It is a simple task where a user will interact with the chat service to create an NF-e for the sale, as if it were their first time.

1. Select at least a few NF-e fields, but don't go overboard. Around 5 fields should be good enough.

-   CNPJ/CPF do Emitente
-   Data de Emissão
-   CNPJ/CPF do Destinatário
-   Produtos/Serviços (List whit description, quantity and unit price)
-   Valor Total da Nota

2. Create the prompt that asks the user for the necessary information to generate the NF-e.

> <h4> Por favor, forneça os seguintes dados para a geração da NF-e: </h4>
> <ul>
> <li>CNPJ/CPF do Emitente: (Informe o CNPJ ou CPF do emissor da nota)</li>
> <li>Data de Emissão: (Qual a data de emissão da nota?)</li>
> <li>CNPJ/CPF do Destinatário: (Informe o CNPJ ou CPF do destinatário)</li>
> <li>Lista de Produtos/Serviços: (Para cada item, informe a descrição, quantidade e preço unitário)</li>
> <li>Valor Total da Nota: (Informe o valor total da nota, incluindo todos os produtos/serviços e impostos)</li>

</ul>

3. The LLM Agent's output should include the parsed user input in JSON format, which could hypothetically be used to call an API to issue the NF-e.

The JSON representation will be something like:

```json
{
	"emitente": {
		"cnpj_cpf": "12345678000199"
	},
	"data_emissao": "2024-09-10",
	"destinatario": {
		"cnpj_cpf": "98765432000188"
	},
	"produtos_servicos": [
		{
			"descricao": "Produto A",
			"quantidade": 10,
			"preco_unitario": 50.0
		},
		{
			"descricao": "Produto B",
			"quantidade": 5,
			"preco_unitario": 100.0
		}
	],
	"valor_total": 750.0
}
```

A prompt can be something like this:

> Q: Bom dia, quero gerar uma nota fiscal para o CNPJ 12345678000155, a data de emissão é 11 de setembro de 2024. O destinatário é o CPF 98765432100. Os produtos são: 7 unidades de "Harry Potter e a Pedra Filosofal" a 35 reais e 12 unidades de "Percy Jackson e o Ladrão de Raios" a 20 reais. O total é 590 reais. A: { "emitente": { "cnpj_cpf": "12345678000155" }, "data_emissao": "2024-09-11", "destinatario": { "cnpj_cpf": "00098765432100" }, "produtos_servicos": [ { "descricao": "Harry Potter e a Pedra Filosofal", "quantidade": 7, "preco_unitario": 35.00 }, { "descricao": "Percy Jackson e o Ladrão de Raios", "quantidade": 12, "preco_unitario": 20.00 } ], "valor_total": 590.00 } Q: O meu CPF é 32165498700, hoje é dia 14 de setembro de 2024, a nota fiscal é para o CPF 98765432199. São 3 unidades de caneta por 2 reais, 5 unidades de caderno por 10 reais, 2 unidades de mochila por 50 reais, 1 unidade de estojo por 15 reais e 4 unidades de lápis por 1 real, dando um total de 175 reais. A: { "emitente": { "cnpj_cpf": "00032165498700" }, "data_emissao": "2024-09-14", "destinatario": { "cnpj_cpf": "00098765432199" }, "produtos_servicos": [ { "descricao": "Caneta", "quantidade": 3, "preco_unitario": 2.00 }, { "descricao": "Caderno", "quantidade": 5, "preco_unitario": 10.00 }, { "descricao": "Mochila", "quantidade": 2, "preco_unitario": 50.00 }, { "descricao": "Estojo", "quantidade": 1, "preco_unitario": 15.00 }, { "descricao": "Lápis", "quantidade": 4, "preco_unitario": 1.00 } ], "valor_total": 175.00 } Q: \<User prompt\>. A:

I performed the tests using a new chat in ChatGPT, and the responses were quite satisfactory and can be [viewed](https://chatgpt.com/share/31a09798-c59c-4acd-bb87-eeedff3ee0ca).

For testing, I also created a [notebook](https://colab.research.google.com/drive/1CQLCJv8DJ_dm7pddpQfLWiz931qv5klN?usp=sharing) that uses a free model as an example for the problem.
