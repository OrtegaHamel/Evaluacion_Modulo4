import os

# Clase base para representar un libro físico
class Libro:
    def __init__(self, titulo, autor, anio, estado='Disponible'):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.estado = estado

    def __str__(self):
        # Método especial para representar el libro como una cadena de texto
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}\nEstado: {self.estado}"
    
    # Métodos getters y setters para los atributos del libro
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor):
        self.autor = autor

    def get_anio(self):
        return self.anio
    
    def set_anio(self, anio):
        self.anio = anio

    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado

class LibroDigital(Libro):
    def __init__(self, titulo, autor,anio, formato, estado='Disponible'):
        # Llama al constructor de la clase base (Libro)
        super().__init__(titulo, autor, anio, estado)
        # Atributo adicional para el formato del libro digital
        self.formato = formato

    def __str__(self):
        # Sobreescribe el método __str__ para incluir el formato del libro digital
        return super().__str__() + f", Formato: {self.formato}"

    # Métodos getters y setters para el atributo del formato del libro digital
    def get_formato(self):
        return self.formato

    def set_formato(self, formato):
        self.formato = formato

#Clase para representar la biblioteca
class Biblioteca:
    def __init__(self, archivo='biblioteca.txt'):
        #Incializa la biblioteca con una lista vacia de libros
        self.libros = []
        self.archivo = archivo
        #Carga los libros desde el archivo
        self.cargar_libros()

    def agregar_libro(self, libro):
        #Agrega un libro a la biblioteca
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def eliminar_libro(self, titulo):
        #Elimina un libro por su título
        for libro in self.libros:
            if libro.get_titulo() == titulo:
                self.libros.remove(libro)
                print(f"Libro eliminado: {titulo}")
                return 
            #Si no se encuentra, lanza una excepción
        raise ValueError(f"Libro no encontrado: {titulo}")
    
    def listar_libros(self):
        #Lista todos los libros en la biblioteca
        if not self.libros:
            print("La biblioteca esta vacia.")
            return
        print("\n --- Libros en la biblioteca --- \n")
        for libro in self.libros:
            print(libro)
            print("-" * 40)

    def buscar_libro(self, titulo):
        #Busca un libro por su título y lo devuelve
        for libro in self.libros:
            if libro.get_titulo() == titulo:
                print("\n --- Libro encontrado --- \n")
                print(libro)
                return
        #Si no se encuentra, lanza una excepción
        raise ValueError(f"Libro no encontrado: {titulo}")
    
    def marcar_prestado(self, titulo):
        #Marca un libro como prestado
        for libro in self.libros:
            if libro.get_titulo() == titulo and libro.get_estado() == 'Disponible':
                libro.set_estado('Prestado')
                print(f"Libro prestado: {titulo}")
                return
        #Si no se encuentra, lanza una excepción
        raise ValueError(f"Libro no encontrado: {titulo}")
    
    def devolver_libro(self, titulo):
        #Devuelve un libro prestado
        for libro in self.libros:
            if libro.get_titulo() == titulo and libro.get_estado() == 'Prestado':
                libro.set_estado('Disponible')
                print(f"Libro devuelto: {titulo}")
                return
        #Si no se encuentra, lanza una excepción
        raise ValueError(f"Libro no encontrado: {titulo}")
    
    def cargar_libros(self):
    # Carga los libros desde el archivo al iniciar el programa
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 5:
                    # Si hay 5 datos, es un libro digital
                        libro = LibroDigital(data[0], data[1], data[2], data[3], data[4])
                    else:
                    # Si hay menos de 5 datos, es un libro físico
                        libro = Libro(data[0], data[1], data[2], data[3])
                    self.libros.append(libro)
            print("Libros cargados desde el archivo.")
    
    def guardar_libros(self):
    # Guarda los libros en el archivo al salir del programa
        with open(self.archivo, 'w') as file:
            for libro in self.libros:
                if isinstance(libro, LibroDigital):
                    # Si es un libro digital, guarda la información adicional
                    file.write(f"{libro.get_titulo()},{libro.get_autor()},{libro.get_anio()},{libro.get_formato()},{libro.get_estado()}\n")
                else:
                    # Si es un libro físico, no guarda la información adicional
                    file.write(f"{libro.get_titulo()},{libro.get_autor()},{libro.get_anio()},{libro.get_estado()}\n")
        print("Cambios guardados en el archivo.")

    
def main():
        # Función principal del programa
        biblioteca = Biblioteca()
        while True:
            print("\n--- Gestor de Biblioteca ---")
            print("1. Agregar libro")
            print("2. Eliminar libro")
            print("3. Listar libros")
            print("4. Buscar libro")
            print("5. Marcar libro como prestado")
            print("6. Devolver libro")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                anio = input("Ingrese el año del libro: ")
                formato = input("Formato (solo para libros digitales, deje en blanco para libros físicos): ")
                if formato:
                    libro = LibroDigital(titulo, autor, anio, formato)
                else:
                    libro = Libro(titulo, autor, anio)
                biblioteca.agregar_libro(libro)
            elif opcion == '2':
                titulo = input("Ingrese el título del libro a eliminar: ")
                try:
                    biblioteca.eliminar_libro(titulo)
                except ValueError as e:
                    print(e)
            elif opcion == '3':
                biblioteca.listar_libros()
            elif opcion == '4':
                titulo = input("Ingrese el título del libro a buscar: ")
                try:
                    biblioteca.buscar_libro(titulo)
                except ValueError as e:
                    print(e)
            elif opcion == '5':
                titulo = input("Ingrese el título del libro a marcar como prestado: ")
                try:
                    biblioteca.marcar_prestado(titulo)
                except ValueError as e:
                    print(e)
            elif opcion == '6':
                titulo = input("Ingrese el título del libro a devolver: ")
                try:
                    biblioteca.devolver_libro(titulo)
                except ValueError as e:
                    print(e)
            elif opcion == '7':
                biblioteca.guardar_libros()
                print("Gracias por usar el Gestor de Biblioteca")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opcción válida.")

if __name__ == '__main__':
    # Inicia el programa
    main()