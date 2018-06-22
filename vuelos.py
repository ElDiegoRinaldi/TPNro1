class Vuelos (object):
    Avion = None
    hora = None
    fecha = None
    origen = None
    destino = None

    def __init__(self, Avion, hora, fecha, origen, destino):
        self.Avion = Avion
        self.hora = hora
        self.fecha = fecha
        self.origen = origen
        self.destino = destino

        self.listaPasajeros = []
        self.listaTripulacion = []

    def getPasajeros(self):
        return self.listaPasajeros

    def getTripulacion(self):
        listaApellidos = []
        for item in self.listaTripulacion:
            listaApellidos.append(item.apellido)

        return listaApellidos

    def getCantTripulacion(self):
        return len(self.listaTripulacion)

    def PasajeroMasJovenPorVuelo(self): #Punto 2

        pasajeroMenor = self.listaPasajeros[0]
        nombrePasajeroMenor = None

        for item in self.listaPasajeros:
            if item.fecha_nac >= pasajeroMenor.fecha_nac:
                pasajeroMenor = item
                nombrePasajeroMenor = item.nombre + ' ' + item.apellido + ' ' + item.DNI

        return nombrePasajeroMenor





