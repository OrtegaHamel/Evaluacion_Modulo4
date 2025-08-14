# Gestor de Biblioteca
Por Álvaro Ortega Hamel

Este programa es una aplicación de gestión de biblioteca escrita en Python. Permite agregar, eliminar, listar, buscar, marcar como prestado y devolver libros. Los datos de los libros se almacenan en un archivo de texto llamado `biblioteca.txt`.

## Requisitos

- Python 3.6 o superior

## Instalación

1. Asegúrate de tener Python instalado en tu sistema. 
2. Clona este repositorio o descarga el archivo `gestor_biblioteca.py` y el archivo `README.md`.

## Ejecución

1. Abre una terminal o línea de comandos.
2. Navega al directorio donde se encuentra el archivo `gestor_biblioteca.py`.
3. Ejecuta el siguiente comando:

   ```sh
   python gestor_biblioteca.py

Si tienes varias versiones de Python instaladas, asegúrate de usar Python 3.

## Uso

Al ejecutar el programa, verás un menú con las siguientes opciones:
1. Agregar libro: Permite agregar un nuevo libro a la biblioteca.
2. Eliminar libro: Permite eliminar un libro de la biblioteca por su título.
3. Listar libros: Muestra todos los libros disponibles en la biblioteca.
4. Buscar libro: Busca un libro por su título y muestra su información.
5. Marcar libro como prestado: Marca un libro como prestado.
6. Devolver libro: Devuelve un libro que estaba prestado.
7. Salir: Guarda los cambios y sale del programa.

## Persistencia de Datos

Los datos de los libros se almacenan en el archivo biblioteca.txt. Al salir del programa, los cambios se guardan automáticamente en este archivo. Al iniciar el programa, los datos se cargan desde este archivo.

## Ejemplo de Archivo biblioteca.txt

El archivo biblioteca.txt contiene los datos de los libros en el siguiente formato:

Título,Autor,Año,Estado
Título,Autor,Año,Formato,Estado

## Notas
Asegúrate de que el archivo biblioteca.txt esté en el mismo directorio que el archivo gestor_biblioteca.py.
Si el archivo biblioteca.txt no existe, el programa lo creará automáticamente al guardar los datos por primera vez.