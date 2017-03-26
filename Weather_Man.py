#!/usr/bin/env python
# encoding: utf-8

import urllib2
import json

key = "xxxxxxxxxxxxxxxx"	#put Your Wunderground API Key here
zip = "90210"			#Put your ZipCode here because this is a terrible show
x = 1

while x == 1:	#This Loop is for the Current Conditions outside at the Predetermined Zipcode

	url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/' + zip + '.json'
	f = urllib2.urlopen(url)
	json_string = f.read()
	parsed_json = json.loads(json_string)
	station = parsed_json['current_observation']['station_id']
	city = parsed_json['location']['city']
	state = parsed_json['location']['state']
	weather = parsed_json['current_observation']['weather']
	temperature_string = parsed_json['current_observation']['temperature_string']
	feelslike_string = parsed_json['current_observation']['feelslike_string']
	print 'Reporting from Weather Station: ' + station + '. Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.'
	f.close()
	x=0

while x==0:	#this is the Loop for the 3 day Forecast
	
	url2 = 'http://api.wunderground.com/api/' + key + '/forecast/q/' + zip + '.json'
	f2 = urllib2.urlopen(url2)
	json_string = f2.read()
	parsed_json = json.loads(json_string)
	for day in parsed_json['forecast']['simpleforecast']['forecastday']:		#Enters a for Loop until all 4 periods are listed with the following information
		print day['date']['weekday'] + ' (' + day['date']['pretty'] + '):'
		print ' Conditions: ' + day['conditions']
		print ' High: ' + day['high']['fahrenheit'] + 'F'
		print ' Low: ' + day['low']['fahrenheit'] + 'F'
		print ' Average Humidity: ' + str(day['avehumidity']) + '%'
	f2.close()
	x=2
