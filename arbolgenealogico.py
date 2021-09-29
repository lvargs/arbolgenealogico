#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Requisitos:
# pip install requests
# pip install bs4
# pip install lxml

import sys
if sys.version_info < (3,):
    print("Este script necesita Python 3 o superior.")
    sys.exit(1)

import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    raise ValueError(
        f"Por favor indique un número de cédula. Uso: {sys.argv[0]} <numcedula>")

persona = {"cedula": sys.argv[1],
           "nombre": "",
           "conocidocomo": "",
           "fechanacimiento": "",
           "nacionalidad": "",
           "edad": "",
           "marginal": ""}

padre = {"cedula": "",
         "nombre": ""}

madre = {"cedula": "",
         "nombre": ""}

url = "https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx"

session = requests.Session()

firstresponse = session.get(url=url)

headers = {"user-agent": "Mozilla",
           "content-type": "application/x-www-form-urlencoded"}
data = {"__VIEWSTATE": "/wEPDwULLTE1OTIyMjMwMDVkZK8IAFVVrLVZ94xw80rFsu4opljJCVOXUsSfBJSod1T8",
        "__EVENTVALIDATION": "/wEdAAmsgmX2ZUY16L/wbsAezXirtTfNpOz0CH4vKngBfzxDIS2hNtLCXCKq92TKMjYS4CX24YOX6Ab2AoRRJXYcN6RPZrHMfDaOuX2c5DuODJSeiypYaPycT+v9uchEvEhJB0tWvoSmUD9cccAzkkmmOR9zkJ/OtIbU04qfUHmBu0NaRFCfQQ61frM+tUgerGfangbkVNG4e7R+/Xmh2Mum3zsAWZf7AC16Gtse4KjiO5c0yg==",
        "txtcedula": persona["cedula"],
        "btnConsultaCedula": "Consultar"}

secondresponse = session.post(url=url, headers=headers, data=data)

soup = BeautifulSoup(secondresponse.content, "lxml")

persona["nombre"] = soup.find(id="lblnombrecompleto").string
persona["conocidocomo"] = soup.find(id="lblconocidocomo").string
persona["fechanacimiento"] = soup.find(id="lblfechaNacimiento").string
persona["nacionalidad"] = soup.find(id="lblnacionalidad").string
persona["edad"] = soup.find(id="lbledad").string
persona["marginal"] = soup.find(id="lblLeyendaMarginal").string
padre["cedula"] = soup.find(id="lblid_padre").string
padre["nombre"] = soup.find(id="lblnombrepadre").string
madre["cedula"] = soup.find(id="lblid_madre").string
madre["nombre"] = soup.find(id="lblnombremadre").string

print('\n')
print("Datos de la persona consultada:")
print("Cédula: {}".format(persona["cedula"]))
print("Nombre completo: {}".format(persona["nombre"]))
print("Conocido como: {}".format(persona["conocidocomo"]))
print("Fecha de nacimiento: {}".format(persona["fechanacimiento"]))
print("Nacionalidad: {}".format(persona["nacionalidad"]))
print("Edad: {}".format(persona["edad"]))
print("Es marginal: {}".format(persona["marginal"]))
print("Cédula del padre: {}".format(padre["cedula"]))
print("Nombre del padre: {}".format(padre["nombre"]))
print("Cédula de la madre: {}".format(madre["cedula"]))
print("Nombre de la madre: {}".format(madre["nombre"]))
