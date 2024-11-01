"""Tipos de Variáveis -> Texto formatado"""

# Declaração
nome = 'Gelzieny'
sobrenome = 'R. Martins'
nome_completo_aspas = """Gabriel
Rezende"""
nome_completo_quebrado = "Gelzieny \
  Casemiro"

# Formatação
print("Nome completo (1a forma): ", nome)
print("Nome completo (2a forma): " + nome)
print("Nome completo (3a forma): " + "Gelzieny " + "Rezende")
print("Nome completo (4a forma): " + "Gelzieny","Rezende")
print("Nome completo (5a forma): ", nome_completo_aspas)
print("Nome completo (6a forma): ", nome_completo_quebrado)
print("Nome completo (7a forma): %s" % nome)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))