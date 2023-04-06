#Palindromo - palavra ou frase que se pode ler, 
#Indiferentemente, da esquerda para a 
#Direita ou vice-versa.
def verificar_palindromo(texto):
    texto = texto.lower().replace("","")
    return texto == texto[::-1]
    
#Texto[::-1] inverte o texto 

texto  = "Socorram-me, subi no ônibus em Marrocos"
if verificar_palindromo(texto):
    print(texto, "é um palíndromo")
else:
    print(texto, "não é um palíndromo.")