import requests
import json
import time
import queue
import threading

proxy_list = []

# def get_proxies():
#     url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&speed=fast&protocols=socks4%2Csocks5"
#     response = requests.get(url)
#     response_status = response.status_code

#     if response_status != 200:
#         print("Something went wrong with the connection from URL")
#         exit()
#     else:
#         print("URL connection is successfull \nStatus Code: "+str(response_status))
#         pass

#     proxies_jsonresponse = response.json()
#     print("--------JSON RESPONSES--------")
#     # print(proxies_jsonresponse)
#     with open("free_proxy_list.json", "w") as json_proxy_file:
#         json.dump(proxies_jsonresponse, json_proxy_file)
#         json_proxy_file.close()
#     newfun()
#     time.sleep(1)
#     list_proxies()

def  list_proxies():
    global proxy_list
    with open('free_proxy_list.json', 'r') as json_proxy_file:
        proxy_data = json.load(json_proxy_file)

    # entry = data['data'][0]
    # print(entry)
    # ip = entry['ip']
    # print("IP:", ip)

    for proxies in proxy_data['data']:
        # print(entry)
        ip = proxies['ip']
        port = proxies['port']
        country = proxies['country']
        city = proxies['city']
        speed = proxies['speed']
        latency = proxies['latency']
        response_time = proxies['responseTime']
        anonymityLevel = proxies["anonymityLevel"]
        # print("IP: ", ip)
        # print("Port: ", port)
        proxy_ip = ip+":"+port
        # print(proxy_ip)
        proxy_list.append(proxy_ip)
        proxy_count = len(proxy_list)
        print(proxy_list)
        print(proxy_count)

        # ips = queue.put(proxy_ip)
        # print(queue.get(ips))
    # check_proxies()

# def check_proxies():
#     global proxy_list
#     while not queue.empty():
#         proxy = queue.get()
#         try:
#             url = "http://ipinfo.io/json"
#             res = requests.get(
#                 url,
#                 proxies={"http":proxy,
#                         "https":proxy})
#         except:
#             print("some problem occur in check proxies")
#             continue
#         if res.status_code == 200:
#             print({proxy})


def check_proxies():
    global proxy_list
    if len(proxy_list) != 0:
        for proxy in proxy_list:
            try:
                url = "http://ipinfo.io/json"
                response = requests.get(
                    url,
                    proxies={"http":proxy,
                            "https":proxy})
            except:
                print("some problem occur in check proxies")
                pass
            if response.status_code == 200:
                print({proxy})
    else:
        print("proxy list is empty")
# thread = threading.Thread(target=check_proxies).start()


def newfun():
    print("Helllo")

list_proxies()