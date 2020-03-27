# :pencil: Quiz for Telegram
> Post scheduled quizzes on Telegram using a list of questions from Google Sheets

## :electric_plug: Set up
1. Click the <kbd>Use this template</kbd> button on GitHub and create a **private repository**
1. Create a Telegram bot
    - Follow [these instructions](https://core.telegram.org/bots#creating-a-new-bot) to generate a token
    - Add your token to `config.py`
1. Connect to Google Sheets
    - Go to [Google Developer Console](https://console.developers.google.com/apis/dashboard) and create a new project
    - Click <kbd>+ ENABLE APIS AND SERVICES</kbd> and enable the "Drive API" as well as the "Sheets API"
    - Navigate to "APIs and Services" > "Credentials"
    - Click <kbd>+ CREATE CREDENTIALS</kbd> and select "Service account"
    - Fill in the required fields, press <kbd>CREATE</kbd>, <kbd>CONTINUE</kbd>, and on the last step click <kbd>+ CREATE KEY</kbd> to download a JSON file
    - Upload the JSON file at the root of your GitHub repo and add the filename to the `credentials` variable in `config.py`
    - Copy the [Google sheet template](https://docs.google.com/spreadsheets/u/1/d/1BE-ZbrkTejJloU_d953nYCKCqVSfoiQQCZ45Y3NSdtc/copy) and share it with the email address found in `client_email` in the JSON file
1. Configure options in `config.py`
    
| Option | Description | Type | Example |
| ------ | ----------- | ---- | ------- |
| `spreadsheet` | **Required** - The name of your Google sheet | String | Q4T Template |
| `channel` | **Required** - The unique identifier of your chat or the username of your channel | String | q4t_playground |
| `loop` | Whether of not the bot should loop through the questions if all the questions have been exhausted | Boolean | `True` |

##### :warning: Make sure your repository is private, because your Google credentials and Telegram token is sensitive information.

## :desktop_computer: Usage
You can add as many question/answer sets in your Google sheet as you want. Everytime the script is run, it will send a quiz to the target chat or channel and increment the index in the `index` sheet. You can keep adding more question/answer sets indefinitely.

### Run at scheduled interval
To send quizzes at a certain interval, run `src/main.py` at the specific interval. The recommended way to do this is to use [GitHub Actions](https://github.com/features/actions). Here is a sample workflow you can put in `.github/workflows/main.yml` to send a quiz every day:

```yml
name: Send quiz
on:
  schedule:
  - cron: '0 0 * * *'

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - uses: actions/setup-python@v1
      with:
        python-version: '>=3.6'
    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Send quiz
      run: python src/main.py
```

### Reset
To reset the spreadsheet, simply run `reset.py`. This will remove all questions and set the index to 2.
