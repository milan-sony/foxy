import eel

# initializing the application
eel.init("web")

# exposing the sum function to javascript
@eel.expose	
def get_url(num1, num2):
	sum = int(num1) + int(num2)
	return sum

# start the index.html file /
# starting the application
eel.start("index.html")
