from fp.fp import FreeProxy
from fp.errors import FreeProxyException

# custom user agent
from user_agent import generate_user_agent, generate_navigator

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def main():
    try:
        proxy = FreeProxy(google=True).get()
        print("Proxy Adderss")
        print(proxy)
    except FreeProxyException:
        print("No Proxy Found")
        exit()

    # generate a user agent
    generate_user_agent()
    user_agent = generate_navigator()

    # define custom options for the Selenium driver
    options = Options()

    # user agent
    options.add_argument(f"user-agent={user_agent}")

    # free proxy server URL
    proxy_server_url = proxy
    options.add_argument(f'--proxy-server={proxy_server_url}')

    # to stop chrome from automatically closing
    options.add_experimental_option("detach", True)

    # translate page to english
    options.add_argument("--lang=en-GB")
    # options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

    # remote allow origins
    options.add_argument('--remote-allow-origins=*')

    # accept insecure certificates
    # http://allselenium.info/selfsigned-certificates-python-selenium/
    options.set_capability("acceptInsecureCerts", True)

    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install()))

    link = 'https://whatismyipaddress.com/'

    # maximize browser window
    driver.maximize_window()
    driver.get(link)

main()