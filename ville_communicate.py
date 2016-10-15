import requests
import lob
import webbrowser, random, threading
from flask import Flask, request, render_template
from ville_api_keys import *

#Use flask to create online server to receive info from ville_index.html
app = Flask(__name__)

@app.route('/')
def get_dat_letter():
	return render_template("ville_index.html")

@app.route('/', methods=['POST'])
def get_dat_letter_post():
	
	#Place online form response into a dictionary
	from_address = {
	'name': request.form['from_name'],
	'address_line1': request.form['from_address_1'],
	'address_line2': request.form['from_address_2'],
	'address_city': request.form['from_city'],
	'address_state': request.form['from_state'],
	'address_zip': request.form['from_zip']
	}

	#Format address string to create url for google API
	from_address_string = ""
	for from_address_key in ['address_line1', 'address_line2', 'address_city', 'address_state', 'address_zip']:
		from_address_string += from_address[from_address_key] 

	#Create custom url with user info
	get_rep_url = "https://www.googleapis.com/civicinfo/v2/representatives?" \
	"address={0}&includeOffices=true&levels=administrativeArea1&" \
	"roles=headOfGovernment&key={1}" .format(from_address_string, VILLE_GOOGLE_API_KEY)

	#Get representative info from google civic info API using user info
	r = requests.get(get_rep_url)
	#Make the response pretty
	google_response = r.json()

	#Because line 2 can be empty, prevents exception
	try:
		to_address = {'address_line2': google_response['officials'][0]['address'][0]['line2']}
	except Exception, e:
		to_address = {'address_line2': " "}

	#Place representative info into a dictionary
	try:
		to_address = {
		'name': google_response['officials'][0]['name'],
		'address_line1': google_response['officials'][0]['address'][0]['line1'],
		'address_city': google_response['officials'][0]['address'][0]['city'],
		'address_state': google_response['officials'][0]['address'][0]['state'],
		'address_zip': google_response['officials'][0]['address'][0]['zip']
		}
	except Exception, e:
		return "Sorry, no Governor information could be found with the info provided. Either move or try again."

	#Use Lob API to create letter with above information
	try: 
		lob.api_key = VILLE_LOB_API_KEY
		letter = lob.Letter.create(
			description = 'Letter to Representative',
			#Dictionary from Google response
			to_address = to_address,
			#Dictionary from online form
			from_address = from_address,
			file = '<html style="padding-top: 3in; margin: .5in;">Dear {{name}},\
			<br><br>{{content}}<br><br><br>{{closing}}<br>{{from_name}}</html>',
			data = {
			'name': to_address['name'],
			#Receives letter content from the online form
			'content': request.form['letter_content'],
			'closing': "Sincerely,",
			'from_name': from_address['name']
			},
			color = True
			)
	except Exception, e:
		return "Sorry, I couldn't make a letter with your info."


	letter_url = letter["url"]
	#Print url to the terminal
	print "\nLetter URL:\n{0}\n" .format(letter_url)
	webbrowser.open(letter_url)
	return ('', 204)

if __name__ == '__main__':
	# Open the webpage in default browser
	port = 5000 + random.randint(0, 999)
	url = "http://127.0.0.1:{0}" .format(port)
	threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
	app.run(port=port, debug=False)
