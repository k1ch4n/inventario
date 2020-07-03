import os
import re
from tabulate import tabulate

ejemplo_dir = 'C:/Users/Nirqa/Documents/trabajos_python/tarea2_nirqa_devnet/Shows_Inventario' #aca poner la ruta del directorio en la cual pondran sus logs
contenido = os.listdir(ejemplo_dir)
Shows_Runs = []
for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.txt'):
        Shows_Runs.append(fichero)
print(Shows_Runs)

print('Tenemos en el inventario '+str(len(Shows_Runs))+' equipos')


'''
for i in range(len(Shows_Runs)):
    k = Shows_Runs[i]
    print('leyendo archivo ',k)

    with open(k,'r') as file:
        #print(file.readlines(), end= '\n'*3)
        #print(type(file.readlines()))
        l = file.readlines()
        print('buscando modelo ')
        '''

'''
        
        for j in range(len(l)):
            #print(l[j])
            
            m = re.search('Cisco IOS-XE', l[j]  )
            
            

            if m == None:
                continue
            else:
                print(m.group(0))
                
                data_modelo = m.group(0)
                break
'''

modelos = {}
def mod_ios():
    for i in range(len(Shows_Runs)):
        k = Shows_Runs[i]
        ###print('leyendo archivo ',k)

        with open(k,'r') as file:
            #print(file.readlines(), end= '\n'*3)
            #print(type(file.readlines()))
            l = file.readlines()
            ####print('el modelo es ')
            
            for j in range(len(l)):
                #print(l[j])

                patrones = ['Cisco IOS-XE','Cisco Nexus']
                for pp in range(len(patrones)):
                    mm = re.search(patrones[pp], l[j])
            
                #m = re.search('Cisco IOS-XE', l[j])
            
            

                    if mm == None:
                        continue
                    else:
                    #print(m.group(0))
                
                        data_modelo = mm.group(0)
                        modelos[str(k)] = data_modelo
                        break
    ###print(data_modelo)
        
#_________________________
hosts = {}
def get_hosts():
    for i in range(len(Shows_Runs)):
        k = Shows_Runs[i]
        #print('leyendo archivo ',k)

        with open(k,'r') as file:
            #print(file.readlines(), end= '\n'*3)
            #print(type(file.readlines()))
            l = file.readlines()
            #print('el nombre del equipo es ')
            
            for j in range(len(l)):
                #print(l[j])

                patrones = [r"^(\S+).*#"]
                for pp in range(len(patrones)):
                    mm = re.search(patrones[pp], l[j])
            
                #m = re.search('Cisco IOS-XE', l[j])
            
            

                    if mm == None:
                        continue
                    else:
                    #print(m.group(0))
                
                        data_hosts = mm.group(1)
                        hosts[str(k)] = data_hosts
                        break
    #print(data_hosts)

##


#__________________________

#haciendo copy paste para llenar tabla:

OsVersion = {}
def get_OsVersion():
    for i in range(len(Shows_Runs)):
        k = Shows_Runs[i]
        #print('leyendo archivo ',k)

        with open(k,'r') as file:
            #print(file.readlines(), end= '\n'*3)
            #print(type(file.readlines()))
            l = file.readlines()
            #print('el nombre del equipo es ')
            
            for j in range(len(l)):
                #print(l[j])

                patrones = [r"^Cisco.*\, Version (\S+),.*$",".*NXOS: version.* (\S+)"]
                for pp in range(len(patrones)):
                    mm = re.search(patrones[pp], l[j])
            
                #m = re.search('Cisco IOS-XE', l[j])
            
            

                    if mm == None:
                        continue
                    else:
                    #print(m.group(0))
                
                        data_OsVersion = mm.group(1)
                        OsVersion[str(k)] = data_OsVersion
                        break
#aca teriana copy paste
#_________________________________________

##############

#__________________________

#haciendo copy paste para llenar tabla:

SerialN = {}
def get_SerialN():
    for i in range(len(Shows_Runs)):
        k = Shows_Runs[i]
        #print('leyendo archivo ',k)

        with open(k,'r') as file:
            #print(file.readlines(), end= '\n'*3)
            #print(type(file.readlines()))
            l = file.readlines()
            #print('el nombre del equipo es ')
            
            for j in range(len(l)):
                #print(l[j])

                patrones = [".*Processor Board ID.* (\S+).*","^Processor board ID.* (\S+).*"]
                for pp in range(len(patrones)):
                    mm = re.search(patrones[pp], l[j])
            
                #m = re.search('Cisco IOS-XE', l[j])
            
            

                    if mm == None:
                        continue
                    else:
                    #print(m.group(0))
                
                        data_SerialN = mm.group(1)
                        SerialN[str(k)] = data_SerialN
                        break
#aca teriana copy paste
#_________________________________________

Uptime = {}
def get_Uptime():
    for i in range(len(Shows_Runs)):
        k = Shows_Runs[i]
        #print('leyendo archivo ',k)

        with open(k,'r') as file:
            #print(file.readlines(), end= '\n'*3)
            #print(type(file.readlines()))
            l = file.readlines()
            #print('el nombre del equipo es ')
            
            for j in range(len(l)):
                #print(l[j])

                patrones = [r".*uptime is (\S.*)"]
                for pp in range(len(patrones)):
                    mm = re.search(patrones[pp], l[j])
            
                #m = re.search('Cisco IOS-XE', l[j])
            
            

                    if mm == None:
                        continue
                    else:
                    #print(m.group(0))
                
                        data_Uptime = mm.group(1)
                        Uptime[str(k)] = data_Uptime
                        break

#more copy
#_____________________________                   
mod_ios()
#print(modelos)
get_hosts()
#print(hosts)
get_OsVersion()
#print(hosts['nx1_show_ver.txt'])
#print(data_modelo)
get_SerialN()
get_Uptime()
#____________
data=[]
for pp in Shows_Runs:
    #print(pp)
    data= data + [[hosts[pp],modelos[pp],OsVersion[pp],SerialN[pp],Uptime[pp]]]
    #print(data)

    
headers = ['Hostname','Platform', 'OS Version', 'Serial Number', 'Uptime']

print(tabulate(data, headers, tablefmt="grid"))
