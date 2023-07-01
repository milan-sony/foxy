from fp.fp import FreeProxy
from fp.errors import FreeProxyException
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

proxy_list = []

# proxy = FreeProxy().get()
# def get_proxy():
    
#     main()

def main():
    try:
        proxy = FreeProxy(google=True).get()
        print(proxy)
        # proxy_list.append(proxy)
    except FreeProxyException:
        print("No Proxy Found")
    # define custom options for the Selenium driver
    options = Options()
    # To stop chrome from automatically closing
    options.add_experimental_option("detach", True)
    # free proxy server URL
    # proxy = get_proxy()
    proxy_server_url = proxy
    options.add_argument(f'--proxy-server={proxy_server_url}')

    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install()))

    link = 'https://www.expressvpn.com/what-is-my-ip'

    # Maximize browser window
    driver.maximize_window()
    driver.get(link)
    time.sleep(2)

main()

