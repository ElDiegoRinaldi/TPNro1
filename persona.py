class Persona (object):
    nombre = None
    apellido = None
    fecha_nac = None
    DNI = None

    def __init__(self, nombre, apellido, fecha, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha
        self.DNI = dni

class Pasajeros (Persona):
    VIP = None
    necesidades_esp = None
    tipo = None

    def __init__(self, tipo, nombre, apellido, fecha, dni, vip, nec):
        Persona.__init__(self, nombre, apellido, fecha, dni)
        self.tipo = tipo
        self.VIP = vip
        self.necesidades_esp = nec


class Tripulacion (Persona):
    modelo_avion = None
    tipo = None

    def __init__(self, tipo, nombre, apellido, fecha, dni):
        Persona.__init__(self, nombre, apellido, fecha, dni)
        self.tipo = tipo

        self.avionesHabilitados = []

class Servicio (Tripulacion):
    tipo = None

    def __init__(self, tipo, nombre, apellido, fecha, dni):
        Persona.__init__(self, nombre, apellido, fecha, dni)
        self.listaIdiomas = []
        self.tipo = tipo

        self.avionesHabilitados = []



