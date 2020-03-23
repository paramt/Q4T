import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
import config

# Authorize Google Sheets
try:
	scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name(config.credentials, scope)
	gc = gspread.authorize(credentials)
except OSError:
	print("JSON file with Google account credentials not found!")
	print("Make sure you've followed the README instructions and added the filepath of your credentials file to config.py")
	exit(1)

# Reset index to 2
def reset_index():
	gc.open(config.spreadsheet).worksheet("index").update("A1", 2)

# Reset datasheet
def reset_datasheet():
	datasheet = gc.open(config.spreadsheet).worksheet("datasheet")
	cells_to_delete = datasheet.range("A2:Z1000")
	for cell in cells_to_delete: cell.value = ""
	datasheet.update_cells(cells_to_delete)

if __name__ == "__main__":
	reset_datasheet()
	reset_index()
