
def find_replace(text, oldText, newText):
    """This function look for a specific text string and replace it."""

    new_string = ""  # Creo una cadena vacia, que es donde se almacenará el nuevo texto.
    i = 0  # Contador que ira aumentando hasta terminar el largo de la cadena
    while i < len(text):  # Mientras el contador sea menor que la cantidad total de caracteres de la cadena de texto. Se seguira ejecutando el programa.
        if text[i:i+len(oldText)] == oldText:  # Es una forma de de encontrar los indices del texto que se desea cambiar.
            new_string = new_string + newText  # Cuando se encuentran los indices del texto que se desea cambiar, se agrega el nuevo texto en el indice donde estaba el texto a cambiar.
            i = i + len(oldText)  # Permite aumentar la busqueda de los indices y tambien ayuda a salir del bucle.

        else:
            new_string = new_string + text[i]  # Si los indices del texto a cambiar no se encuentran, cada letra se va agregando a la nueva cadena.
            i = i + 1  # Aumenta en uno el número del indice a buscar.

    return new_string

print(find_replace("Hola como anda todo? Espero que estes muy bien!", "que", "tu"))