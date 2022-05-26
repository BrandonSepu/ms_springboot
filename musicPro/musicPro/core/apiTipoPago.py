from pprint import pprint
import requests
import json


def getAllTipoPago():
    try:
        key="tipoPagos"
        url="https://springbootventas.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            #pprint(data)
            #print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

#getAllTipoPago()

def getTipoPago(id):

    try:
        url="https://springbootventas.herokuapp.com/tipoPago/"+ str(id)
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

#getTipoPago(1)

def getTipoPagoby(detalle):  #NO REALIZADA
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

def loadTipoPago(pago_tpag):
    try:
        url="https://springbootventas.herokuapp.com/loadTipoPago"
        respuesta = False
    
        if len(pago_tpag) <= 20:
            dato = {"pago_tpag": pago_tpag}
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
      
#loadTipoPago("cheque")  

def updateTipoPago(id_tpag,pago_tpag):
    try:
        url="https://springbootventas.herokuapp.com/updateTipoPago"
        respuesta = False
    
        if len(pago_tpag) <= 100:
            dato = {'id_tpag': id_tpag,"pago_tpag":pago_tpag}
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

#getAllTipoPago()
#updateTipoPago(34,"cheque")

def delTipoPagoById(id):
    try:
        data = getTipoPago(id)
        respuesta = False
        url="https://springbootventas.herokuapp.com/delTipoPago/" + str(id)
        if id >= 0:
            respuesta = requests.delete(url)
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta) + " eliminaste a la venta: " + data["pago_tpag"])
                print("se logró")
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("id no encontrada = "+id)
        
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)

#delTipoPagoById(24)
#getTipoPago(5)
#getAllTipoPago()
    

    
