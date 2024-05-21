import requests
url="http://servizos.meteogalicia.gal/rss/observacion/observacionConcellos.action"

respuesta=requests.get(url)

d=respuesta.json()

listaConcellos=d["listaObservacionConcellos"]

ciudades=["Vigo","Pontevedra","Santiago de Compostela","Ourense","A Coruña","Lugo","Ferrol"]
for elemento in listaConcellos:
    if elemento["nomeConcello"] in ciudades:
        print(elemento["nomeConcello"],elemento["temperatura"],"ºC")