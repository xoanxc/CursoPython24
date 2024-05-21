# Lista con elementos de diferentes tipos
lista = [3, "perro", (2, 3)]

for elemento in lista:
    print(elemento, " Tipo de dato:", type(elemento))

print(lista[1][:4])  # 'perr'
print(lista[2])  # (2, 3)
print(lista[2][0])  # 2

# Diccionario
dic = {
    "forma": "cuadrado",
    "color": "rojo",
    "lado": 10
}

print(dic["forma"])  # 'cuadrado'
print(dic["color"])  # 'rojo'
print(dic.keys())  # dict_keys(['forma', 'color', 'lado'])
print(dic.values())  # dict_values(['cuadrado', 'rojo', 10])
print(dic.items())  # dict_items([('forma', 'cuadrado'), ('color', 'rojo'), ('lado', 10)])

for elemento in dic.items():
    if "rojo" == str(elemento[1]):
        print(elemento[0])  # 'color'

# Manejo de claves inexistentes en un diccionario
try:
    print(dic["radio"])
except KeyError as e:
    print(f"Error: {e}")  # 'Error: radio'

print(dic.get("radio", 0))  # 0

# Importación de requests y obtención de datos de un servicio web
import requests

url = "http://servizos.meteogalicia.gal/rss/observacion/observacionConcellos.action"
respuesta = requests.get(url)

print(respuesta)  # <Response [200]>

d = respuesta.json()
listaConcellos = d["listaObservacionConcellos"]

print(listaConcellos[0])  # {'dataLocal': '2024-05-16T16:37:00', 'dataUTC': '2024-05-16T14:37:00', 'icoEstadoCeo': 111, 'icoVento': 306, 'idConcello': 15007, 'nomeConcello': 'A Baña', 'sensacionTermica': 11.7, 'temperatura': 11.7}

print(listaConcellos[0]["nomeConcello"], listaConcellos[0]["temperatura"], "ºC")  # 'A Baña 11.7 ºC'

# Filtrando los datos por ciudades específicas
ciudades = ["Vigo", "Pontevedra", "Santiago de Compostela", "Ourense", "A Coruña", "Lugo", "Ferrol"]
for elemento in listaConcellos:
    if elemento["nomeConcello"] in ciudades:
        print(elemento["nomeConcello"], elemento["temperatura"], "ºC")
        # 'A Coruña 14.2 ºC', 'Ferrol 13.1 ºC', 'Lugo 13.2 ºC', 'Ourense 15.9 ºC', 'Pontevedra 14.7 ºC', 'Santiago de Compostela 12.0 ºC', 'Vigo 14.2 ºC'
