class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir_datos(self):
        print(f"Titular: {self.titular}, Cantidad: ${self.cantidad}")


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        self.imprimir_datos()
        print("Información de Caja de Ahorro...")


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtener_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self):
        self.imprimir_datos()
        print(f"Plazo: {self.plazo} meses, Interés: {self.interes}%")
        total_interes = self.obtener_interes()
        print(f"El interés será de: ${total_interes} en total.")

#Datos a utilizar 
caja_ahorro = CajaAhorro("Sebastián", 60000)
plazo_fijo = PlazoFijo("Mariana", 120000, 24, 8)

print("Caja de Ahorro:")
caja_ahorro.mostrar_informacion()

print("\nPlazo Fijo:")
plazo_fijo.mostrar_informacion()