from sistema import Sistema

ElSistema = Sistema()

ElSistema.cargar_archivos('datos.json')


print('Punto 1')
for item in ElSistema.listaVuelos:
    print('Vuelo: '+ str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino )
    for item2 in item.getPasajeros():
        print(item2.nombre + ' ' + item2.apellido)
    print('\n')


print('Punto 2')
for item in ElSistema.listaVuelos:
    print('Vuelo: ' + str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino)
    print(item.PasajeroMasJovenPorVuelo())

print('hola')
for item in ElSistema.listaVuelos:
    print(item.getTripulacion())

