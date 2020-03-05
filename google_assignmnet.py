import requests
import webbrowser

# https://developers.google.com/maps/documentation/urls/guide#forming-the-map-url
# Google map direction calling address.
GOOGLE_MAPS_API_URL = 'https://www.google.com/maps/dir/?api=1'


# 목적지, 도착시 string 입력
origin_A = input("Enter the origin location:  ")
destination_B = input("Enter the destination location  ")

# 입력받은 parameter 값 각 origin, destination 할당
param = {'origin': origin_A,
         'destination': destination_B}

# Module calling
req = requests.get(GOOGLE_MAPS_API_URL, params=param)
print(req.url)
webbrowser.open(req.url)
