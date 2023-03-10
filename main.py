# Imports libraries
import requests
import os
from bs4 import BeautifulSoup

# Loads secret variable
url = os.environ['url']

# Function for calling all functions
def call_all_functions():
	stepone()
	steptwo()
	stepthree()
	stepfour()

# Removes old files
try:
	os.remove("spans.html")
	os.remove("images.txt")
	os.remove("captions.txt")
except:
	pass

# STEP ONE
# GET WEBSITE CONTENT

def stepone():
	# Gets response
	r = requests.request("GET", url)
	
	# Saves response
	response = r.text
	
	# Converts to BeautifulSoup
	soup = BeautifulSoup(response, "html.parser")
	
	# Finds all "span" elements
	spans = soup.find_all("span", {"style": "FONT-SIZE: 12pt"})
	
	# Sets increment, used to see how many items in spans
	increment = 1
	
	# Opens spans
	f = open("spans.html", "a")
	
	# Saves to spans
	for item in spans:
		# Checks the amount of times this has looped
		if (increment <= 2):
			# If the first two times, do not include
			pass
		else:
			# If not the first two times, continue

			# Writes to spans
			f.write(str(item))

		# Increases increment
		increment += 1
	
	# Close file
	f.close()
	
	# Prints increment and success confirmation
	print(f'Step One Completed\nTotal lines scraped: {increment}')

# STEP TWO
# MODIFY WEBSITE CONTENT

def steptwo():
	# Opens spans on read mode
	f = open("spans.html", "r")

	# Reads and saves to variable
	relative_links = f.read()

	# Closes spans on read mode
	f.close()

	# Converts all mentions of "src=" to "src=[BASE URL]" in order to convert to absolute links
	absolute_links = relative_links.replace('src="', f'src="{url}')

	# Opens spans on write mode
	f = open("spans.html", "w")

	# Overwrites spans with new version
	f.write(absolute_links)

	# Closes spans
	f.close()

	# Prints success confirmation
	print("Step Two Completed")

# STEP THREE
# GET ALL IMAGES

def stepthree():
	# Opens spans on read mode
	f = open("spans.html", "r")
	
	# Reads spans and saves to variable
	cluttered = f.read()
	
	# Closes spans
	f.close()
	
	# Converts to BeautifulSoup
	soup = BeautifulSoup(cluttered, "html.parser")
	
	# Finds all images
	images = soup.find_all("img")
	
	# Opens images file
	f = open("images.txt", "a")

	for item in images:
		# Writes to file
		f.write(str(item))
	
	# Closes images
	f.close()

	# Prints success confirmation
	print("Step Three Completed")

# STEP FOUR
# GETS ALL CAPTIONS

def stepfour():
	# Opens spans on read mode
	f = open("spans.html", "r")
	
	# Reads spans and saves to variable
	cluttered = f.read()
	
	# Closes spans
	f.close()
	
	# Converts to BeautifulSoup
	soup = BeautifulSoup(cluttered, "html.parser")
	
	# Finds all links
	captions = soup.select('p a[href]')
	
	# Opens captions file
	f = open("captions.txt", "a")
	
	for item in captions:
		# Writes caption
		f.write(str(item))
	f.close()

call_all_functions()

