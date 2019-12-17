# Gina Gross, test form B
import urllib.request, urllib.error, urllib.parse, json


# I know how to access all of the relevant information!! The one thing that's killing me is I cannot remember how to
# load in the API! I looked at our Flickr example, but is this API RESTful? i don't know. (APIs are really confusing
# for me, though I understand more what they are now, but for some reason, I cannot remember the exact 'how' to load
# in this demo API, and have it present to use. I tried to replicate the flickrREST, but super complicated and confusing
# and didn't seem correct! Anyway, so I want you to understand that I know all the logic of accessing this API, I
# am just fumbling with how exactly to load it in. So, I don't know if my building blocks (not the classes, but the two functions)
# are faulty, but I'm going to try to do the tasks assuming they are - with correct logic etc.

def getFlights(user="1", params={}):
    params[method] = "flights.flights"
    return json.load(urllib.request.urlopen("http://hcde310demo.appspot.com/api/v2" + "?" + urllib.parse.urlencode(params))["flights"]


def getAirports(airportsList):
    method = "airports.getInfo"
    return json.load(urllib.request.urlopen("http://hcde310demo.appspot.com/api/v2" + "?" + urllib.parse.urlencode(params))["results"]

class Flight():
    def __init__(self,flightInfo):
        self.fromAirport = flightInfo["flights"]["fromAirport"]
        self.toAirport = flightInfo["flights"]["toAirport"]
        self.date = flightInfo["flights"]["date"]
        self.aircraftType = flightInfo["flights"]["aircraftType"]

class Airport():
    def __init__(self,airportInfo):
        self.iata = airportInfo["results"]["airport"]["iata"]
        self.name = airportInfo["results"]["airport"]["airportName"]
        self.city = airportInfo["results"]["airport"]["city"]
        self.country = airportInfo["results"]["airport"]["country"]
        self.latitude = airportInfo["results"]["airport"]["location"]["lat"]
        self.longitude = airportInfo["results"]["airport"]["location"]["lng"]

# = 2.1 =
# Unfortunately, I spent all of my time trying to remember the correct way to invoke this API. :( I didn't even get to
# the fun part of actually messing around with it! I love it when during the exam you forget how to do the basics. -_-