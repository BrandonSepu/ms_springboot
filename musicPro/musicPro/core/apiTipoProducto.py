from pprint import pprint
import requests
import json


def getAllTipoPro():
    try:
        key="tipo"
        url="https://springbootproductos.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            pprint(data)
            print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

#getAllTipoPro()

def getTipoPro(id):

    try:
        url="https://springbootproductos.herokuapp.com/tipo/"+ str(id)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            print(str(respuesta))
            print(data)
            return data
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
        
    except Exception as e:
        print(e)

#getTipoPro(4)

def getTipoProByType(tipo):
    try:
        key="tipo"
        url="https://springbootproductos.herokuapp.com/" + key
        data=False
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            for i in data:
                if i["nom_tipo"] == tipo:
                    print("lo encontre")
                    data = i
                    print(data)
                    break
                else:
                    print("NO lo encontre")
                    data = False
                    pprint(data)
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta))) 
        return data
    except Exception as e:
        print(e)
        
#getTipoProByType(4); 

def loadProducto(nom_tipo):
    try:
        url="https://springbootproductos.herokuapp.com/loadTipo"
        respuesta = False
    
        if len(nom_tipo) <= 100:
            dato = {"nom_tipo":nom_tipo}
            respuesta = requests.post(url, json = dato )
            if respuesta.status_code == 200:
                print(print("se logró"+ str(respuesta)))
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("el largo del rut excede el maximo")
    except Exception as e:
        print("No se logró")
        print(e)
        data = False
        pprint(data)
    return  respuesta
      

#loadProducto("otros2")  

def updateTipoPro(id_tipo,nom_tipo):
    try:
        url="https://springbootproductos.herokuapp.com/updateTipo"
        respuesta = False
    
        if len(nom_tipo) <= 100:
            dato = {'id_tipo': id_tipo,"nom_tipo":nom_tipo}
            respuesta = requests.put(url, json = dato )
            if respuesta.status_code == 200:
                print(print("se logró"+ str(respuesta)))
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("el largo del rut excede el maximo")
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)
        data = False
        pprint(data)
    return  respuesta  

#getAllTipoPro()
#updateTipoPro("24","otros3")

def delTipoProById(id):
    try:
        data = getTipoPro(id)
        respuesta = False
        url="https://springbootproductos.herokuapp.com/delTipo/" + str(id)
        if id >= 0:
            respuesta = requests.delete(url)
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta) + " eliminaste a : " + data["nom_tipo"])
                print("se logró")
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("id no encontrada = "+id)
        
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)

#delTipoProById(24)
#getTipoPro(4)
#getAllTipoPro()
    
    
