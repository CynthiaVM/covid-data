from django.shortcuts import render
import requests
import pprint

from requests.models import Response

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "98681c991fmshf6843598095047fp1b8661jsn103fbe67bddd"
    }

response = requests.request("GET", url, headers=headers).json()
#response = json.loads(response)
response = response["response"]
# lista por compresion, otra manera de consulta y comprimir un poco de codigo. 
#json es un formato de intercambio de datos de facil lectura y escritura.Actualiza sin actualizar la pag.

#countries= []

countries= [dato["country"] for dato in response] #lista de compresion

countries.sort()

#countries = []
#for r in response:
    #countries.append(r['country'])
#countries.sort()

def home(request):
    if request.method=='POST': #solicitud de formulario, compara.
        pais = request.POST["selectedcountry"]
        for i in response:
            if pais==i["country"]: #saca la data y la muestra en la terminal
                #pprint.pprint(i)
                new=i["cases"]["new"]if i['cases']['new'] else '-'
                active= i["cases"]["active"]if i['cases']['active'] else '-'
                critical= i["cases"]["critical"]if i['cases']['critical'] else '-'
                recovered=i["cases"]["recovered"]if i['cases']['recovered'] else '-'
                total= i["cases"]["total"]if i['cases']['total'] else '-'
                deaths= int(total)- int(active)- int(recovered)
        context=  {   
            "new":new,
            "active": active,
            "critical": critical,
            "recovered": recovered,
            "total": total, 
            "deaths": deaths,
            "pais": pais,
            "countries":countries,
            }   
        return render(request, "core/index.html", context=context)

    return render(request, "core/index.html", {"countries": countries})

