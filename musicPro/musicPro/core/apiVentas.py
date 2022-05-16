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

def getUserByEmail(email):
    try:
        key="users"
        url="https://springbootusers.herokuapp.com/" + key
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

def loadVenta(product_id,user_id,detalle_ven_id_detven):
    try:
        url="https://springbootusers.herokuapp.com/load"
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
      

#loadUser("Vanesuki","21126141-2","21")  

def updateUser(id_user,nom_user,rut_user,age_user,tipo_user,email_user,pass_user):
    try:
        url="https://springbootusers.herokuapp.com/update"
        respuesta = False
    
        if len(rut_user) <= 10:
            dato = {'id_user': id_user,"nom_user":nom_user,"rut_user":rut_user,"age_user":age_user,"tipo_user":tipo_user,"email_user":email_user,"pass_user":pass_user}
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

#getAllUsers()
#updateUser(94,'vanesita','20447641-2',21,'bodeguera','val11e@gmail.com','vane',)
#updateUser(94,'vanesita','20447641-2',23,'vendedora','val11e@gmail.com','vane',)

def delUserById(id):
    try:
        data = getUser(id)
        respuesta = False
        url="https://springbootusers.herokuapp.com/dUser/" + str(id)
        if id >= 0:
            respuesta = requests.delete(url)
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta) + " eliminste a : " + data["nom_user"])
                print("se logró")
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("id no encontrada = "+id)
        
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)

#delUserById(74)
#getUser(4)
#getAllUsers()
    
    