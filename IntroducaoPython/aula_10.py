"""Método => Booleanos"""


# Valores Booleanos
ativo = True
inativo = False

print(f"Ativo: {ativo}")
print(f"Inativo: {inativo}")

""" Operadores de Comparação

Igual a (==): Verifica se dois valores são iguais
"""
igual = 5 == 5
print(f"Igual (5 == 5): {igual}")

# Diferente de (!=): Verifica se dois valores são diferentes
diferente = 5 != 5
print(f"Diferente (5 != 5): {diferente}")

# Maior que (>) 
maior = 5 > 3 
print(f"5 maior que 3: {maior}")

# Menor que (<)
menor = 5 < 3
print(f"5 menor que 3: {menor}")

# Maior ou igual a (>=)
maior_igual = 5 >= 5
print(f"5 menor ou igual a 3: {maior_igual}")

# Menor ou igual a (<=)
menor_igual = 3 <= 5 
print(f"5 menor ou igual a: {menor}")

"""Operadores Lógicos

and: Retorna True se ambas as condições forem verdadeiras
"""
print(f"V e igual V: {True and True}") 
print(f"V e diferente V: {True and False}") 

# or: Retorna True se pelo menos uma das condições for verdadeira.

print(f"V ou F: {True or False}") 
print(f"F or F: {False or False}") 

# not: Inverte o valor booleano.
print(f"V nao F: {not True}") 
print(f"F nao V: {not False}") 