from datetime import datetime, timedelta

# espacios disponibles
espacios = {
    'vehiculos': ['v' + str(i) for i in range(1, 51)],
    'motos': ['m' + str(i) for i in range(1, 26)]
}

#diccionarios para almacenar el estado de los espacios, los alquileres y las entradas
estado_espacios = {esp: 'Disponible' for esp in espacios['vehiculos'] + espacios['motos']} 
alquiler = set()
registro_entrada = {}
registro_placas = {}

tarifa_hora_vehiculo = 5000  # Tarifa por hora para vehículos
tarifa_hora_moto = 3000  # Tarifa por hora para motos

hora_entrada = datetime.strptime('06:00', '%H:%M').time()
hora_salida = datetime.strptime('22:00', '%H:%M').time()
duracion_jornada = 16  # Duración de la jornada laboral de 6am a 10pm

def mostrar_matriz():
    print("***************************************")
    for i in range(0, len(espacios['vehiculos']), 10):
        fila_vehiculos = [f"{esp}({estado_espacios[esp][0]})" for esp in espacios['vehiculos'][i:i+10]]
        print('-'.join(fila_vehiculos))
    print("***************************************")
    for i in range(0, len(espacios['motos']), 10):
        fila_motos = [f"{esp}({estado_espacios[esp][0]})" for esp in espacios['motos'][i:i+10]]
        print('-'.join(fila_motos))
    print("***************************************")

def calcular_tarifa_ocupacion(hora_entrada, hora_salida, tipo_vehiculo):
    entrada = datetime.combine(datetime.today(), hora_entrada)
    salida = datetime.combine(datetime.today(), hora_salida)
    if salida < entrada:
        salida += timedelta(days=1)
    duracion = (salida - entrada).total_seconds() / 3600
    tarifa_hora = tarifa_hora_vehiculo if tipo_vehiculo.startswith('v') else tarifa_hora_moto
    costo = duracion * tarifa_hora
    if duracion > 0.7 * duracion_jornada:
        costo *= 0.85
    return round(costo)

def calcular_tarifa_alquiler(tipo_vehiculo, horas):
    tarifa_hora = tarifa_hora_vehiculo if tipo_vehiculo.startswith('v') else tarifa_hora_moto
    costo = horas * tarifa_hora
    return round(costo)

def alquilar_espacio():
    tipo = input("¿Es un vehículo o una moto? (v/m): ").lower()
    if tipo not in ['v', 'm']:
        print("Tipo no válido.")
        return

    placa = input("Ingrese la placa del vehículo: ")
    horas = float(input("Ingrese la cantidad de horas que desea alquilar: "))
    # Mostrar todos los espacios disponibles
    disponibles_vehiculos = [esp for esp in espacios['vehiculos'] if estado_espacios[esp] == 'Disponible']
    disponibles_motos = [esp for esp in espacios['motos'] if estado_espacios[esp] == 'Disponible']
    
    print("Espacios disponibles para vehículos:", ', '.join(disponibles_vehiculos))
    print("**+---------------***-----------------***")
    print("Espacios disponibles para motos:", ', '.join(disponibles_motos))

    espacio = input("Ingrese el espacio que desea alquilar: ")

    # Verificar si el espacio existe
    if espacio not in estado_espacios or estado_espacios[espacio] != 'Disponible':
        print("El espacio seleccionado no está disponible o no existe.")
        return

    # Verificar si el tipo de vehículo coincide con el espacio seleccionado
    if (tipo == 'v' and espacio.startswith('m')) or (tipo == 'm' and espacio.startswith('v')):
        print(f"El espacio {espacio} no es válido para el tipo de vehículo seleccionado.")
        return

    tarifa = calcular_tarifa_alquiler(tipo, horas)
    print(f"La tarifa de alquiler por {horas} horas es: ${tarifa}")
    confirmar = input("¿Desea confirmar el alquiler? (s/n): ").lower()
    if confirmar == 's':
        estado_espacios[espacio] = 'Alquiler(A)'
        alquiler.add(espacio)
        registro_placas[espacio] = placa
        hora_actual = datetime.now()
        registro_entrada[espacio] = hora_actual
        print(f"El espacio {espacio} ha sido alquilado para la placa {placa} por {horas} horas.")
        print(f"Hora de inicio del alquiler: {hora_actual.strftime('%Y-%m-%d %H:%M:%S')}")
        mostrar_matriz()
 
