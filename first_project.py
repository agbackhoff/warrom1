def escribir_mensaje():
    mensaje = "¡Hola desde Docker!"
    
    # Escribir el mensaje en output.txt
    with open('output.txt', 'w') as archivo:
        archivo.write(mensaje)
    
    print("Mensaje escrito en output.txt exitosamente")

if __name__ == "__main__":
    escribir_mensaje() 