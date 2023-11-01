from modulo.app import AppAlquilerCompra

class main:
    def main():
        try:
            app = AppAlquilerCompra()
            print("Bienvenido a la aplicación de alquiler y compra de vehículos.")
            while True:
                print("\nMenu Principal:")
                print("1. Registrarse")
                print("2. Iniciar sesión")
                print("3. Salir")
                opcion = input("Seleccione una opción (1, 2 o 3): ")

                if opcion == '1':
                    nombre_usuario = input("Ingrese su nombre de usuario: ")
                    contrasena = input("Ingrese su contraseña: ")
                    app.registrar_usuario(nombre_usuario, contrasena)
                elif opcion == '2':
                    nombre_usuario = input("Ingrese su nombre de usuario: ")
                    contrasena = input("Ingrese su contraseña: ")
                    if nombre_usuario in app.usuarios_registrados and app.usuarios_registrados[nombre_usuario].contrasena == contrasena:
                        print(f"Bienvenido, {nombre_usuario}!")
                        app.mostrar_opciones()
                    else:
                        print("Nombre de usuario o contraseña incorrectos.")
                elif opcion == '3':
                    print("Gracias por usar nuestra aplicación. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        except Exception as e:
            print(f"Error en la función main: {e}")

    if __name__ == "__main__":
        main()