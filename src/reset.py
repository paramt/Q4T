import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
import configure

# Authorize Google Sheets
try:
	scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name(configure.credentials, scope)
	gc = gspread.authorize(credentials)
except OSError:
	print("JSON file with Google account credentials not found!")
	print("Make sure you've followed the README instructions and added the filepath of your credentials file to configure.py")
	exit(1)

# Reset index to 2
gc.open(configure.spreadsheet).worksheet("index").update("A1", 2)

# Open datasheet
datasheet = gc.open(configure.spreadsheet).worksheet("datasheet")

# Reset datasheet
cells_to_delete = datasheet.range("A2:Z1000")
for cell in cells_to_delete: cell.value = ""
datasheet.update_cells(cells_to_delete)
