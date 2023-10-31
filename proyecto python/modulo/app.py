from .usuario import Usuario
from .vehiculo import Vehiculo
import json

class AppAlquilerCompra:
    def __init__(self):
        self.usuarios_registrados = {}
        self.opciones_vehiculos = {
            'carro': [Vehiculo('Mazda', 250000, 5), Vehiculo('Toyota', 220000, 3), Vehiculo('Suzuki', 180000, 4)],
            'moto': [Vehiculo('Yamaha', 50000, 6), Vehiculo('Honda', 60000, 7), Vehiculo('Kawasaki', 45000, 2)]
        }
        self.opciones_vehiculos['carro'][0].agregar_precio_alquiler(1, 500)
        self.opciones_vehiculos['carro'][0].agregar_precio_alquiler(3, 1400)
        self.opciones_vehiculos['carro'][0].agregar_precio_alquiler(7, 3000)

        self.opciones_vehiculos['carro'][1].agregar_precio_alquiler(1, 600)
        self.opciones_vehiculos['carro'][1].agregar_precio_alquiler(3, 1500)
        self.opciones_vehiculos['carro'][1].agregar_precio_alquiler(7, 3200)
        
        self.opciones_vehiculos['carro'][2].agregar_precio_alquiler(1, 400)
        self.opciones_vehiculos['carro'][2].agregar_precio_alquiler(3, 1300)
        self.opciones_vehiculos['carro'][2].agregar_precio_alquiler(7, 2800)

        self.opciones_vehiculos['moto'][0].agregar_precio_alquiler(1, 300)
        self.opciones_vehiculos['moto'][0].agregar_precio_alquiler(3, 800)
        self.opciones_vehiculos['moto'][0].agregar_precio_alquiler(7, 1800)

        self.opciones_vehiculos['moto'][1].agregar_precio_alquiler(1, 400)
        self.opciones_vehiculos['moto'][1].agregar_precio_alquiler(3, 1000)
        self.opciones_vehiculos['moto'][1].agregar_precio_alquiler(7, 2200)

        self.opciones_vehiculos['moto'][2].agregar_precio_alquiler(1, 300)
        self.opciones_vehiculos['moto'][2].agregar_precio_alquiler(3, 1300)
        self.opciones_vehiculos['moto'][2].agregar_precio_alquiler(7, 2600)
        self.cargar_usuarios()

    def registrar_usuario(self, nombre_usuario, contrasena):
        try:
            usuario = Usuario(nombre_usuario, contrasena)
            self.usuarios_registrados[nombre_usuario] = usuario
            self.guardar_usuarios()
            print("Usuario registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar usuario: {e}")

    def mostrar_opciones(self):
        try:
            print("\nOpciones de vehículos:")
            print("1. Alquilar")
            print("2. Comprar")
            opcion = input("Seleccione una opción (1 o 2): ")

            if opcion == '1':
                self.seleccionar_tipo('alquiler')
            elif opcion == '2':
                self.seleccionar_tipo('compra')
            else:
                if opcion != 1 or 2:
                    print("Opción no válida. Por favor, seleccione 1 o 2.")
        except Exception as e:
            print(f"Error al mostrar opciones: {e}")

    def seleccionar_tipo(self, tipo_operacion):
        try:
            tipo_vehiculo = input("\nSeleccione el tipo de vehículo (carro o moto): ")
            if tipo_vehiculo in self.opciones_vehiculos:
                print(f"\nOpciones de {tipo_vehiculo}s disponibles:")
                for i, vehiculo in enumerate(self.opciones_vehiculos[tipo_vehiculo], start=1):
                    print(f"{i}. {vehiculo} - Precio: ${vehiculo.precio_compra} - Stock: {vehiculo.stock}")
                opcion = int(input(f"Seleccione el vehículo que desea {tipo_operacion} (1, 2, o 3): "))
                if opcion >= 1 and opcion <= 3:
                    vehiculo_elegido = self.opciones_vehiculos[tipo_vehiculo][opcion - 1]
                    print(f"Usted ha seleccionado un {vehiculo_elegido.nombre}.")
                    dias_alquiler = int(input("Ingrese la cantidad de días de alquiler: "))
                    if dias_alquiler in vehiculo_elegido.precios_alquiler:
                        costo_total = vehiculo_elegido.precios_alquiler[dias_alquiler]
                        print(f"El costo total del alquiler es: ${costo_total}")
                    else:
                        print("No se encontró un precio de alquiler para la cantidad de días especificada.")
                else:
                    print("Opción no válida.")
            else:
                print("Tipo de vehículo no válido.")
        except Exception as e:
            print(f"Error al seleccionar tipo: {e}")

    def guardar_usuarios(self):
        with open('usuarios.json', 'w') as archivo_json:
            usuarios_dict = {}
            for nombre, usuario in self.usuarios_registrados.items():
                usuarios_dict[nombre] = {
                    'nombre_usuario': usuario.nombre_usuario,
                    'contrasena': usuario.contrasena,
                    'vehiculo_elegido': None,  
                    'precio_vehiculo': None,  
                }
            json.dump(usuarios_dict, archivo_json)

    def cargar_usuarios(self):
        try:
            with open('usuarios.json', 'r') as archivo_json:
                usuarios_dict = json.load(archivo_json)
                for nombre, usuario_data in usuarios_dict.items():
                    nombre_usuario = usuario_data['nombre_usuario']
                    contrasena = usuario_data['contrasena']
                    self.usuarios_registrados[nombre] = Usuario(nombre_usuario, contrasena)
        except FileNotFoundError:
            pass