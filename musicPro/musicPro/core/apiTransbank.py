import requests

#GET ALL
def getAllAccount():
    try:
        key="account"
        url="https://springboottransbank.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            #pprint(data)
            print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

def getAllBank():
    try:
        key="bank"
        url="https://springboottransbank.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            #pprint(data)
            print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

def getAllClient():
    try:
        key="client"
        url="https://springboottransbank.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            #print(data)
            print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

def getAllBalance():
    try:
        key="balance"
        url="https://springboottransbank.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            #print(data)
            print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

#getAllAccount()
#getAllBalance()
#getAllBank()
#getAllClient()

#GET ONE
def getClient(id):
    try:
        url="https://springboottransbank.herokuapp.com/client/"+ str(id)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("se logró"+ str(respuesta))
            data = respuesta.json()
            print(str(respuesta))
            print(data)
            return data
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
    except Exception as e:
        print(e)

def getBank(id):
    try:
        url="https://springboottransbank.herokuapp.com/bank/"+ str(id)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("se logró"+ str(respuesta))
            data = respuesta.json()
            print(str(respuesta))
            print(data)
            return data
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
    except Exception as e:
        print(e)
        
def getAccount(id):
    try:
        url="https://springboottransbank.herokuapp.com/account/"+ str(id)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("se logró"+ str(respuesta))
            data = respuesta.json()
            print(str(respuesta))
            print(data)
            return data
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
    except Exception as e:
        print(e)

def getBalance(id):
    try:
        url="https://springboottransbank.herokuapp.com/balance/"+ str(id)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("se logró"+ str(respuesta))
            data = respuesta.json()
            print(str(respuesta))
            #print(data)
            return data
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
    except Exception as e:
        print(e)

#getAccount(1)

#JPA NATIVE QUERYS
def balanceByClient(idClient):
    try:
        url="https://springboottransbank.herokuapp.com/balancebyclient/"+ str(idClient)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("se logró"+ str(respuesta))
            data = respuesta.json()
            print(str(respuesta))
            #print(data)
            return data
        else:
            print(print("Funcion: balanceByClient - NO se logró, id no encontrada"+ str(respuesta)))
    except Exception as e:
        print(e)

#balanceByClient(1)

#PAGO APROBADO

def pagoAprobado(email, password, account, balance):
    status = False
    client = getAllClient()
    for c in client:
        if c["email_cli"] == email and c["pass_cli"] == password:
            status = True
            clientFound = c
            #print(clientFound)
            print("Usuario valido...")
            break
        else:
            print("usuario no encontrado")
    if clientFound:
        #print(int(clientFound["id_cli"]))
        balClient = balanceByClient(clientFound["id_cli"])
        for bc in balClient:
            if account == bc["id_acc"]["name_acc"]:
                if balance <= bc["balance_bal"]:
                    print("si alcanzas a comprar")
                else:
                    print("no te alcanza el dinero")
                break
            else:
                print("no sirve")
    else:
        status = False
    
    print(status)
    return status

pagoAprobado("dcorish0@java.com","Devi","CREDITO",1)