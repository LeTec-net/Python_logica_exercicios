'''
Questão 3 – Lista de frutas
Crie uma lista contendo pelo menos 5 frutas.

Depois:

 - Exiba a lista completa.
 - Exiba apenas a primeira fruta.
 - Exiba apenas a última fruta.
 - Adicione algumas frutas e exiba a última, independente da quantidade.
'''

fruits = ["banana", "laranja", "kiwi",
          "abacate", "tangerina", "morango", "pêra"]
print(fruits[0])
print(fruits[4])
# Obtém o último elemento da lista independente da quantidade
print(fruits[len(fruits) - 1])
