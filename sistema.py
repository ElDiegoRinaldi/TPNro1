from persona import Tripulacion
from persona import Pasajeros
from persona import Servicio
from vuelos import Vuelos
from modelo_avion import Modelo_Avion

from datetime import datetime


import json

class Sistema (object):

    def __init__(self):
        self.listaVuelos = []
        self.listaPersonas = []
        self.listaAviones = []

    def cargar_archivos (self, archivos):      #JSON
        with open(archivos, 'r') as archivo:
            diccionario = json.loads(archivo.read())

        for avion in diccionario['Aviones']:
            a = Modelo_Avion(avion['codigoUnico'],avion['cantidadDePasajerosMaxima'],avion['cantidadDeTripulaciónNecesaria'])
            self.listaAviones.append(a)

        for persona in diccionario['Personas']:
            if persona['tipo'] == 'Pasajero':

                fechaNacimiento = datetime.strptime(persona['fechaNacimiento'], '%Y-%m-%d').date()

                necesidades = ""
                try:
                    necesidades = persona['solicitudesEspeciales']
                except:
                    pass
                p = Pasajeros(persona['tipo'], persona['nombre'], persona['apellido'], fechaNacimiento, persona['dni'], persona['vip'], necesidades)

                self.listaPersonas.append(p)

            if persona['tipo'] == 'Piloto':
                fechaNacimiento = datetime.strptime(persona['fechaNacimiento'], '%Y-%m-%d').date()

                codigos = persona['avionesHabilitados']

                listaTemporal = []

                for item in self.listaAviones:
                    for item2 in codigos:
                        if item.codigo == item2:
                            listaTemporal.append(item)

                t = Tripulacion(persona['tipo'], persona['nombre'], persona['apellido'], fechaNacimiento, persona['dni'])
                t.avionesHabilitados = listaTemporal

                self.listaPersonas.append(t)

            if persona['tipo'] == 'Servicio':
                fechaNacimiento = datetime.strptime(persona['fechaNacimiento'], '%Y-%m-%d').date()

                idiomas = persona['idiomas']
                codigos = persona['avionesHabilitados']

                listaTemporal = []

                for item in self.listaAviones:
                    for item2 in codigos:
                        if item.codigo == item2:
                            listaTemporal.append(item)

                s = Servicio(persona['tipo'], persona['nombre'], persona['apellido'],fechaNacimiento , persona['dni'])
                s.listaIdiomas = idiomas
                s.avionesHabilitados = listaTemporal

                self.listaPersonas.append(s)

        for vuelos in diccionario['Vuelos']:

            lPasa = vuelos['pasajeros']
            lTrip = vuelos['tripulacion']

            PasajerosAux = []
            TripulantesAux = []

            for item in self.listaPersonas:
                if item.tipo == 'Pasajero':
                    for item2 in lPasa:
                        if item.DNI == item2:
                            PasajerosAux.append(item)
            for item in self.listaPersonas:
                if item.tipo == 'Piloto'or item.tipo == 'Servicio':
                    for item2 in lTrip:
                        if item.DNI == item2:
                            TripulantesAux.append(item)

            for item in self.listaAviones:
                fecha = datetime.strptime(vuelos['fecha'], '%Y-%m-%d').date()

                if item.codigo == vuelos['avion']:
                    v = Vuelos(item, vuelos['hora'], fecha, vuelos['origen'], vuelos['destino'])
                    v.listaPasajeros = PasajerosAux
                    v.listaTripulacion = TripulantesAux

                    self.listaVuelos.append(v)


    def VuelosQueNoAlcanzenLaTripMinima(self): #Punto 3
        listaVuelosQueNoAlcanzan = []

        for item in self.listaVuelos:
            if item.getCantTripulacion() < item.Avion.cant_tripulacion_necesaria:
                listaVuelosQueNoAlcanzan.append(str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino)

        return listaVuelosQueNoAlcanzan

    def VuelosConTripulantesNoAutorizados(self): #Punto 4
        listaVuelosConTripulantesNoAutorizados = []

        for item in self.listaVuelos:
            for item2 in item.listaTripulacion:
                if item.Avion not in item2.avionesHabilitados:
                    listaVuelosConTripulantesNoAutorizados.append('Vuelo a ' + item.destino)
                    break

        return listaVuelosConTripulantesNoAutorizados

    def TripulantesQueVolaronMasDeUnaVezAlDia(self): #Punto 5
        tripQueRompenLaRegla = []

        for item in self.listaVuelos:
            for item2 in self.listaVuelos:
                if item != item2:
                    if item.fecha == item2.fecha:
                        for item3 in item.listaTripulacion:
                            if item3 in item2.listaTripulacion:
                                tripQueRompenLaRegla.append(item3.nombre + ' ' + item3.apellido + ' ' + ' DNI: ' + item3.DNI)
            break

        return tripQueRompenLaRegla




