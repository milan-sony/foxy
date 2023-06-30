import requests
import json

def get_proxies():
    url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&speed=fast&protocols=socks4%2Csocks5"
    response = requests.get(url)
    response_status = response.status_code

    if response_status != 200:
        print("Something went wrong with the connection from URL")
        exit()
    else:
        print("URL connection is successfull \nStatus Code: "+str(response_status))
        pass

    proxies_jsonresponse = response.json()
    print("--------JSON RESPONSES--------")
    print(proxies_jsonresponse)

get_proxies()