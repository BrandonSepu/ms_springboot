from pprint import pprint
import requests
import json


def getAllBodega():
    try:
        key="bodega"
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

#getAllBodega()

def getBodega(id):
    
    try:
        url="https://springbootproductos.herokuapp.com/bodega/"+ str(id)
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

#getBodega(2)

def getProByBodega(product):
    try:
        key="bodega"
        url="https://springbootproductos.herokuapp.com/" + key
        data=False
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            for i in data:
                print(i["producto_id"])
                if i["producto_id"] == product:
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
        
#getProByBodega(1); 

def loadBodega(producto_id,stock_bod):
    try:
        url="https://springbootproductos.herokuapp.com/loadInBodega"
        respuesta = False
    
        if len(pric_pro) <= 10:
            dato = {"producto_id":producto_id,"stock_bod":stock_bod}
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
      

#loadProducto("batería","Con sonidos fuertes, marca Electric","70.000","1")  

def updateProducto(id_pro,nom_pro,des_pro,pric_pro,tipo_id_tipo):
    try:
        url="https://springbootproductos.herokuapp.com/updateBodega"
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
#updateProducto("14","batería1","Con sonidos chi fuertisimos marca Electric","70.000","1")

def delProductoById(id):
    try:
        data = getProducto(id)
        respuesta = False
        url="https://springbootproductos.herokuapp.com/delBoPro/" + str(id)
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

#delProductoById(34)
#getProducto(4)
#getAllPro()
    
    


