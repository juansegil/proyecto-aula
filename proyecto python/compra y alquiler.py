class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}"

class Vehiculo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Vehículo: {self.nombre} - Precio: ${self.precio}"

class AppAlquilerCompra:
    def __init__(self):
        self.usuarios_registrados = {}
        self.opciones_vehiculos = {
            'carro': [Vehiculo('Mazda', 25000), Vehiculo('Toyota', 22000), Vehiculo('suzuki', 18000)],
            'moto': [Vehiculo('Yamaha', 5000), Vehiculo('honda', 6000), Vehiculo('Kawasaki', 4500)]
        }

    def registrar_usuario(self, nombre_usuario, contrasena):
        usuario = Usuario(nombre_usuario, contrasena)
        self.usuarios_registrados[nombre_usuario] = usuario

    def mostrar_opciones(self):
        print("\nOpciones de vehículos:")
        print("1. Alquilar")
        print("2. Comprar")
        opcion = input("Seleccione una opción (1 o 2): ")
        if opcion == '1':
            self.seleccionar_tipo('alquiler')
        elif opcion == '2':
            self.seleccionar_tipo('compra')
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

    def seleccionar_tipo(self, tipo_operacion):
        tipo_vehiculo = input("\nSeleccione el tipo de vehículo (carro o moto): ")
        if tipo_vehiculo in self.opciones_vehiculos:
            print(f"\nOpciones de {tipo_vehiculo}s disponibles:")
            for i, vehiculo in enumerate(self.opciones_vehiculos[tipo_vehiculo], start=1):
                print(f"{i}. {vehiculo} - Precio: ${vehiculo.precio}")
            opcion = int(input(f"Seleccione el vehículo que desea {tipo_operacion} (1, 2, o 3): "))
            if opcion >= 1 and opcion <= 3:
                vehiculo_elegido = self.opciones_vehiculos[tipo_vehiculo][opcion - 1]
                print(f"Usted ha {tipo_operacion} un {vehiculo_elegido.nombre}. ¡Disfrútelo! Precio: ${vehiculo_elegido.precio}")
            else:
                print("Opción no válida.")
        else:
            print("Tipo de vehículo no válido.")

def main():
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
            print("Usuario registrado exitosamente.")
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

if __name__ == "__main__":
    main()
