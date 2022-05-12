from pprint import pprint
import requests
import json

from requests import request
import requests
import urllib3


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
        data = {'nom_user':nom_user,
                'rut_user':rut_user,
                'age_user':age_user,
                'tipo_user':tipo_user,
                'email_user':email_user,
                'pass_user':pass_user
                }
        response = requests.post(url, json = data)
        print("se logró"+ str(response))   
    except Exception as e:
        print("No se logró")
        print(e)
        data = False
        pprint(data)
    return  response  

loadUser('Vanesia','243326141-1',21,'vendedora','vane@gmail.com', 'vane')  
#getAllUsers()
