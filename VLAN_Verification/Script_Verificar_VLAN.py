import csv
from netmiko import ConnectHandler

# Declaracion de variables

serials = []
ports = []
serials_master = []
ip_addresses_master = []
hostnames_master = []
indexes = []
ip_addresses = []
hostnames = []

# Obtener direccion IP basado en la lista de devices que se quieren verificar y el Inventario

with open('devices_to_verify.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        serials.append(row[0])
        ports.append(row[1])

with open('Inventario.csv') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    for row in csv_reader2:
        serials_master.append(row[11])
        ip_addresses_master.append(row[4])
        hostnames_master.append(row[3])

for serial in serials:
    if serial in serials_master:
        indexes.append(serials_master.index(serial))

for index in indexes:
    ip_addresses.append(ip_addresses_master[index])
    hostnames.append(hostnames_master[index])

# Conectarse a los devices en la lista de IPs, y correr los comandos de verificacion que se quieren

for ip in ip_addresses:
    
    juniper_switch = {
        'device_type': 'juniper',
        'ip': ip,
        'username': 'testadmin',
        'password': 'testpass',
        'verbose': False,
    }

    print("Connecting to device {}".format(hostnames[ip_addresses.index(ip)]))

    connect_lab = ConnectHandler(**juniper_switch)

    output = connect_lab.send_command("show configuration interfaces | display set | match 0/0/{} | match vlan".format(ports[ip_addresses.index(ip)]))

    print(output)

# Guardar el output del comando en un archivo txt

"""
print(output)
    f = open('whatevs.txt', 'w')
    f.write(output)
    f.close()
"""