import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
 
import folium
 
from opencage.geocoder import OpenCageGeocode
 
number = input("Enter the PhoneNumber with the country code : ")

phoneNumber = phonenumbers.parse(number)

Key = "ChIJvXERGk2WyzsRhvXnJgV-qAs" #generate your api https://opencagedata.com/api
 
yourLocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+yourLocation)

yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+yourServiceProvider)
 
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
 
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
 
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)
 
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
 
myMap.save("Location.html")

