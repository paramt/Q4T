import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import configure

# Authorize Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(configure.credentials, scope)
gc = gspread.authorize(credentials)

# Open sheets
datasheet = gc.open(configure.spreadsheet).worksheet("datasheet")
index = gc.open(configure.spreadsheet).worksheet("index")

# Get question and options from current index
index_val = index.cell(1, 1).value
question = datasheet.cell(index_val, 1).value
options = [datasheet.cell(index_val, i + 2).value for i in range(10)]
answer = options[0]
options = [option for option in options if option] # Remove blank questions
random.shuffle(options)
answer_index = options.index(answer)

url = f"https://api.telegram.org/bot{configure.token}/sendPoll"

query = {"chat_id": f"@{configure.channel}", "question": question,
		 "type":"quiz", "correct_option_id": answer_index}
response = requests.request("GET", url, params = query, json = {"options": options})

if response.json()["ok"] == True:
	# Increment index
	index.update("A1", int(index.cell(1, 1).value) + 1)
else:
	raise Exception("Unable to send Telegram message: " + response.json()["description"])
