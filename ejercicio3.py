# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código
def es_palindrome(textoin):
    
    textoin = textoin.lower().replace(" ", "")
    
   
    if textoin == textoin[::-1]:
        return "El texto es palíndromo"
    else:
        return "El texto no es palíndromo"

print(es_palindrome("Paralelepipedo"))  