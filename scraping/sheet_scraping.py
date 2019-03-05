import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from operator import itemgetter

from Person import Person


def pull_from_google(url):
    """
    Pulls raw paper data from Google Sheets

    Args:
        url (string): url of a Google sheet to pull data from

    Outputs:
        (list of strings): header row from sheet
        (list of lists): individual rows containing paper data
    """
    # setup connection
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
    gc = gspread.authorize(credentials)

    # pull papers from Delta Lab paper spreadsheet
    paper_worksheet = gc.open_by_url(url)

    # split into header and paper data
    header = paper_worksheet.get_worksheet(0).get_all_values()[0]
    responses = paper_worksheet.get_worksheet(0).get_all_values()[1:]

    return header, responses


def main():
    sheet_url = os.environ['SHEET_URL']
    header, rows = pull_from_google(sheet_url)

    print(header)
    print(rows)


if __name__ == '__main__':
    main()
