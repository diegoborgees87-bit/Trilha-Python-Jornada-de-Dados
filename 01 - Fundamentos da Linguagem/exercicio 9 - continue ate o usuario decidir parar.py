####################################################################
     # Exercício 9 – Continue até o usuário decidir parar
####################################################################
# Crie um programa que permaneça em execução enquanto o usuário responder: "sim"
# A cada repetição, mostre: "Treino iniciado!"
# Depois, pergunte novamente: "Deseja realizar outro treino?"
# Quando a resposta for diferente de sim, o while deve terminar e o programa deve mostrar: "Treino encerrado."
# Não é necessário trabalhar com números neste exercício. Utilize a resposta do input() como texto.

resposta = "S"

while resposta == "S":
    print("Treino iniciado!")
    resposta = input("Deseja realizar outro treino? S / N  ")

print("Treino encerrado.")
  
