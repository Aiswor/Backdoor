# README

## English Version

### Program:

This script starts an HTTP server on the specified port.
It allows you to access the files in the directory where the script is located from a web browser.

1. Starts a local HTTP server on port `3500`.
2. Clears the terminal screen.
3. Opens Firefox.
4. Clears the terminal screen again.
5. Asks the user for feedback on the program.

### How to use:

Run the script using Python:
```bash
python3 script.py
```

If you need to stop the HTTP server, follow these steps:
1. Run `ps aux` in the terminal to find the process running on port `3500`.
2. Identify the process ID (PID) of the server.
3. Use `kill <PID>` to stop the process.

### Notes:
- Script designed for Linux systems.
- Do not close the terminal while the script is running.
- You must have Python 3 installed for the program to work.

----------------------------------------------------------------------------------------------------

## Versión en Español

### Programa:

Este script abre un servidor HTTP en el puerto establecido.
Te permite acceder a los archivos del directorio donde se encuentra el script desde un navegador.

1. Inicia un servidor HTTP local en el puerto `3500`.
2. Limpia la pantalla del terminal.
3. Abre Firefox.
4. Limpia la pantalla del terminal nuevamente.
5. Pregunta al usuario su opinión sobre el programa.

### Cómo usarlo:

Ejecuta el script usando Python:
```bash
python3 script.py
```

Si necesitas detener el servidor HTTP, sigue estos pasos:
1. Ejecuta `ps aux` en la terminal para encontrar el proceso en el puerto `3500`.
2. Identifica el ID del proceso (PID) del servidor.
3. Usa `kill <PID>` para detener el proceso.

### Notas:
- Script diseñado para sistemas Linux.
- No cierres la terminal mientras el script esté en ejecución.
- Tienes que tener instalado python3 para que el programa funcione.

