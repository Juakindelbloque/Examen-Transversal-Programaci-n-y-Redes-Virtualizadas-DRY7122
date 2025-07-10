from geopy.distance import geodesic


santiago = (-33.4511975670156, -70.67224417792927)
bariloche = (-41.14054138836147, -71.30996240350743)


while True:
    print("\n--- Calculadora de Distancias Chile - Argentina ---")
    print("Ingrese 's' en cualquier momento para salir.")
    
    origen = input("Ciudad de Origen (Santiago): ")
    if origen.lower() == 's':
        break
    
    destino = input("Ciudad de Destino (Bariloche): ")
    if destino.lower() == 's':
        break


    if origen.lower() == "santiago" and destino.lower() == "bariloche":
        distancia_km = geodesic(santiago, bariloche).kilometers
        distancia_millas = geodesic(santiago, bariloche).miles
    else:
        print("Solo disponible: Santiago -> Bariloche")
        continue

    print("Medios disponibles: auto, avion")
    transporte = input("Ingrese medio de transporte: ")
    if transporte.lower() == 's':
        break

    if transporte == "auto":
        velocidad = 80
    elif transporte == "avion":
        velocidad = 800
    else:
        print("Transporte no válido.")
        continue

    duracion = distancia_km / velocidad

    print(f"\nDesde {origen.title()} hasta {destino.title()}:")
    print(f"- Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"- Medio de transporte: {transporte}")
    print(f"- Duración aproximada: {duracion:.2f} horas")

print("Programa finalizado.")