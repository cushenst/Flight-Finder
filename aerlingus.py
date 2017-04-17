#Stephen Cushen 2017

from bs4 import BeautifulSoup
import requests 
import urllib
import json
import math
airport_data = json.loads(open('airports.json').read())
def iata(name):
	for i in range(len(airport_data)):
		if airport_data[i]['name']:
			if name in airport_data[i]['name']:
				return airport_data[i]['iata']
		else:
			pass
orign = input().title()
orign = iata(orign)
destination = input().title()
destination = iata(destination)
d_date = '2017-06-14'
a_date = '2017-06-14'
adult = 1
teen = 0
child = 0
infants = 0

data = {"flightJourneySearches":[{"sourceAirportCode":orign,"destinationAirportCode":destination,"departureDate":d_date},{"sourceAirportCode":destination,"destinationAirportCode":orign,"departureDate":a_date}],"fareType":"RETURN","fareCategory":"ECONOMY","numAdults":adult,"numYoungAdults":teen,"numChildren":child,"numInfants":infants,"promoCode":"","groupBooking":"false"}
data = json.dumps(data).encode('utf8')
url = requests.post('https://www.aerlingus.com/api/search/fixedFlight',data=data,headers={'content-type': 'application/json'})
if url.text != '':
	rec_data = json.loads(url.text)
	low = float(math.inf)
	for i in range(len(rec_data['data'][0]['flightOptions'][0]['airJourney'])):
		if float(rec_data['data'][0]['flightOptions'][0]['airJourney'][i]['lowPrice']) < float(low):
			low = float(rec_data['data'][0]['flightOptions'][0]['airJourney'][i]['lowPrice'])
			date_arr = rec_data['data'][0]['flightOptions'][0]['airJourney'][i]['arrivalDateTimeStr']
			date_depart = rec_data['data'][0]['flightOptions'][0]['airJourney'][i]['departDateTimeStr']

	print(low)
	print(date_depart,date_arr)

else:
	print('No Flights found')

