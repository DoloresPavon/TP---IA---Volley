import os

flag_leer = False

path = "Scout"

archivos = os.listdir(path)

for archivo in archivos:
    ruta_archivo = os.path.join(path, archivo)
    with open('CSV/'+archivo[:-4]+'.csv', "w") as archivo:
        with open(ruta_archivo, encoding='latin1') as f:
            for line in f:
                if '[3SCOUT]' in line:
                    flag_leer = True
                elif '[' in line:
                    flag_leer = False
                if flag_leer:
                    if '[3SCOUT]' not in line:
                        archivo.write(line)

