import random
from django.shortcuts import render
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
import requests

def webpay_plus_create():
    try:
        url = 'https://webpay3g.transbank.cl'
        respuesta = requests.get(url)
        print(respuesta.status_code)
        if respuesta.status_code == 200:
            data = respuesta.json()
            #pprint(data)
            print(print("se logró"+ str(respuesta)))
            return data
        else:
            print(print("NO se logró" + str(respuesta)))
    except Exception as e:
        print(e)
    

#webpay_plus_create()

## Versión 3.x del SDK
# Webpay Plus
from transbank.webpay.webpay_plus.transaction import Transaction

tx = Transaction(WebpayOptions("commercecode", "apikey", IntegrationType.LIVE))
# Oneclick
from transbank.webpay.oneclick.mall_inscription import MallInscription
from transbank.webpay.oneclick.mall_transaction import MallTransaction

ins = MallInscription(WebpayOptions("commercecode", "apikey", IntegrationType.LIVE))
tx = MallTransaction(WebpayOptions("commercecode", "apikey", IntegrationType.LIVE))
# Transaccion Completa
from transbank.webpay.transaccion_completa.transaction import Transaction

tx = Transaction(WebpayOptions("commercecode", "apikey", IntegrationType.LIVE))
# Transaccion Completa Mall
from transbank.webpay.transaccion_completa.mall_transaction import MallTransaction

tx = MallTransaction(WebpayOptions("commercecode", "apikey", IntegrationType.LIVE))

## Versión 2.x del SDK

# Webpay Plus
WebpayPlus.configure_for_production('commerce_code', 'apikey')

# Oneclick
from transbank import oneclick as BaseOneClick
from transbank.common.integration_type import IntegrationType

BaseOneClick.commerce_code = "commercecode"
BaseOneClick.api_key = "apikey"
BaseOneClick.integration_type = IntegrationType.LIVE

# Transaccion Completa
from transbank import transaccion_completa as BaseTransaccionCompleta
from transbank.common.integration_type import IntegrationType

BaseTransaccionCompleta.commerce_code = "commercecode"
BaseTransaccionCompleta.api_key = "apikey"
BaseTransaccionCompleta.integration_type = IntegrationType.LIVE