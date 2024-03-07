class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Sueldo: {self.sueldo}")

    def pagar_impuesto(self):
        if self.sueldo > 3000000:
            print("Debe pagar impuestos.")
        else:
            print("No tiene que pagar impuestos.")

nombre_persona = input("Ingrese el nombre: ")
edad_persona = int(input("Ingrese la edad: "))
sueldo_empleado = float(input("Ingrese el sueldo: "))

#instancias de las clases
persona = Persona(nombre_persona, edad_persona)
empleado = Empleado(nombre_persona, edad_persona, sueldo_empleado)

print("\nDatos de la Persona:")
persona.imprimir_datos()

print("\nDatos del Empleado:")
empleado.imprimir_datos()
empleado.pagar_impuesto()