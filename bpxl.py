palabras = ["manzana", "pera", "banana", "naranja", "uva"]
letra = "n" 
resultado = []  
for palabra in palabras:  
    if letra in palabra: 
        resultado.append(palabra)  
print(resultado) 