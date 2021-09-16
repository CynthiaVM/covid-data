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
#lista por compresion, otra manera de consulta y comprimir un poco de codigo

#countries= []

countries= [dato["country"] for dato in response] #lista de compresion

countries.sort()

#countries = []
#for r in response:
    #countries.append(r['country'])
#countries.sort()

def home(request):
    if request.method=='POST':
        pais = request.POST['selectedcountry']
        for i in response:
            if pais==i["country"]: #saca la data y la muestra en la terminal
                #pprint.pprint(i)
                new=i["cases"]["new"]
                active= i["cases"]["active"]
                critical= i["cases"]["critical"]
                recovered=i["cases"]["recovered"]
                total= i["cases"]["total"]
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

    return render(request, 'core/index.html', {'countries': countries})

