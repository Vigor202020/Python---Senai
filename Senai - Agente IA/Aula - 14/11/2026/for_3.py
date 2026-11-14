inimigo = {"vida":100}

ataque = {"Chamas 🔥":25, "Água 🌊":20}     # Com os {} eu crio um DÍCIONARIO, com isso eu posso facilmente poxar os valores dento de uma variavel

inimigo["vida"] = inimigo["vida"] - ataque["Chamas 🔥"]     # Posso puxar as diferentes informações com []
inimigo["vida"] = inimigo["vida"] - ataque["Água 🌊"]

print(f("O Héroi causou inimigo["vida"] ")