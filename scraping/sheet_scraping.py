import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from operator import itemgetter

from Person import Person


def pull_from_google(url):
    """
    Pulls raw people data from Google Sheets.

    :param url: (string): url of a Google sheet to pull data from
    :return: (list of strings): header row from sheet
    :return: (list of lists): individual rows containing paper data
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


def remap_list_values(orig_values, remapping):
    """
    Remaps values in a list to new values based on remapping dict.

    :param orig_values: (list of strings) list of values to be remapped.
    :param remapping: (dict of strings) remapping from orig_values to new values.
    :return: (list of strings) list of remapped values based on remappings.
    """
    return [remapping[x] if x in remapping else x for x in orig_values]


def create_person(field_lookup, data):
    """
    Creates a Person object given data for a person and a dict containing mappings from field to index in list for data.

    :param field_lookup: (dict) dict mapping fields needed for person data to indices.
    :param data: (list) list of data to use for creating person.
    :return: (Person) new Person object with given data.
    """
    return Person(data[field_lookup['first_name']],
                  data[field_lookup['last_name']],
                  data[field_lookup['year']],
                  data[field_lookup['major']],
                  data[field_lookup['academic_interests']],
                  data[field_lookup['post_grad_goal']],
                  data[field_lookup['software_experience']],
                  data[field_lookup['hobbies']])


def main():
    sheet_url = os.environ['SHEET_URL']
    header, rows = pull_from_google(sheet_url)

    # remap headers
    header_remapping = {
        'Timestamp': 'timestamp',
        'First Name': 'first_name',
        'Last Name': 'last_name',
        'What is your year in school?': 'year',
        'What is your major?': 'major',
        'What are your academic interests?': 'academic_interests',
        'Currently, what is your post-graduation goal?': 'post_grad_goal',
        'What software development experience do you have?': 'software_experience',
        'What are some of your hobbies?': 'hobbies'
    }
    remapped_header = remap_list_values(header, header_remapping)
    header_lookup = {remapped_header[i]: i for i in range(0, len(remapped_header))}

    # create Person objects for each person with their responses
    people = [create_person(header_lookup, person_data) for person_data in rows]

    # create and export krf file
    file_output = '\n'.join(['(in-microtheory KRR-Winter2019FactsMt)',
                             '(genlMt KRR-Winter2019FactsMt SocialModelingMt)',
                             '(genlMt KRR-Winter2019FactsMt NUPeopleLanguageInfoMt)',
                             '(genlMt KRR-Winter2019InClassMt KRR-Winter2019FactsMt)',
                             '(genlMt KRR-Winter2019RulesMt KRR-Winter2019FactsMt)'])

    file_output += '\n\n'

    for person in people:
        file_output += person.generate_krf() + '\n\n'

    file = open('../krf/people.krf', 'w')
    file.write(file_output)
    file.close()


if __name__ == '__main__':
    main()
