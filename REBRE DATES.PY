import serial
from datetime import datetime
import math
BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/ttyUSB0"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)
missatge=""

while True:
    lectura_1 = cansat.readline().decode('Ascii').rstrip("\r\n")
    print(lectura_1)

    saber_estat=lectura_1.split("/")
    estat=saber_estat[0] # Aqui trobarem en quin estat està actualment (Repòs)
    lectura=saber_estat[1]
    if estat=="0": # Mostram l'estat nombre 0 
        print(lectura) 
    if estat=="1": # Aqui mostrarem la lectura de l'estat 1 
        print(lectura)
    if estat=="2": # Aqui es pot veure la lectura de l'estat 2 
        print(lectura)

    if estat=="3": #Aqui entram ja dins l'estat nombre 3 
        
        #separa cada valor per les comes i ho guarda en una llista
        dades = lectura.split(',')
        print(dades)

        #Així podem accedir a cada valor i guardar-lo en una variable
        dada1 = dades[0]
        dada2 = dades[1] # Les dades són un text, per tant, s'han de convertir al tipus que volem
        dada3 = int(dades[2])
        dada4 = float(dades[3]) 
        dada5 = float(dades[4])
    
        R_AUX = 10 #kolohms

        vol_ter = 5-(5*dada3)/1023

        r_ter = (vol_ter*R_AUX)/(5-vol_ter)

        

        t= round(73.74 - 21.06*math.log(r_ter),3)#Això és la formula de el termistor per aconseguir la seva temperatura

        #El que apareix seguidament són els costants
        g = 9.80866 # La Gravetat 
        M_AIRE = 0.0289644 # Massa de l'aire 
        r = 8.3144598 
        H_0 = 0 #Altura inicial 
        P_0 = 101300 # Presió Inicial 
        T_0 = 13.2 #Altura actualment

        p=(float(dada4)) #La presió mos la donarà el BMP280 

        h= round(H_0 +((math.log (P_0/p)*r*T_0 )/(g*M_AIRE)),3) #Formula per conseguir trobar la altura



        print(f"Dada 1: {dada1}")
        print(f"Dada 2: {dada2}")
        print(f"Dada 3: {dada3}")
        print(f"Dada 4: {dada4}")
        print(f"Dada 5: {dada5}")
        print (f"Temperatura: {t}")
        print (f"Altura: {h}")

        nom_fitxer = "rebredates.csv"


        # 'a' significa 'append' i fa que afegim línies a un fitxer sense borrar lo que ja tenim
        with open(nom_fitxer, 'a') as file_object:
            file_object.write(f"{lectura}\n")
    elif estat =="4": #Entrada a l'estat nombre 4 
        dy="" #Això eés la variable. 
        codi_morse= "" #I això és la variable del codi morse. 
        
        while len(codi_morse)<4: #Serà la llargaria del codi morse. 
            while True:
                lectura_1 = cansat.readline().decode('Ascii').rstrip("\r\n")
                saber_estat=lectura_1.split("/")
                estat=saber_estat[0] # Aqui trobarem en quin estat està actualment (Repòs)
                lectura=saber_estat[1]
                if lectura =="0":
                    dy+=lectura
                else:
                    if len(dy)==0:
                        continue
                    else:
                        break
                if estat!="4":
                    break
            if len(dy) <=3:
                print(".")
                codi_morse+="."
                dy=""
            elif len(dy) >7:
                break
            else:
                print("-")
                codi_morse+="-"
                dy=""
            if estat!="4":
                    break
        codi_lletres = [".-", "-...", "-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--", "....-",".....","-....","--...","---..","----.","-----"]
        lletres= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
        contador=0
        for i in codi_lletres:
            if i == codi_morse:
                print(lletres[contador])
                missatge+=lletres[contador]
                break
            contador+=1
        if i !=codi_morse:
            print(f"El missatge es: {missatge}")
    
    elif estat =="5": # Això mostra l'estat nombre 5
         print (lectura)
    elif estat =="6": # I finalment aqui mostra l'estat nombre 6
        print(lectura)
