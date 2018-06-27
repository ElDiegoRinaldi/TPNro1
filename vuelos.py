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

    def mostrarPasajeros(self):
        listaDNIs = []
        for item in self.listaPasajeros:
            listaDNIs.append(item.DNI)

        return listaDNIs


    def getPasajeros(self):
        return self.listaPasajeros

    def getTripulacion(self):
        listaDNIs = []
        for item in self.listaTripulacion:
            listaDNIs.append(item.DNI)

        return listaDNIs

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

    def PasajerosVipOEspeciales(self):   #Punto 6
        pasajerosVip = []

        for item in self.listaPasajeros:
            if item.VIP == 1 or item.necesidades_esp != "":
                pasajerosVip.append(item.nombre + ' ' + item.apellido + ' ' + item.DNI)

        return pasajerosVip

    def IdiomasPorVuelo(self): #Punto 7
        idiomasHablados = []

        for item in self.listaTripulacion:
            if item.tipo == 'Servicio':
                for item2 in item.listaIdiomas:
                    if item2 not in idiomasHablados:
                        idiomasHablados.append(item2)


        return idiomasHablados