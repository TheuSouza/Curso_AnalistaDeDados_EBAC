import re


# Usando Re para encontrar a letra "A" em textos
contador = len(re.findall('a', 'a arara azul arranha a aranha alaranjada', re.IGNORECASE))
print(contador)