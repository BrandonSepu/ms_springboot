from pprint import pprint
import requests
import json


def getAllVentas():
    try:
        key="ventas"
        url="https://springbootventas.herokuapp.com/" + key
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

#getAllVentas()

def getVenta(id):

    try:
        url="https://springbootventas.herokuapp.com/venta/"+ str(id)
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

#getVenta(1)

def gettVentaByDetalle(detalle):
    try:
        key="ventas"
        url="https://springbootventas.herokuapp.com/" + key
        data=False
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            for i in data:
                if i["detalle_ven_id_detven"] == detalle:
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
        
#gettVentaByDetalle(2);

def loadVenta(product_id,user_id,detalle_ven_id_detven):
    try:
        url="https://springbootventas.herokuapp.com/loadInVenta"
        respuesta = False
    
        if len(product_id) <= 10:
            dato = {"product_id": product_id,"user_id": user_id,"detalle_ven_id_detven": detalle_ven_id_detven}
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
      
#loadVenta("24",24,4)  

def updateVenta(id_ventas,product_id,user_id,detalle_ven_id_detven):
    try:
        url="https://springbootventas.herokuapp.com/updateVenta"
        respuesta = False
    
        if len(id_ventas) <= 10:
            dato = {'id_ventas': id_ventas,"product_id":product_id,"user_id":user_id,"detalle_ven_id_detven":detalle_ven_id_detven}
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

#getAllVentas()
#updateVenta("1","2","84","1")

def delVentaById(id):
    try:
        data = getVenta(id)
        respuesta = False
        url="https://springbootventas.herokuapp.com/delVenta/" + str(id)
        if id >= 0:
            respuesta = requests.delete(url)
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta) + " eliminaste a la venta: " + data["id_ventas"])
                print("se logró")
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("id no encontrada = "+id)
        
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)

#delVentaById(4)
#getVenta(4)
#getAllVentas()
    

    
