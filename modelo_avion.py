class Modelo_Avion (object):
    codigo = None
    cant_pasajeros_max = None
    cant_tripulacion_necesaria = None

    def __init__(self, codigo, cant_p, cant_t):
        self.codigo = codigo
        self.cant_pasajeros_max = cant_p
        self.cant_tripulacion_necesaria = cant_t