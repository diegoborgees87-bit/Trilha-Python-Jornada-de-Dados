########################################################
         # Exercício 2 – Calculando o placar
########################################################
# Uma seleção marcou 3 gols no primeiro tempo e 2 gols no segundo tempo.
# Crie variáveis para armazenar essas duas informações e calcule:
# o total de gols da partida;
# quantos gols foram marcados a mais no primeiro tempo em relação ao segundo.
# Ao final, imprima os resultados na tela.

gols_1t = 3 
gols_2t = 2 

total_gols     = gols_1t + gols_2t
diferenca_gols = gols_1t - gols_2t 

if diferenca_gols > 0:
    print(f"A diferença de Gols entre o primeiro e segundo tempo foi de: {diferenca_gols}")
else:
    print(f"Não forma marcos mais gols no segundo tempo.")

print(f"O total de gols foi de: {total_gols}")