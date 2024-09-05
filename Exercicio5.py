#5) Invertendo Caracteres de uma String em Python
def inverter_string(texto):
  """
  Inverte os caracteres de uma string.

  Args:
    texto: A string a ser invertida.

  Returns:
    A string invertida.
  """
  texto_invertido = ""
  for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

# String a ser invertida
texto = "Exemplo de string"

texto_invertido = inverter_string(texto)

print(f"String original: {texto}")
print(f"String invertida: {texto_invertido}")