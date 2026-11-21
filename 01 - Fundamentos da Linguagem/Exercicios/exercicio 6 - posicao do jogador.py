#################################################################
              # Exercício 6 – Posição do jogador
#################################################################
# Exercício 6 – Posição do jogador
# Utilizando o input(), peça ao usuário para informar a posição de um jogador. As opções esperadas são:
# goleiro
# defesa
# meio
# ataque
# Armazene a resposta em uma variável chamada posicao.
# Depois, utilize match case para verificar a posição informada e mostrar uma mensagem correspondente à função daquele jogador em campo.
# Por exemplo: Digite a posição do jogador: ataque
# Saída esperada: Responsável principalmente pela criação e finalização das jogadas ofensivas.
# Crie também um caso para quando o usuário digitar uma posição diferente das opções esperadas. Nesse caso, mostre: Posição inválida.

posicao_jogador = input("Informe a posição do jogador: opções -> goleiro, defesa, meio, ataque: ")

match posicao_jogador:
    case "goleiro":
        print("Responsável por defender bolas lançadas ao gol.")
    case "defesa":
        print("Responsável por impedir que o ataque do time adversário avance ao gol.")
    case "meio":
        print("Responsável por armar as jogadas para os atacantes.")
    case "ataque": 
        print("Responsável pelo ataque ao time adversário.")
    case _: 
        print("Posição inválida.")