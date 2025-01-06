def obtener_info_sistema():
    import platform
    import os
    import socket
    
    return {
        "sistema": platform.system(),
        "version": platform.version(),
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "usuario": os.getenv('USER', 'desconocido'),
        "directorio": os.getcwd()
    }

def escribir_mensaje():
    try:
        info_sistema = obtener_info_sistema()
        
        mensaje = "=== REPORTE DE EJECUCIÓN ===\n\n"
        mensaje += f"¡Hola desde Docker!\n"
        mensaje += f"Fecha de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        mensaje += "\n=== INFORMACIÓN DEL SISTEMA ===\n"
        mensaje += f"Sistema Operativo: {info_sistema['sistema']}\n"
        mensaje += f"Versión SO: {info_sistema['version']}\n"
        mensaje += f"Hostname: {info_sistema['hostname']}\n"
        mensaje += f"Versión Python: {info_sistema['python_version']}\n"
        mensaje += f"Usuario: {info_sistema['usuario']}\n"
        mensaje += f"Directorio: {info_sistema['directorio']}\n"
        
        mensaje += "\n=== VARIABLES DE ENTORNO ===\n"
        for var in ['PATH', 'PYTHONPATH', 'LANG']:
            mensaje += f"{var}: {os.getenv(var, 'no definida')}\n"
        
        mensaje += "\n=== ESTADO DE EJECUCIÓN ===\n"
        mensaje += "Estado: Ejecución exitosa\n"
        mensaje += f"Timestamp final: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}\n"
        
        # Escribir el mensaje en output.txt
        with open('output.txt', 'w', encoding='utf-8') as archivo:
            archivo.write(mensaje)
        
        print("Reporte detallado escrito en output.txt exitosamente")
        print("Contenido del reporte:")
        print(mensaje)
    
    except Exception as e:
        error_msg = f"Error inesperado: {str(e)}\n"
        error_msg += f"Tipo de error: {type(e).__name__}\n"
        print(error_msg)
        
        # Intentar escribir el error en el archivo
        try:
            with open('output.txt', 'w', encoding='utf-8') as archivo:
                archivo.write("=== ERROR DE EJECUCIÓN ===\n" + error_msg)
        except:
            print("No se pudo escribir el error en el archivo")

if __name__ == "__main__":
    import os
    from datetime import datetime
    escribir_mensaje() 