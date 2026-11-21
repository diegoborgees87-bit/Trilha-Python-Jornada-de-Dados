########################################################
        # Exercício 3 – Trabalhando com operadores
########################################################
# pontos = 7
# vitorias = 2
# saldo_gols = 4

# Crie expressões que respondam às seguintes perguntas:
# A seleção possui mais de 5 pontos?
# A seleção possui exatamente 3 vitórias?
# O saldo de gols é maior ou igual a 0?
# A seleção possui mais de 5 pontos e saldo de gols positivo?
# A seleção possui 3 vitórias ou mais de 6 pontos?


pontos     = 7
vitorias   = 2
saldo_gols = 4 

if pontos > 5: 
    print("A seleção possui mais de 5 pontos.")
else: 
    print("A seleção não possui mais de 5 pontos.")

if vitorias == 3:
    print("A seleção possui exatamente 3 vitórias.")
else:
    print("A seleção não possui 3 vitórias exatas.")

if saldo_gols >= 0:
    print("O saldo de gols é maior ou igual a 0.")
else:
    print("O salde de gols é menor que 0.")

if pontos > 5 and saldo_gols > 0: 
    print("A seleção possui mais de 5 pontos e saldo de gols positivo.")
else: 
    print("A seleção não possui mais de 5 pontos e saldo de gols positivo.")

if vitorias >= 3 or pontos > 6:
    print("A seleção possui mais de 3 vitórias ou mais de 6 pontos.")
else: 
    print("A seleção não possui mais de 3 vitórias ou mais de 6 pontos.")