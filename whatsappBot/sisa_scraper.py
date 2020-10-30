import requests
import json
from tabulate import _table_formats, tabulate


def grades():
    session = requests.session()
    payload = {'usuario.nick': 'usuario', 'usuario.contrasexa': 'contraseña'}
    r=session.post('https://srvcldutez.utez.edu.mx:8443/SISAVA/iniciarSesion', data=payload)

    rr = session.get('https://srvcldutez.utez.edu.mx:8443/SISAVA/consultarHistorial')
    #print(rr)
    #print(json.loads(rr.content))

    data = json.loads(rr.content)

    mat = []
    tabla = [['Materia','U1','U2','U3','U4','U5', 'U6', 'U7', 'U8', 'U9', 'U10'],]


    clase = 0
    unit = 0
    units = len(data["consulta"][0]["clases"][clase]["materia"]["unidades"])



    while clase < 6:
        for i in data["consulta"][0]["clases"]:
            mat.append(data["consulta"][0]["clases"][clase]["materia"]["descripcion"])
        
            for x in data["consulta"][0]["clases"][clase]["materia"]["unidades"]:
                unidad = (data["consulta"][0]["clases"][clase]["materia"]["unidades"][unit]["calificacion"])
                mat.append(unidad)
    ##            print(mat)
                if unit < units:
                    unit= unit+1
            unit = 0

    ##        print(clase)
            tabla.append(mat)
    ##        print(tabla)
            mat = []
            
          
            if clase < 6:
                clase = clase+1

    return(tabulate(tabla, headers='firstrow', numalign="right"))
