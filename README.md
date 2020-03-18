# Quiz for Telegram
> Post scheduled quizzes using a list of questions from Google Sheets

## Set up
1. Clone this repo
1. Install dependencies
1. Create a Telegram bot
    - Follow [these instructions](https://core.telegram.org/bots#creating-a-new-bot) to generate a token
    - Add your token to `configure.py`
1. Connect to Google Sheets
    - Go to [Google Developer Console](https://console.developers.google.com/apis/dashboard) and create a new project
    - Click <kbd>+ ENABLE APIS AND SERVICES</kbd> and enable the "Drive API" as well as the "Sheets API"
    - Navigate to "APIs and Services" > "Credentials"
    - Click <kbd>+ CREATE CREDENTIALS</kbd> and select "Service account"
    - Fill in the required fields, press <kbd>CREATE</kbd>, <kbd>CONTINUE</kbd>, and on the last step click <kbd>+ CREATE KEY</kbd> to download a JSON file
    - Add the path to the downloaded json file to `configure.py`
    - Copy the [Google sheet template](https://docs.google.com/spreadsheets/u/1/d/1BE-ZbrkTejJloU_d953nYCKCqVSfoiQQCZ45Y3NSdtc/copy) and share it with the email address found in `client_email` in the JSON file
1. Configure options in `configure.py`
    - Set the value of `spreadsheet` to the name of your Google sheet
    - Set the value of `channel` to the unique identifier of your chat or username of your channel

## Usage
You can add as many question/answer sets in your Google sheet as you want. Everytime the script is run, it will send a quiz to the target chat or channel and increment the index in the `index` sheet. You can keep adding more question/answer sets indefinitely, but if you want to reset then delete all previous questions and set the index to `2`.
