# Função 1 (nível básico)
# Aqui vamos somar dois números

def soma(a, b):
    return a + b

# Aplicação: A função recebe dois parâmetros. Retorna a soma deles.

resultado = soma(3, 5)
print(resultado)

# Função 2 (nível médio)
# Aqui vamos verificar se o número é par ou ímpar

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
# Aplicação: Operção de módulo %. Verifica se é divisível por 2.

print(par_impar(3))
print(par_impar(2))