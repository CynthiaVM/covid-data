from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "98681c991fmshf6843598095047fp1b8661jsn103fbe67bddd"
    }

response = requests.request("GET", url, headers=headers).text
response = json.loads(response)
response = response["response"]

countries = []
for r in response:
    countries.append(r['country'])
countries.sort()

def home(request):
    if request.method=='POST':
        pais = request.POST['selectedcountry']
    return render(request, 'core/index.html', {'countries': countries, 'pais': pais if request.method=='POST' else '' })

