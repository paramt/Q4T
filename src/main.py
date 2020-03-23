import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import config
import reset

# Authorize Google Sheets
try:
	scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name(config.credentials, scope)
	gc = gspread.authorize(credentials)
except OSError as e:
	print("JSON file with Google account credentials not found!")
	print("Make sure you've followed the README instructions and added the filepath of your credentials file to config.py")
	exit(1)

# Open sheets
datasheet = gc.open(config.spreadsheet).worksheet("datasheet")
index = gc.open(config.spreadsheet).worksheet("index")

# Get question and options from current index
index_val = index.cell(1, 1).value
question = datasheet.cell(index_val, 1).value

if question == "":
	if config.loop:
		reset.reset_index()
		index_val = index.cell(1, 1).value
		question = datasheet.cell(index_val, 1).value
	else:
		print("No questions found in the Google sheet!")
		exit(1)

options = [datasheet.cell(index_val, i + 2).value for i in range(10)]
answer = options[0]
options = [option for option in options if option] # Remove blank questions
random.shuffle(options)
answer_index = options.index(answer)

url = f"https://api.telegram.org/bot{config.token}/sendPoll"

query = {"chat_id": f"@{config.channel}", "question": question,
		 "type":"quiz", "correct_option_id": answer_index, "is_anonymous": config.anonymous}
response = requests.request("GET", url, params = query, json = {"options": options})

if response.json()["ok"] == True:
	# Increment index
	index.update("A1", int(index_val) + 1)
else:
	raise Exception("Unable to send Telegram message: " + response.json()["description"])
