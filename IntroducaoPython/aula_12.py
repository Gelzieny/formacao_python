"""Lista => Principais métodos"""

# Declaração de uma lista
misturada = [1, 2, 3, 4, 5, "texto", False, True]

# Modificação de elementos da lista
misturada[0] = 'Python'
print(f"Minha lista de exemplo: {misturada}")

""" Métodos de Listas 

# append(elemento): Adiciona um elemento ao final da lista.
"""

misturada.append(6)
print(f"Apos append(6): {misturada}")

# index(elemento): Retorna o índice da primeira ocorrência de um elemento.
indice = misturada.index(6)
print(f"Index do elemento 6: {indice}")

# insert(posição, elemento): Insere um elemento em uma posição específica.
misturada.insert(2, "morango")
print(f"Apos o insere (2, 'morango'): {misturada}")

# remove(elemento): Remove ocorrência de um elemento.
misturada.remove("morango")
print(f'Removendo elemento: {misturada}')
print(f'Apos o pop(morango): {misturada}')

# pop(indice): Remove e retorna o elemento na posição especificada. Se nenhum índice for passado, remove o último elemento.
elemento_devido = misturada.pop(3)
print(f'Elemento removido: {elemento_devido}')
print(f'Apos o pop(3): {misturada}')

# count(elemento): Conta quantas vezes um elemento aparece na lista.
print(f"Contar elementos da lista: {misturada.count('texto')}")

frutas = ["maçã", "banana", "laranja"]

print(frutas.sort())

# sort(): Ordena a lista em ordem crescente.
info = frutas.sort()
print(f'Ordena a lista em ordem crescente: {info}')

# sort(reverse=True) para ordenar em ordem decrescente
ret = frutas.sort(reverse=True)
print(f'Ordena a lista em ordem decrescente: {ret}')