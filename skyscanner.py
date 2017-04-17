from bs4 import BeautifulSoup
import requests 
import urllib
import json
#url = requests.get('https://www.aerlingus.com/html/flightSearchResult.html#/sourceAirportCode_0={0}&destinationAirportCode_0={1}&departureDate_0={2}&sourceAirportCode_1={1}&destinationAirportCode_1={0}&departureDate_1={3}&fareType={4}&fareCategory=ECONOMY&numAdults={5}&numYoungAdults={6}&numChildren={7}&numInfants={8}&promoCode=&groupBooking=false'.format('dub','lon','2017-06-06','2017-06-14','RETURN','1','0','0','0'))
orign = 'DUB'
destination = 'LON'
d_date = '2017-06-06'
a_date = '2017-06-14'
adult = 1
teen = 0
child = 0
infants = 0
#data = {"flightJourneySearches":[{"sourceAirportCode":orign,"destinationAirportCode":destination,"departureDate":d_date},{"sourceAirportCode":destination,"destinationAirportCode":orign,"departureDate":a_date}],"fareType":"RETURN","fareCategory":"ECONOMY","numAdults":adult,"numYoungAdults":teen,"numChildren":child,"numInfants":infants,"promoCode":"","groupBooking":"false"}
#data = 'cabinclass=Economy&country=UK&currency=GBP&locale=en-GB&locationSchema=iata&originplace=EDI&destinationplace=LHR&outbounddate=2017-05-30&inbounddate=2017-06-02&adults=1&children=0&infants=0&apikey=st722418192322551237814021871251'

#data = urllib.parse.urlencode( data )
#data = json.dumps(data).encode('utf8')
url = requests.get('http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/IE/EUR/en-GB/DUB/LHR/2017-05-30/2017-06-02?apiKey=st722418192322551237814021871251',headers={"Content-Type" : "application/x-www-form-urlencoded"})
#url = requests.get('http://partners.api.skyscanner.net/apiservices/reference/v1.0/locales?apiKey=st722418192322551237814021871251',headers={"Content-Type" : "application/x-www-form-urlencoded"})

#url = requests.post('http://partners.api.skyscanner.net/apiservices/pricing/v1.0',data=data,headers={"Content-Type" : "application/x-www-form-urlencoded"})
print(url.text)
#rec_data = json.loads(url.text)
#for i in range(len(rec_data['data'][0]['flightOptions'][0]['airJourney'])):
#	print(rec_data['data'][0]['flightOptions'][0]['airJourney'][i]['lowPrice'])

