import csv
from netmiko import ConnectHandler

ip_addresses = []
usuario = input("Digite su usuario para conectarse: ")
clave = input("Por favor digite su contraseña: ")

with open('equipos_configurar.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        ip_addresses.append(row[0])

for ip in ip_addresses:
    juniper_device = {
        'device_type': 'juniper',
        'ip': ip,
        'username': usuario,
        'password': clave,
        'verbose': False,
    }

    print("Conectandose a {} ".format(ip))

    net_connect = ConnectHandler(**juniper_device)
    net_connect.send_config_from_file(config_file='equipos_configurar.txt')

    print("La configuracion fue aplicada correctamente")

    output = net_connect.send_command("show system commit")

    print(output)

print("Saliendo...")





