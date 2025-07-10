vlan = int(input("Buenas, ingrese el número de VLAN: "))

if 1 <= vlan <= 1005:
    print("Esta es una VLAN Normal (Estandar).")
elif 1006 <= vlan <= 4094:
    print("Esta es una VLAN Extendida.")
else:
    print("Número de VLAN invalido, ingreso un número valido (1-4094).")