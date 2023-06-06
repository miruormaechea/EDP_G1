class Persona:
    """
    Representa a una persona.
    Atributos:
    - nombre (str): El nombre de la persona.
    - apellido (str): El apellido de la persona.
    - dni (str): El DNI de la persona.
    - mail (str): El correo electrónico de la persona.
    - calle (str): El nombre de la calle de la dirección de la persona.
    - altura (str): La altura de la dirección de la persona.
    - telefono (str): El número de teléfono de la persona.
    """

    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono):
        """
        Inicializa un objeto Persona.
        :param nombre: El nombre de la persona.
        :param apellido: El apellido de la persona.
        :param dni: El DNI de la persona.
        :param mail: El correo electrónico de la persona.
        :param calle: El nombre de la calle de la dirección de la persona.
        :param altura: La altura de la dirección de la persona.
        :param telefono: El número de teléfono de la persona.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail
        self.calle = calle
        self.altura = altura
        self.telefono = telefono

    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la persona.
        :return: Una cadena que representa a la persona en el formato "Persona: <nombre> <apellido>".
        """
        return f"Persona: {self.nombre} {self.apellido}"
