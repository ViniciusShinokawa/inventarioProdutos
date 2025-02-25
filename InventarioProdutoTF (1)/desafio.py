#1. Crie uma lista com 10 items
esporte = ["Futebol","Basquete","Karate","KungFu","Baseball"]
#2. Crie uma Tupla com 5 items 
minha_tupla = (1, "dois", 3.0, True, [5, 6, 7])
print(minha_tupla)
#3. Criedicinario com 3 items (codigo,nome,preço)
meu_dicionario = { 
    "codigo" : 2,
    "nome" : "Arroz",
    "preço" : 19.00 ,
}

print(meu_dicionario)
# Crie uma função que imprima os items da lista na tela 

def imprimir_esportes(esportes):
    for esporte in esportes:
        print(esporte)

# Exemplo de uso
esportes = ["Futebol", "Basquete", "Karate", "KungFu", "Baseball"]
imprimir_esportes(esportes)

