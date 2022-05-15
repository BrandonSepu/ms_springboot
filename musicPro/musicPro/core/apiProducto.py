from pprint import pprint
import requests
import json


def getAllPro():
    try:
        key="productos"
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

#getAllPro()

def getProducto(id):

    try:
        url="https://springbootproductos.herokuapp.com/productos/"+ str(id)
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

#getProducto(4)

def getUserByType(email):
    try:
        key="productos"
        url="https://springbootproductos.herokuapp.com/" + key
        data=False
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            for i in data:
                print(i["email_user"])
                if i["email_user"] == email:
                    print("lo encontre")
                    data = i
                    print(data)
                    break
                else:
                    print("NO lo encontre")
                    data = False
                    pprint(data)
                    break
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta))) 
        return data
    except Exception as e:
        print(e)
        
#getUserByEmail("brandonsepux@gmail.com");


def loadProducto(nom_pro,des_pro,pric_pro,tipo_id_tipo):
    try:
        url="https://springbootproductos.herokuapp.com/loadProducto"
        respuesta = False
    
        if len(pric_pro) <= 10:
            dato = {"nom_pro":nom_pro,"des_pro":des_pro,"pric_pro":pric_pro,"tipo_id_tipo":tipo_id_tipo}
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
      

loadProducto("batería","Con sonidos fuertes, marca Electric","70.000","1")  

def updateProducto(id_pro,nom_pro,des_pro,pric_pro,tipo_id_tipo):
    try:
        url="https://springbootproductos.herokuapp.com/updateProduct"
        respuesta = False
    
        if len(pric_pro) <= 10:
            dato = {'id_pro': id_pro,"nom_pro":nom_pro,"des_pro":des_pro,"pric_pro":pric_pro,"tipo_id_tipo":tipo_id_tipo}
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

#getAllPro()
#updateProducto(94,'vanesita','20447641-2',21,'bodeguera','val11e@gmail.com','vane',)
#updateProducto(94,'vanesita','20447641-2',23,'vendedora','val11e@gmail.com','vane',)

def delProductoById(id):
    try:
        data = getProducto(id)
        respuesta = False
        url="https://springbootproductos.herokuapp.com/delPro/" + str(id)
        if id >= 0:
            respuesta = requests.delete(url)
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta) + " eliminaste a : " + data["nom_pro"])
                print("se logró")
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("id no encontrada = "+id)
        
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)

#delProductoById(4)
#getProducto(4)
#getAllPro()
    
    
