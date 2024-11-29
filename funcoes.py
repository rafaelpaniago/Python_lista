# Função 1 (nível básico)
# Aqui vamos somar dois números

# def soma(a, b):
#     return a + b

# # Aplicação: A função recebe dois parâmetros. Retorna a soma deles.

# resultado = soma(3, 5)
# print(resultado)

# # Função 2 (nível médio)
# # Aqui vamos verificar se o número é par ou ímpar

# def par_impar(numero):
#     if numero % 2 == 0:
#         return "Par"
#     else:
#         return "Ímpar"
    
# # Aplicação: Operção de módulo %. Verifica se é divisível por 2.

# print(par_impar(3))
# print(par_impar(2))



# Nova função

# def cadastro_pessoa(nome, idade, **informacoes):
#     pessoa = {'nome': nome, 'idade': idade}
#     pessoa.update(informacoes)
#     return pessoa

# nome = input('Digite o nome: ')
# idade = int(input('Digite a idade: '))
# cidade = input('Digite a cidade: ')
# estado = input('Digite o estado: ')
# prof = input('Digite a profissão: ')
# est_c = input('Digite o estado civil: ')

# pessoa = cadastro_pessoa(nome, idade, cidade=cidade, estado=estado, profissao=prof, estado_civil=est_c)
# print(pessoa)


# Função de cadastro

def cadastro_p(nome, **infos):
    pessoa = {'nome': nome}
    pessoa.update(infos)
    return pessoa

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
profissao = input('Digite a profissão: ')

pessoa = cadastro_p(nome = nome, idade = idade, profissao = profissao)
print(pessoa)










# Função 3

# def criar_pessoa(nome, idade, **informacoes):
#     pessoa = {'nome': nome, 'idade': idade}
#     pessoa.update(informacoes)
#     return pessoa

# # Uso
# pessoa = criar_pessoa("Ana", 30, cidade="São Paulo", profissao="Engenheira")
# print(pessoa)
# Saída: {'nome': 'Ana', 'idade': 30, 'cidade': 'São Paulo', 'profissao': 'Engenheira'}

# Explicação:

# Usa **informacoes para receber argumentos opcionais como pares chave-valor.
# Demonstra a manipulação dinâmica de dados com dicionários.



# Função 4

# def validar_dados(nome, email):
#     if not nome or not email:
#         return False, "Nome e e-mail são obrigatórios."
#     if "@" not in email:
#         return False, "E-mail inválido."
#     return True, "Dados válidos."

# def salvar_usuario(nome, email):
#     valido, mensagem = validar_dados(nome, email)
#     if valido:
#         # Simula salvar no banco de dados
#         return f"Usuário {nome} salvo com sucesso!"
#     else:
#         return f"Erro ao salvar usuário: {mensagem}"

# # Uso
# print(salvar_usuario("Ana", "ana@exemplo.com"))  # Saída: Usuário Ana salvo com sucesso!
# print(salvar_usuario("", "ana@exemplo.com"))     # Saída: Erro ao salvar usuário: Nome e e-mail são obrigatórios.

# Explicação:

# A função validar_dados verifica as regras básicas de entrada.
# A função salvar_usuario chama validar_dados antes de processar os dados.
# No Django, você usará algo semelhante para validar e salvar dados de formulários.





# Função 5

# def calcular_desconto(preco, percentual):
#     return preco - (preco * percentual / 100)

# def calcular_total_com_desconto(preco, quantidade, desconto_percentual):
#     subtotal = preco * quantidade
#     total = calcular_desconto(subtotal, desconto_percentual)
#     return total

# # Uso
# preco_unitario = 100
# quantidade = 3
# desconto = 10

# total = calcular_total_com_desconto(preco_unitario, quantidade, desconto)
# print(f"Total com desconto: R$ {total:.2f}")
# # Saída: Total com desconto: R$ 270.00


# Explicação:

# A função calcular_desconto realiza o cálculo do desconto.
# A função calcular_total_com_desconto reutiliza essa lógica para calcular o valor total, considerando a quantidade e o desconto.
# Isso reflete práticas comuns em aplicações Django, como cálculos de preços em modelos ou views.

