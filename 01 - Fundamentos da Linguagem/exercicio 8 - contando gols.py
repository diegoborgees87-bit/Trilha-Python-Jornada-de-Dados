############################################################
              # Exercício 8 – Contando gols
############################################################
# Crie uma variável: gols = 0
# Depois, utilize um for para simular 5 oportunidades de gol.
# A cada repetição, acrescente 1 à variável gols e mostre a quantidade atual.
# O resultado deve seguir esta ideia:
# Gol! Total: 1
# Gol! Total: 2
# Gol! Total: 3
# ...
# Ao final, mostre a quantidade total de gols.

gols = 0

for oportunidade in range(1, 6):
    gols += 1 

    print(f"Gol! Total: {gols}")

print(f"Total de Gols:{gols}")