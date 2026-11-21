#################################################################
        # Exercício 5 – Avaliando o desempenho da seleção
#################################################################
# Crie uma variável chamada pontos.
# Utilizando if, elif e else, classifique o desempenho da seleção da seguinte forma:
# 7 pontos ou mais → Excelente campanha
# de 4 a 6 pontos → Campanha regular
# menos de 4 pontos → Campanha ruim
# Teste o programa utilizando diferentes valores para pontos.

pontos = 3

if pontos >= 7:
    print("Excelente campanha.")
elif pontos >= 4 and pontos <= 6: 
    print("Campanha regular.")          
else:
    print("Campanha ruim.") 