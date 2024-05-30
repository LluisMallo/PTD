import serial
from datetime import datetime

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/ttyUSB0"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

while True:
    lectura_1 = cansat.readline().decode('Ascii').rstrip("\r\n")
    print(lectura_1)

saber_estat=lectura_1.split("#")
estat=saber_estat[0]
lectura=saber_estat[1]
while estat=="3":
    
    #separa cada valor per les comes i ho guarda en una llista
    dades = lectura.split(',')
    print(dades)

    #Així podem accedir a cada valor i guardar-lo en una variable
    dada1 = dades[0]
    dada2 = int(dades[1]) # Les dades són un text, per tant, s'han de convertir al tipus que volem
    dada3 = dades[2]
    dada4 = float(dades[3]) 
    dada5 = dades[4]

    print(f"Dada 1: {dada1}")
    print(f"Dada 2: {dada2}")
    print(f"Dada 3: {dada3}")
    print(f"Dada 4: {dada4}")
    print(f"Dada 5: {dada5}")
