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

def getProByType(tipo):
    try:
        key="productos"
        url="https://springbootproductos.herokuapp.com/" + key
        data=False
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            for i in data:
                print(i["tipo_id_tipo"])
                if i["tipo_id_tipo"] == tipo:
                    print("lo encontre")
                    data = i
                    #print(data)
                    
                else:
                    print("NO lo encontre")
                    data = False
                    #pprint(data)
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta))) 
        return data
    except Exception as e:
        print(e)
        
#getProByType(1); 

def loadProducto(nom_pro,des_pro,pric_pro,stock_pro,tipo_id_tipo,img_pro):
    try:
        url="https://springbootproductos.herokuapp.com/loadProducto"
        respuesta = False
        status = False
        
        dato = {"nom_pro":nom_pro,"des_pro":des_pro,"pric_pro":pric_pro,
        "tipo":tipo_id_tipo,"stock_pro":stock_pro, "img_pro": img_pro}
        respuesta = requests.post(url, json = dato )
        if respuesta.status_code == 200:
            print("se logró ingresar el producto"+ str(respuesta))
            status = True
        else:
            print("NO se logró Ingresar el producto "+ str(respuesta.status_code) +str(respuesta.text))
        
    except Exception as e:
        print("No se logró")
        print(e)
        data = False
        #pprint(data)
    return  status
      

#loadProducto("Guitarra","madera cahoba profesional Fender","90000",2, 12)  

def updateProducto(id_pro,nom_pro,des_pro,pric_pro,tipo_id_tipo,stock_pro,img_pro):
    try:
        url="https://springbootproductos.herokuapp.com/updateProduct"
        respuesta = False
    
        if len(pric_pro) <= 10:
            dato = {'id_pro': id_pro,"nom_pro":nom_pro,"des_pro":des_pro,
            "pric_pro":pric_pro,"tipo_id_tipo":tipo_id_tipo,"stock_pro":stock_pro,"img_pro":img_pro}
            respuesta = requests.put(url, json = dato )
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta))
            else:
                print("NO se logró, id no encontrada"+ str(respuesta))
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
        url="https://springbootproductos.herokuapp.com/delPro/" + str(id)
        
        respuesta = requests.delete(url)
        if respuesta.status_code == 200:
            print("se logró"+ str(respuesta) + " eliminaste a : " + data["nom_pro"])
            print("se logró")
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)

#delProductoById(34)
#getProducto(4)
#getAllPro()
    
