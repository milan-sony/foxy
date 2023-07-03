<p align="center">
    <img width="100" src="./web/fox-icon.png" alt="Icon">
</p>

<h1 align="center">
  FOXY<sub>PROXY</sub>
</h1>

<p align="center">A proxy server build with selenium webdriver for chrome in python</p>

<details>
  <summary>BTS</summary>
I recently saw an article on <a href="https://medium.com/">Medium</a> about how to make a proxy server of our own. After reading the <a href="https://thesocialproxy.medium.com/making-a-proxy-server-in-selenium-the-ultimate-guide-ee8b8a09f222">article</a> I got a basic idea of how to build one. First I tought to build it by scrapping all the free proxies available and apply the concept of rotating proxy and pass it to the selenium webdriver. Trust me! most of the free proxies out there is not working and most of addresses won't works with google and scrapping all the proxies availabe then getting the working one was very time consuming. So I search whether there is any libray for getting free proxies. After some searches I found one named <a href="https://pypi.org/project/free-proxy/">free proxy</a> I added this library to my code, it gave working IP addresses and the module also has many parameters, this helps me to find proxies with google LLc. Then I created custom options for the Selenium webdriver for chrome and pass the IP to it, then solved the problems faced like stoping the chrome from automatically closing, remote allow origins, accept insecure certificates etc. With Eel-python library i build one ui to to eter the url to the selenium to search
</details>

## Libraries used

- `tkinter`
- `playsound`

## Read documentation about

- <a href = "https://docs.python.org/3/library/tkinter.html">Tkinter</a>
- <a href = "https://www.healthline.com/health/eye-health/20-20-20-rule">20-20-20 rule</a>

## Run locally

You will need to install Python on you system, head over to https://www.python.org/downloads/ to download python.
(Dont Forget to tick `Add Python to PATH` while installing Python)

Once you have downloaded Python on your system, 
run the following command inside your terminal (only if your system is git enabled, otherwise download the zip file and extract it)

```bash
  git clone https://github.com/milan-sony/chronooptic.git
```

Then go to the project folder

```bash
  cd chronooptic
```

(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```

Activate the virtual environment

```bash
  venv/Scripts/activate
```

If error occurs when activating virtual environment, run the following command

```bash
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Then Install the dependencies needed for this project

```bash
  pip install -r requirements.txt
```

Now run the script

```bash
  python chronooptic.py
```

## Screenshot

<img src="Screenshot.png">
