# Nesse outro exemplo usaremos Váriaveis com dados

frutas_tupladas = ("maçã", "banana", "laranja")  # TUPLA = Conjunto de dados (pode ser string ou number) 
# -> Uma TUPLA não pode receber, alterar ou subtrair mais dasdos

fruta_lista = [] # Uma LISTA pode, alterar dados a vontade com funções

print(type(frutas_tupladas))
print(type(fruta_lista))

for variavel_nova in frutas_tupladas:           # Criamos o for para Percorrer uma sequencia de dados que chamamos da variavel_nova e ela vai extrai os dados com "in" de frutas.tupladas
    fruta_lista.append(variavel_nova.upper())   # Assim fazemos a fruta_lista .append (Tipo adicionando a lista) o valor da Variavel_nova que tem os dados da Tupla com o .upper e a liberdade de escrever e modificar

print(fruta_lista)