def facturar_alquiler():
    espacio = input("Ingrese el espacio a facturar: ")
    if espacio not in alquiler:
        print("Este espacio no está en alquiler.")
        return
    tipo_vehiculo = espacio[0]
    hora_entrada = registro_entrada[espacio]
    hora_actual = datetime.now()
    horas_transcurridas = (hora_actual - hora_entrada).total_seconds() / 3600
    tarifa = calcular_tarifa_alquiler(tipo_vehiculo, horas_transcurridas)
    print(f"Espacio: {espacio}")
    print(f"Placa: {registro_placas[espacio]}")
    print(f"Hora de entrada: {hora_entrada.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hora de salida: {hora_actual.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"La tarifa de alquiler es: ${tarifa}")
    confirmar = input("¿Desea finalizar el alquiler? (s/n): ").lower()
    if confirmar == 's':
        alquiler.remove(espacio)
        estado_espacios[espacio] = 'Disponible'
        del registro_placas[espacio]
        del registro_entrada[espacio]
        print(f"El alquiler del espacio {espacio} ha sido finalizado.")
        mostrar_matriz()

def registrar_entrada():
    tipo = input("¿Es un vehículo o una moto? (v/m): ").lower()
    if tipo not in ['v', 'm']:
        print("Tipo no válido.")
        return

    placa = input("Ingrese la placa del vehículo: ")
    #Muestra los espacios disponibles para vehículos y motos
    disponibles_vehiculos = [esp for esp in espacios['vehiculos'] if estado_espacios[esp] == 'Disponible']
    disponibles_motos = [esp for esp in espacios['motos'] if estado_espacios[esp] == 'Disponible']
    
    print("Espacios disponibles para vehículos:", ', '.join(disponibles_vehiculos))
    print("Espacios disponibles para motos:", ', '.join(disponibles_motos))

    espacio = input("Ingrese el espacio que desea ocupar: ")

    # Verificamos si el espacio existe
    if espacio not in estado_espacios or estado_espacios[espacio] != 'Disponible':
        print("El espacio seleccionado no está disponible o no existe.")
        return

    # Verificamos si el tipo de vehículo coincide con el espacio seleccionado
    if (tipo == 'v' and espacio.startswith('m')) or (tipo == 'm' and espacio.startswith('v')):
        print(f"El espacio {espacio} no es válido para el tipo de vehículo seleccionado.")
        return

    estado_espacios[espacio] = 'Ocupado(O)'
    hora_actual = datetime.now().time()
    registro_entrada[espacio] = hora_actual
    registro_placas[espacio] = placa
    print(f"El espacio {espacio} ha sido ocupado por la placa {placa}. Hora de entrada: {hora_actual.strftime('%H:%M')}")
    mostrar_matriz()

def facturar_salida():
    espacio = input("Ingrese el espacio a facturar: ")
    if estado_espacios[espacio] != 'Ocupado(O)':
        print("Este espacio no está ocupado.")
        return
    hora_entrada = registro_entrada[espacio]
    hora_salida = datetime.now().time()
    tipo_vehiculo = espacio[0]
    tarifa = calcular_tarifa_ocupacion(hora_entrada, hora_salida, tipo_vehiculo)
    print(f"La tarifa para el espacio {espacio} es: ${tarifa}")
    print(f"Hora de entrada: {hora_entrada.strftime('%H:%M')}")
    print(f"Hora de salida: {hora_salida.strftime('%H:%M')}")
    confirmar = input("¿Desea confirmar la salida? (s/n): ").lower()
    if confirmar == 's':
        estado_espacios[espacio] = 'Disponible'
        del registro_entrada[espacio]
        del registro_placas[espacio]
        print(f"El vehículo ha salido del espacio {espacio}.")
        mostrar_matriz()

def informe_espacios():
    print("Espacios alquilados:")
    for esp in alquiler:
        print(f"{esp}: Placa {registro_placas[esp]}")
    print("\nEspacios ocupados:")
    for esp, estado in estado_espacios.items():
        if estado == 'Ocupado(O)':
            print(f"{esp}: Placa {registro_placas[esp]}")

def menu():
    while True:
        print("""
        1. Mostrar matriz del parqueadero
        2. Alquilar (entrada del v/m por placa y tipo)
        3. Facturar alquiler v/m
        4. Registrar entrada (v/m ocupado por placa y tipo)
        5. Facturar salida de v/m (ocupado)
        6. Informe espacios alquilados u ocupados
        7. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            mostrar_matriz()
        elif opcion == '2':
            alquilar_espacio()
        elif opcion == '3':
            facturar_alquiler()
        elif opcion == '4':
            registrar_entrada()
        elif opcion == '5':
            facturar_salida()
        elif opcion == '6':
            informe_espacios()
        elif opcion == '7':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

print("Bienvenido al Administrador del Parqueadero")
menu()