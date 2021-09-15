import requests
import folium
import json
# Input your ip address
ip_address = input("enter your ip address:")
# URL to send the request to
request_url =' https://geolocation-db.com/jsonp/' + ip_address + "?access_key=" + 'free'
# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
# Clean the returned string so it just contains the dictionary data for the IP address
result = result.split("(")[1].strip(")")
# Convert this data into a dictionary
result  = json.loads(result)
print(result)
lat=(result['latitude'])
print(lat)
lon=(result['longitude'])
print(lon)
fg = folium.FeatureGroup("My Map")
fg.add_child(folium.GeoJson(data = (open('indian_states.json','r',encoding='utf-8-sig').read())))
map = folium.Map(location=[lat, lon],popup="This is Your Location", zoom_start=12)
folium.Marker(
    [lat,lon],
).add_to(map)
map.add_child(fg)
map.save("1.html")



