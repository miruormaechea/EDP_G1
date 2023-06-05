class Persona:
    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail
        self.calle = calle
        self.altura = altura
        self.telefono = telefono

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido}"