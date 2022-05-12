from pprint import pprint
import requests
import json


def getAllUsers():
    key="users"
    url="https://springbootusers.herokuapp.com/" + key

    response = requests.get(url)
    data = response.json()
    pprint(data)
    return data

#getAllUsers()

def getUser(id):
    key="user/"
    url="https://springbootusers.herokuapp.com/" + key + str(id)

    response = requests.get(url)
    
    data = response.json()
    print(data)
    return data

#getUser(4)

def getUserByEmail(email):
    key="users"
    url="https://springbootusers.herokuapp.com/" + key

    response = requests.get(url)
    data = response.json()
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
    
    return data
        
#getUserByEmail("brandonsepux@gmail.com");

def login(email, password):
    key="users"
    url="https://springbootusers.herokuapp.com/" + key

    response = requests.get(url)
    data = response.json()

    for i in data:
        #print(i["email_user"])
        if i["email_user"] == email and i["pass_user"] == password:
            print("lo encontre, usuario logueado")
            data = i
            pprint(data)
            break
            
        else:
           print("NO lo encontre, clave o email incorrectos")
           data = False
           pprint(data)
           break
    return data 
    
#login("brandonsepux@gmail.com", "cesariño")

def loadUser(nom_user,rut_user,age_user,tipo_user,email_user,pass_user):
    
    url="https://springbootusers.herokuapp.com/load"
    try:
        dato = {"nom_user":"vanesita","rut_user":"20447641-2","age_user":"21","tipo_user":"bodeguera","email_user":"val11e@gmail.com","pass_user":"vane"}
        response = requests.post(url, json = dato )
        print("se logró"+ str(response)) 
    except Exception as e:
        print("No se logró")
        print(e)
        data = False
        pprint(data)
    return  response  

#loadUser("Vanesia","243126141-2","21","bodeguera","val11e@gmail.com","vane")  
getAllUsers()
