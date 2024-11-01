"""Principais métodos do tipo texto"""

# Declaração
nome = 'Gelzieny'
sobrenome = 'R. Martins'
idade = 30
saudacao = "Ola, seja bem vindo!!!"
mensagem = """Este e um texto
de multiplas linhas."""
frase = "Python e divertido!"

# Formatação
print("Formatacao: Nome = ", nome)

# Concatenação
print("Concatenacao: Nome completo = ", nome + " " + sobrenome)

# Interpolação (f-strings)
print(f"Interpolacao: Ola, {nome}! Voce tem {idade} anos.")

# Repetição
print("Repeticao: "+"ha" * 3)

# Comprimento da String
print(f"Comprimento da string: {len(frase)}")

# Indexação e Fatiamento
print(f"Fatiamento: {frase[0]}")

print(f"Fatiamento parte da string: {frase[0:3]}")

"""Métodos Comuns de Strings

lowe() => Converte para minúsculas.
"""
print(f"Converte para minusculas: {nome.lower()}")

#upper(): Converte para maiúsculas.
print(f"Converte para maiusculas: {nome.upper()}")

# replace(): Substitui uma parte da string por outra
sub = frase.replace("divertido", "top")
print(f"""Texto original:{frase} Texto substituido:  {sub}""")

# strip(): Remove espaços extras no início e no final.
texto = "   Python   ".strip()
print(f"Remove espacos: {texto}")