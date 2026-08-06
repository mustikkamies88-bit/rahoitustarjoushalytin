import json, os
from datetime import datetime
MAX_RATE=float(os.getenv('MAX_RATE','6')); MAX_PRICE=int(os.getenv('MAX_PRICE','15000')); MAX_KM=int(os.getenv('MAX_KM','250000'))
# Ensimmäinen käyttöön otettava versio käyttää demodataa. Tähän kohtaan lisätään seuraavaksi live-parserit liike kerrallaan.
offers=[{"dealer":"J. Rinta-Jouppi","title":"Vaihtoautojen rahoituskampanja","rate":4.99,"url":"https://www.rintajouppi.fi/korkotarjous/","reason":"Korko alle 6 %, useita 7-paikkaisia automaatteja ja osa alle budjetin.","cars":[{"model":"Kia Sorento 2015","price":14900,"km":238000,"fuel":"Diesel","gearbox":"Automaatti","seats":7,"service_book":True},{"model":"Seat Alhambra","price":12900,"km":245000,"fuel":"Diesel","gearbox":"Automaatti","seats":7,"service_book":True},{"model":"VW Sharan","price":13900,"km":249000,"fuel":"Diesel","gearbox":"Automaatti","seats":7,"service_book":True}]}]
alerts=[]
for o in offers:
    cars=[c for c in o['cars'] if o['rate']<MAX_RATE and c['price']<=MAX_PRICE and c['km']<=MAX_KM and c['gearbox']=='Automaatti' and c['seats']>=7 and c.get('service_book')]
    if cars:
        o=dict(o); o['cars']=cars; o['updated']=datetime.now().strftime('%d.%m.%Y %H:%M'); alerts.append(o)
out={'updated_at':datetime.now().strftime('%d.%m.%Y %H:%M'),'alerts':alerts}
open('results.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=2))
print('alerts',len(alerts))
